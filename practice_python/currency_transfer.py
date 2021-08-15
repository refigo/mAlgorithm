#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"

def convert_currency(code_1, code_2):
  while True:
    print(f"\nHow many {code_1} do you want to convert to {code_2}")
    try:
      amount = int(input())
      break
    except ValueError:
      print("That wasn't a number.")
      continue
  currency_url = f"https://wise.com/gb/currency-converter/{code_1.lower()}-to-{code_2.lower()}-rate?amount={amount}"
  currency_r = requests.get(currency_url)
  currency_soup = BeautifulSoup(currency_r.text, "html.parser")
  source_to_target = float(currency_soup.find("h3", {"class":"cc__source-to-target"}).find("span", {"class":"text-success"}).get_text())
  result = amount * source_to_target
  #print(f"{result:0,.0f}")
  print(f"{format_currency(amount, code_1, locale='ko_KR')} is {format_currency(result, code_2, locale='ko_KR')}")
    

def get_input(country_list):
  while True:
    try:
      number = int(input("#: "))
    except ValueError:
      print("That wasn't a number.")
      continue
    try:
      return country_list[number]
    except IndexError:
      print("Choose a number from the list.")


def init():
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

  print("Welcome to CurrencyConvert PRO 2000\n")
  for index, value in enumerate(country_list):
    print("#", index, value["country"])

  print("\nWhere are you from? Choose a country by number.\n")
  choose_first = get_input(country_list)
  print(choose_first["country"])

  print("\nNow choose another country.\n")
  choose_second = get_input(country_list)
  print(choose_second["country"])

  convert_currency(choose_first["code"], choose_second["code"])

init()

