#!/usr/bin/env python3

def add_to_dict(a_dict={}, word="", definition=""):
  if type(a_dict) is dict:
    if not word or not definition:
      return print("You need to send a word and a definition.")
    if word in a_dict:
      return print(word, "is already on the dictionary. Won't add.")
    else :
      a_dict[word] = definition
      return print(word, "has been added.")
  else :
    return print("You need to send a dictionary. You sent:", type(a_dict))
  
def get_from_dict(a_dict={}, word=""):
  if type(a_dict) is dict:
    if not word:
      return print("You need to send a word to search for.")
    if word in a_dict:
      return print(word + ": " + a_dict[word])
    else :
      return print(word, "was not found in this dict.")
  else :
    return print("You need to send a dictionary. You sent:", type(a_dict))

def update_word(a_dict={}, word="", definition=""):
  if type(a_dict) is dict:
    if not word or not definition:
      return print("You need to send a word and a definition to update.")
    if word in a_dict:
      a_dict[word] = definition
      return print(word, "has been updated to:", a_dict[word])
    else :
      return print(word, "is not on the dict. Can't update non-existing word.")
  else :
    return print("You need to send a dictionary. You sent:", type(a_dict))

def delete_from_dict(a_dict={}, word=""):
  if type(a_dict) is dict:
    if not word:
      return print("You need to specify a word to delete.")
    if word in a_dict:
      del a_dict[word]
      return print(word, "has been deleted.")
    else :
      return print(word, "is not in this dict. Won't delete.")
  else :
    return print("You need to send a dictionary. You sent:", type(a_dict))

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\


