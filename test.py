# sending requests to umich api to get room schedule
# authorization can be obtained from the postman request

import requests
import json
from dotenv import load_dotenv
from token_generator import token_generator
import os

def json_maker(scope, room=None, start_date=None, end_date=None):
    token_generator(scope)
    load_dotenv()
    classrooms = os.getenv('ACCESS_TOKEN')
    RoomID = room
    class_requestUrl = f"https://gw.api.it.umich.edu/um/aa/ClassroomList/v2/Classrooms"
    requestHeaders = {
        "Authorization": f"Bearer {classrooms}",
        "Accept": "application/json"
    }

    response = requests.get(class_requestUrl, headers=requestHeaders)
    j = json.loads(response.text)
    with open("classrooms.json", "w") as f:
        json.dump(j, f, indent=4)

json_maker('classrooms')
