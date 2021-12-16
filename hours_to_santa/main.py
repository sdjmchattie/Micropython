from hours_to_santa.rtc.ds3231_i2c import DS3231_I2C as RTC
from hours_to_santa.seven_segment import SevenSegment
from machine import I2C, Pin, Timer
from math import fabs
from time import mktime


def make_time(t):
    return mktime((2000 + t[0], t[1], t[2], t[3], t[4], t[5], 0, 0))

def update_time(timer):
    global current_time
    global seven_segment
    current_time += 1
    displayed_hours = str(fabs(current_time - goal_time) / 3600)
    seven_segment.dp_pos = displayed_hours.find('.') - 1
    digits = [int(x) for x in '%s0000' % displayed_hours.replace('.', '')[0:5]]
    if digits[4] >= 5:
        digits[3] += 1
    seven_segment.digits = digits
    print(displayed_hours)
    


rtc = RTC(I2C(0, sda = Pin(4), scl = Pin(5)))
seven_segment = SevenSegment(20, 16, 13, 11, 10, 19, 14, 12, 21, 18, 17, 15)
current_time = make_time(rtc.read_time()[1:])
goal_time = make_time([21, 12, 25, 0, 0, 0])


def run():
    Timer(freq=1, mode=Timer.PERIODIC, callback=update_time)

if __name__ == "__main__":
    run()
