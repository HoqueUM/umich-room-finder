from token_generator import token_generator
import json
from test import json_maker
import datetime

def get_meeting_times(room, start_date, end_date):
    """
    Fetch meeting times for a given room and date range.
    """
    token_generator('classrooms')
    times = json_maker('classrooms', room=room, start_date=start_date, end_date=end_date)
    return times['Classrooms']['Classroom']

def get_intervals():
    with open('classrooms.json', 'r') as file:
        data = json.load(file)
    classes = data['Classrooms']['Classroom']
    today = datetime.date.today().strftime('%B %d, %Y')
    march20 = '03-20-2024'
    schedule_dict = {}
    limiter = 0
    for classroom in classes:
        facility_id = classroom['FacilityID']
        times = get_meeting_times(facility_id, march20, march20)
        time_intervals = []
        for meeting in times:
            start_time = meeting['MtgStartTime']
            end_time = meeting['MtgEndTime']
            time_intervals.append((start_time, end_time))
        schedule_dict[facility_id] = time_intervals
        limiter += 1
        if limiter == 5:
            break
    return schedule_dict

def is_available(start_time, end_time):
    start_time = datetime.strptime(start_time, "%H:%M")
    end_time = datetime.strptime(end_time, "%H:%M")
    
    now = datetime.now().time()
    
    if start_time.time() <= now <= end_time.time():
        return True
    return False

def get_available_times():
    times = get_intervals()
    available_times = {}
    for room, intervals in times.items():
        available_times[room] = []
        for interval in intervals:
            start_time, end_time = interval
            if is_available(start_time, end_time):
                available_times[room].append((start_time, end_time))
    return available_times