from token_generator import token_generator
import requests
import json
from test import json_maker

token_generator('classrooms')

with open('classrooms.json', 'r') as file:
    # Step 3: Load the JSON content from the file into a Python dictionary
    data = json.load(file)

# Step 4: Now you can use 'data' as a dictionary
# Example: Print the first Classroom's FacilityID
print(data['Classrooms']['Classroom'][0]['FacilityID'])

classes = data['Classrooms']['Classroom']

for i in range(len(classes)):
    #print(classes[i]['FacilityID'])
    print(json_maker('classrooms', room=classes[i]['FacilityID'])) 