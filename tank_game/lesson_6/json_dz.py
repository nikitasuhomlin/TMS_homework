import json

with open('json_dz.json', 'r') as f:
    data = json.load(f)
    print(type(data))
    print(data['id'])
