from token_generator import token_generator
import json
from test import json_maker
import datetime

token_generator('classrooms')

def get_meeting_times(room, start_date, end_date):
    """
    Fetch meeting times for a given room and date range.
    """
    times = json_maker('classrooms', room=room, start_date=start_date, end_date=end_date)
    return times['Classrooms']['Classroom']

def main():
    with open('classrooms.json', 'r') as file:
        data = json.load(file)

    classes = data['Classrooms']['Classroom']
    today = datetime.date.today().strftime('%B %d, %Y')

    for classroom in classes:
        facility_id = classroom['FacilityID']
        print(f"Meeting times for {facility_id} on {today}:")
        
        times = get_meeting_times(facility_id, today, today)
        
        for meeting in times:
            start_time = meeting['MtgStartTime']
            end_time = meeting['MtgEndTime']
            print(f"Start: {start_time}, End: {end_time}")
        print("-" * 40)  

if __name__ == "__main__":
    main()