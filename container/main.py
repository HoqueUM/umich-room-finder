from find_classrooms import get_intervals, find_available_times, is_room_available_by_schedule



times = get_intervals()
print(times)
available = find_available_times(times)
print(is_room_available_by_schedule(times, '400NI1180'))