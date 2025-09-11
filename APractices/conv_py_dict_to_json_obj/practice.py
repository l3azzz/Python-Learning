import json


python_obj = {
    "name": "David",
    "class": 1,
    "age": 6
}
converted_json = json.dumps(python_obj)
print(type(converted_json))