import json
json_string = '{"name":"Abubakr" , "age":18 }'
data = json.loads(json_string)
print(data)
print(type(data))