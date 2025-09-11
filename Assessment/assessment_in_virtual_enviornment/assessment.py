# JSON ഫയൽ വായിക്കാൻ ഒരു python പ്രോഗ്രാം എഴുതുക 
import json
data = {"name" : "John", "age": 30, "city": "NewYork"}

with open ("users.json", "r" ) as json_file:
    json_from_file = json.load(json_file)