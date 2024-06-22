# sending requests to umich api to get room schedule
# authorization can be obtained from the postman request

import requests
import json
from dotenv import load_dotenv
from token_generator import token_generator
import os
import datetime

def json_maker(scope, room=None, start_date=None, end_date=None):
    token_generator(scope)
    load_dotenv()
    classrooms = os.getenv('ACCESS_TOKEN')
    RoomID = room
    class_requestUrl = f"https://gw.api.it.umich.edu/um/aa/ClassroomList/v2/Classrooms/{room}/Meetings"
    requestHeaders = {
        "Authorization": f"Bearer {classrooms}",
        "Accept": "application/json"
    }

    response = requests.get(class_requestUrl, headers=requestHeaders)
    return response.json()

#json_maker('classrooms')
