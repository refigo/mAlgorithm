import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

def find_info_by_id(id):
  for pop in db["popular"]:
    if pop["id"] == id:
      return pop
  for new in db["new"]:
    if new["id"] == id:
      return new

@app.route("/<id>")
def get_id_comments(id):
  id_info = find_info_by_id(id)
  r_comments = requests.get(f"{base_url}/search?tags=comment,story_{id}")
  json_comments = r_comments.json()
  hits_comments = json_comments["hits"]

  list_comments = []
  for hit in hits_comments:
    author = hit.get("author")
    comment_text = hit.get("comment_text")
    list_comments.append({"author":author, "comment_text":comment_text})
  return render_template("detail.html", info=id_info, comments=list_comments)

def get_new():
  r_new = requests.get(new)
  json_new = r_new.json()
  hits_new = json_new["hits"]
  
  new_list = db.get("new")
  if not new_list:
    new_list = []
    for hit in hits_new:
      new_list.append({"title":hit["title"], "url":hit["url"], "points":hit["points"], "author":hit["author"], "num_comments":hit["num_comments"], "id":hit["objectID"]})
    db["new"] = new_list
  return render_template("index.html", new=True, hits=new_list)

def get_popular():
  r_popular = requests.get(popular)
  json_popular = r_popular.json()
  hits_popular = json_popular["hits"]
  
  popular_list = db.get("popular")
  if not popular_list:
    popular_list = []
    for hit in hits_popular:
      popular_list.append({"title":hit["title"], "url":hit["url"], "points":hit["points"], "author":hit["author"], "num_comments":hit["num_comments"], "id":hit["objectID"]})
    db["popular"] = popular_list
  return render_template("index.html", popular=True, hits=popular_list)

@app.route("/")
def home():
  order_by = request.args.get("order_by")
  if order_by == "popular":
    return get_popular()
  elif order_by == "new":
    return get_new()
  elif not order_by:
    return get_popular()

app.run(host="0.0.0.0")
