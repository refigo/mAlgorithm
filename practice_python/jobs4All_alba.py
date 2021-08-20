import os
import csv
import requests
from bs4 import BeautifulSoup


def save_to_file(name, jobs_info_lists):
  name = name.replace("/","_")
  file = open(f"{name}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place","title","time","pay","date"])
  for job_info in jobs_info_lists:
    writer.writerow(job_info)
  file.close()
  return

def find_jobs(name, url):
  company_rq = requests.get(url)
  company_soup = BeautifulSoup(company_rq.text, "html.parser")
  job_table = company_soup.find("div", {"class":"goodsList"}).find("table").find("tbody")

  jobs_info_lists = []
  job_trs = job_table.find_all("tr")
  for job_tr in job_trs:
    try:
      if "summaryView" in job_tr["class"]:
        continue
    except:
      pass
    try:
      job_place = job_tr.find("td",{"class":"local"}).text.strip()
    except:
      job_place = ""
    try:
      job_title = job_tr.find("td",{"class":"title"}).find("span",{"class":"company"}).text.strip()
    except:
      job_title = ""
    try:
      job_time = job_tr.find("td",{"class":"data"}).text.strip()
    except:
      job_time = ""
    try:
      job_pay = job_tr.find("td",{"class":"pay"}).text.strip()
    except:
      job_pay = ""
    try:
      job_date = job_tr.find("td",{"class":"regDate"}).text.strip()
    except:
      job_date = ""
    jobs_info_lists.append([job_place, job_title, job_time, job_pay, job_date])
  save_to_file(name, jobs_info_lists)
  return

def init():
  os.system("clear")
  alba_url = "http://www.alba.co.kr"
  alba_rq = requests.get(alba_url)
  alba_soup = BeautifulSoup(alba_rq.text, "html.parser")

  main_super_brand_list = alba_soup.find("div", {"id":"MainSuperBrand"}).find_all("li", {"class":"impact"})
  for each in main_super_brand_list:
    brand_info = each.find("a", {"class":"goodsBox-info"})
    company_name = brand_info.find("span", {"class":"company"}).get_text().strip()
    print(f"Scrapping {company_name}..")
    company_url = brand_info["href"]
    find_jobs(company_name, company_url)
  print("Done! Goodbye~")

init()
