from flask import Flask, jsonify
import json
import requests
from find_classrooms import is_room_available_by_schedule, get_intervals

app = Flask(__name__)

def available(id, rooms):
    return is_room_available_by_schedule(rooms, id)

intervals = get_intervals()

def get_available_rooms_hashmap():
    rooms = {}
    for room in intervals.keys():
        rooms[room] = available(room, intervals)
    return rooms

@app.route('/check_availability/<room_id>', methods=['GET'])
def check_availabilty(id, rooms):
    availability = available(id, rooms)
    return jsonify({"room_id": id, "available": availability})

@app.route('/list_available_rooms', methods=['GET'])
def list_available_rooms():
    available_rooms = get_available_rooms_hashmap()
    return jsonify(available_rooms)

if __name__ == '__main__':
    app.run(debug=True)
