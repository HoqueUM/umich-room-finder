from token_generator import token_generator
import json
from json_maker import json_maker
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
    for classroom in classes:
        facility_id = classroom['FacilityID']
        times = get_meeting_times(facility_id, march20, march20)
        time_intervals = []
        for meeting in times:
            start_time = meeting['MtgStartTime']
            end_time = meeting['MtgEndTime']
            time_intervals.append((start_time, end_time))
        schedule_dict[facility_id] = time_intervals
    return schedule_dict

def to_datetime(time_str):
    return datetime.datetime.strptime(time_str, "%I:%M %p")

def find_available_times(schedule):
    
    day_start = to_datetime("12:00 AM")
    day_end = to_datetime("11:59 PM")
    
    available_times = {}
    
    for room, intervals in schedule.items():
        intervals = sorted(intervals, key=lambda x: to_datetime(x[0]))
        
        room_available_times = []
        previous_end = day_start
        
        for start, end in intervals:
            start_time = to_datetime(start)
            end_time = to_datetime(end)
            
            if previous_end < start_time:
                room_available_times.append((previous_end.strftime("%I:%M %p"), start_time.strftime("%I:%M %p")))
            previous_end = max(previous_end, end_time)
        
        if previous_end < day_end:
            room_available_times.append((previous_end.strftime("%I:%M %p"), day_end.strftime("%I:%M %p")))
        
        available_times[room] = room_available_times
    
    return available_times

def is_room_available_by_schedule(schedule, room_name):
    now = datetime.datetime.now()
    room_intervals = schedule.get(room_name, [])
    
    for start, end in room_intervals:
        start_time = to_datetime(start)
        end_time = to_datetime(end)
        if start_time.time() <= now.time() <= end_time.time():
            return False
    
    return True

def is_room_available_by_not_schedule(schedule, room_name):
    now = datetime.datetime.now()
    room_intervals = schedule.get(room_name, [])
    
    for start, end in room_intervals:
        start_time = to_datetime(start)
        end_time = to_datetime(end)
        if start_time.time() <= now.time() <= end_time.time():
            return True
    
    return False