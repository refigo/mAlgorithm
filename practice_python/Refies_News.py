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


@app.route("/")
def home():
  get_popular()
  return "Hello"

@app.route("/?order_by=popular")
def get_popular():
  r_popular = requests.get(popular)
  print(r_popular)
  json_popular = r_popular.json()
  hits_popular = json_popular["hits"]
  for hit in hits_popular:
    print(hit["title"])

  return "Popular"

@app.route("/?order_by=new")
def get_new():
  return "New"

@app.route("/<id>")
def news_id(id):
  return "id"

app.run(host="0.0.0.0")
