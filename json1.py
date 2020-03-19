import json
person_json = '{"name":"Tanay","age":20,"college":"PICT"}'
person_dict = json.loads(person_json)

person_json2 = json.dumps(person_dict)

print(person_dict)
print(person_json)

with open("person.json") as f:
    var = json.load(f)

with open("person.txt","w") as f:
    json.dump(person_dict,f)


print(var)