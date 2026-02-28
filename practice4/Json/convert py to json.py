import json

data = {
    "name": "Abubakr",
    "age": 18,
    "is_student": True
}

json_string = json.dumps(data)

print(json_string)
print(type(json_string))