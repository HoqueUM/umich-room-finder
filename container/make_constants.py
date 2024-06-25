import json

with open('classrooms.json', 'r') as file:
    data = json.load(file)

arr = data['Classrooms']['Classroom']
ids = []

for classroom in arr:
    ids.append(classroom['FacilityID'])

with open('constants.json', 'w') as file:
    json.dump(ids, file, indent=4)