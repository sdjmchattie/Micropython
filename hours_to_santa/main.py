from hours_to_santa.rtc import RTC
from math import fabs

import time

rtc = RTC(sda_pin = 4, scl_pin = 5)

def hours_between(a, b):
    time_a = time.mktime((2000 + a['year'], a['month'], a['day'], a['hour'], a['minute'], a['second'], 0, 0))
    time_b = time.mktime((2000 + b['year'], b['month'], b['day'], b['hour'], b['minute'], b['second'], 0, 0))
    return fabs(time_a - time_b) / 3600

def main():
    while (True):
        current_time = rtc.get_date_time()
        goal_time = { 'year': 21, 'month': 12, 'day': 25, 'hour': 0, 'minute': 0, 'second': 0 }
        print(hours_between(current_time, goal_time))
        time.sleep_ms(1000)

main()