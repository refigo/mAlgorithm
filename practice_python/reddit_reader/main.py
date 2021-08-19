import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")

@app.template_filter()
def thousandFormat(value):
    #value = float(value)
    return "{:0,}".format(value)

def get_subreddit_data(subreddit, agg_list):
  r_subreddit = requests.get(f"https://www.reddit.com/r/{subreddit}/top/?t=month", headers=headers)
  soup_subreddit = BeautifulSoup(r_subreddit.text, "html.parser")
  posts = soup_subreddit.find("div", {"class":"_31N0dvxfpsO6Ur5AKx4O5d"}).find_all("div", {"class":["_1oQyIsiPHYt6nx7VOmd1sz", "scrollerItem", "Post"]})

  for post in posts:
    try:
      if "promoted" == post.find("span", {"class":"_2oEYZXchPfHwcf9mTMGMg8"}).get_text():
        print("Promoted, get out of here!")
        continue
    except:
      pass
    title = post.find("h3", {"class":"_eYtD2XCVieq6emjKBH3m"}).get_text()
    try:
      link = post.find("a", {"class":"_3jOxDPIQ0KaOWpzvSQo-1s"})["href"]
    except:
      continue
    upvotes = post.find("div", {"class":"_1E9mcoVn4MYnuBQSVDt1gC"}).get_text()
    if 'k' in upvotes:
      k_idx = upvotes.index('k')
      upvotes = float(upvotes[:k_idx]) * 1000

    post_dict = {"title":title, "link":link, "upvotes":int(upvotes), "subreddit":subreddit}
    agg_list.append(post_dict)
  return

@app.route("/read")
def read():
  to_aggregate = request.args
  agg_list = []
  for subreddit in to_aggregate:
    print(f"Scrapping r/{subreddit}...")
    get_subreddit_data(subreddit, agg_list)
  sorted_agg_list = sorted(agg_list, key= lambda x: x["upvotes"], reverse=True)

  return render_template("read.html", subreddit_to_aggregate=to_aggregate, aggregated_list=sorted_agg_list)

@app.route("/")
def home():
  return render_template("home.html", subreddits=subreddits)

app.run(host="0.0.0.0")

