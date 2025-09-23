import time 
try:
    choose_hour_to_alarm = int(input('Choose a hour (1-12) to alarm '))
    choose_mins_to_alarm = int(input('Choose a mins (01-59) to alarm '))
except ValueError:
    print('Sorry a number not a letter')

choose_meridiem_time = input('Choose to alarm AM or PM ')

# to present as a output in our local time
hour = time.strftime('%I')
minutes = time.strftime('%M')
locale = time.strftime('%p')

int_hour = int(hour)
int_mins = int(minutes)

def alarm_time(hours, mins, meridiem):
    while True:
        time.sleep(5)
        hour = time.strftime('%I')
        minutes = time.strftime('%M')
        locale = time.strftime('%p')

        int_hour = int(hour)
        int_mins = int(minutes)
        
        
        if hours == int_hour and mins == int_mins and meridiem == locale:
            print(f'alarm time, {hour}:{minutes} {locale}')
            return 'Alarm Clock!!!'
            
alarm = alarm_time(choose_hour_to_alarm, choose_mins_to_alarm, choose_meridiem_time)
print(alarm)

