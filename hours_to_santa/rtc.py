from hours_to_santa.lib.ds3231_i2c import DS3231_I2C
from machine import I2C, Pin
from math import floor

Days = ['None', 'Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']


def convert_base(src_base, dest_base, num):
    a = floor(num / src_base)
    b = num % src_base
    return a * dest_base + b

class RTC:
    def __init__(self, sda_pin, scl_pin):
        rtc_i2c = I2C(0, sda = Pin(sda_pin), scl = Pin(scl_pin))
        self.rtc = DS3231_I2C(rtc_i2c)

    def set_date_time(self, year, month, day, hour, minute, second, wkday):
        date_time_bytes = bytes([
            convert_base(10, 16, second),
            convert_base(10, 16, minute),
            convert_base(10, 16, hour),
            convert_base(10, 16, Days.index(wkday)),
            convert_base(10, 16, day),
            convert_base(10, 16, month),
            convert_base(10, 16, year),
        ])
        self.rtc.set_time(date_time_bytes)

    def get_date_time(self):
        date_time_bytes = self.rtc.read_time()
        return {
            'year': convert_base(16, 10, date_time_bytes[6]),
            'month': convert_base(16, 10, date_time_bytes[5]),
            'day': convert_base(16, 10, date_time_bytes[4]),
            'week_day': Days[convert_base(16, 10, date_time_bytes[3])],
            'hour': convert_base(16, 10, date_time_bytes[2]),
            'minute': convert_base(16, 10, date_time_bytes[1]),
            'second': convert_base(16, 10, date_time_bytes[0]),
        }
