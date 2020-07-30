hour,time = input().split()

hour = int(hour)
time = int(time)

if time >= 45:
    minus_time_1 = time - 45
    print(hour, minus_time_1)
elif time < 45:
    if hour == 0:
        minus_hour_1 = 23
        minus_time_2 = time + 15
        print(minus_hour_1, minus_time_2)
    else:
        minus_hour_2 = hour - 1
        minus_time_3 = time + 15
        print(minus_hour_2, minus_time_3)
