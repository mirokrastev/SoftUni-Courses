record_in_sec = float(input())
distance_meters = float(input())
onemeter_swim = float(input())

distance_travelled = distance_meters * onemeter_swim
added_time = (distance_meters // 15) * 12.5
total_time = distance_travelled + added_time
missing_seconds = total_time - record_in_sec

if total_time < record_in_sec:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {missing_seconds:.2f} seconds slower.')