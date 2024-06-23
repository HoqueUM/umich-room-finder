from token_generator import token_generator
import requests
import json
from test import json_maker
import datetime

token_generator('classrooms')

with open('classrooms.json', 'r') as file:
    data = json.load(file)

classes = data['Classrooms']['Classroom']

today = datetime.date.today().strftime('%B %d, %Y')

for i in range(len(classes)):
    #print(classes[i]['FacilityID'])
    times = json_maker('classrooms', room=classes[i]['FacilityID'], start_date=today, end_date=today)
    print(times)

    
    