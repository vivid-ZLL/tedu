import json

# dumps ,loads
item01 = {'name': 'Alice', 'id': '001'}
print(item01)
print(type(item01))

item = json.dumps(item01)
print(item)
print(type(item))

# dump,load
list01 = [
    {'name': 'Alice', 'id': '001'},
    {'name': 'Alicinya', 'id': '002'}
]

with open('alpha', 'w') as f:
    json.dump(list01, f, ensure_ascii=False)
