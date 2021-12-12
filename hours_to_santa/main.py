from hours_to_santa.rtc.ds3231_i2c import DS3231_I2C as RTC
from machine import I2C, Pin
from math import fabs

import time

rtc = RTC(I2C(0, sda = Pin(4), scl = Pin(5)))

def hours_between(a, b):
    time_a = time.mktime((2000 + a[0], a[1], a[2], a[3], a[4], a[5], 0, 0))
    time_b = time.mktime((2000 + b[0], b[1], b[2], b[3], b[4], b[5], 0, 0))
    return fabs(time_a - time_b) / 3600

def main():
    while (True):
        current_time = rtc.read_time()[1:]
        goal_time = [21, 12, 25, 0, 0, 0]
        print(hours_between(current_time, goal_time))
        time.sleep_ms(1000)

main()
