#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"

country_r = requests.get(url)

country_soup = BeautifulSoup(country_r.text, "html.parser")

country_table = country_soup.find("table", {"class":"table"})

country_tr = country_table.find("tbody").find_all("tr")

country_list = []
for each in country_tr:
  country = each.select("tr > td")[0].get_text(strip="true").capitalize()
  code = each.select("tr > td")[2].get_text(strip="true")
  if code:
    country_dict = {"country": country, "code":code}
    country_list.append(country_dict.copy())

sorted_country_list = sorted(country_list, key=lambda k : k["country"])

print("Hello! Please choose select a country by number:")
for index, value in enumerate(sorted_country_list):
  print("#", index, value["country"])

while True:
  try:
    number = int(input("#: "))
  except ValueError:
    print("That wasn't a number.")
    continue
  try:
    selected_country = sorted_country_list[number]
    print("You choose", selected_country["country"])
    print("The currency code is", selected_country["code"])
    break
  except IndexError:
    print("Choose a number from the list.")

