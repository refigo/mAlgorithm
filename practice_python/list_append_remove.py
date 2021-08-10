#!/usr/bin/env python3

def is_on_list(days, name):
  for day in days:
    if day == name:
      return True
  return False

def get_x(days, number):
  return days[number]

def add_x(days, name):
  days.append(name)

def remove_x(days, name):
  days.remove(name)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

