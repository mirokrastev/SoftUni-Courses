n = int(input())
snowball_value = 0
snowball_value_garbage = 0
snowball_snow_collector = 0
snowball_time_collector = 0
snowball_quality_collector = 0

for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value_garbage = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value_garbage > snowball_value:
        snowball_value = snowball_value_garbage
        snowball_snow_collector = snowball_snow
        snowball_time_collector = snowball_time
        snowball_quality_collector = snowball_quality
print(f'{snowball_snow_collector} : {snowball_time_collector} = {snowball_value:.0f} ({snowball_quality_collector})')