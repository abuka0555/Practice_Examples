import json
data = {
    "name":"Abubakr",
    "age" : 18,
    "is_student": True
}

with open("data.json", "w") as file:
    json.dump(data,file,indent=4)