import json

with open('info.json', 'r') as json_f:
    a = json.load(json_f)


print(a)

