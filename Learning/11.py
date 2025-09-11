# NETWORKING 






















# VIDEO 1 : JSON

# json is a datatype now it is suppported by various languages 
# to acces or read or modify we need json module

import json

movie_dict = {
  "movies": [
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "year": 2010
    },
    {
      "title": "The Lord of the Rings: The Fellowship of the Ring",
      "director": "Peter Jackson",
      "year": 2001
    },
    {
      "title": "Parasite",
      "director": "Bong Joon Ho",
      "year": 2019
    }
  ]
}

# now how to convert dictionary to json



# dumps is used to convert json to string
json_movie_dict = json.dumps(movie_dict, indent=4) # indent referse to spaces to put in json doc
#print(type(json_movie_dict)) #it's converted to a string
#print(json_movie_dict) # print the string json in terminal


                       # "w" means write
with open("movies.json","w") as json_file: # creates or open movies.json file
    json.dump(movie_dict,json_file)   # dumb meanns it is ready to wrtie to a file now
             


converted_dict = json.loads(json_movie_dict)
#print(type(converted_dict))
                       # "r" means read
with open ("movies.json", "r" ) as json_file:
    json_from_file = json.load(json_file)
    #print(json_from_file)













# video 2 : REQUESTS Get Metho

# in python for handling this we use request it's a library also 
# pip install request
import requests


r = requests.get("https://traveller.talrop.works/api/v1/places/")
#print(r) # print if we have gotten
#print(r.text) # print in plain text
#print(r.json()) # print in json only work if that is in json
#print(type(r.text)) # print's r.text type
#print(type(r.json())) # print type of r.json dict method

# this how we get info like json from https










# video 3 : Request Post Method


r = requests.get("https://traveller.talrop.works/api/v1/places/")


# 10 sec


