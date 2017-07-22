import json

jpid = "040B1001"
path = 'static/TTM/JSON/' + jpid + '.json'

with open(path) as json_file:
    json_data = json.load(json_file)
    print(json_data)


print('\n\n')

json_1 = json.dumps(list(json_data))
json_2 = json.loads(json_1)
print(json_2)

print('\n\n')

json_3 = json.dumps('static/TTM/JSON/routes.json')
json_4 = json.loads(json_3)
print(json_4)






