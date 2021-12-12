Days = ['None', 'Monday', 'Tuesday', 'Wednesday', 'Thurday', 'Friday', 'Saturday', 'Sunday']

def parse_to_byte(value, unit_bits, ten_bits):
    ten_mask = int('0' + '1' * ten_bits, 2)
    tens_binary = (int(value / 10) & ten_mask) << unit_bits
    unit_mask = int('0' + '1' * unit_bits, 2)
    units_binary = value % 10 & unit_mask
    return tens_binary + units_binary

def parse_from_byte(byte, unit_bits, ten_bits):
    ten_mask = int('0' + '1' * ten_bits, 2)
    tens = (byte >> unit_bits) & ten_mask
    unit_mask = int('0' + '1' * unit_bits, 2)
    units = byte & unit_mask
    return tens * 10 + units

class DS3231_I2C:
    ADDRESS = 0x68
    REGISTER = 0x00

    def __init__(self, i2c, addr=0x68):
        self.i2c = i2c
        self.addr = addr
        self.reg = 0x00

    def set_time_bytes(self, time_list):
        self.i2c.writeto_mem(int(self.addr), int(self.reg), time_list)

    def read_time_bytes(self):
        return self.i2c.readfrom_mem(int(self.addr), int(self.reg), 7)

    def set_time(self, wkday, year, month, day, hour, minute, second):
        self.set_time_bytes([
            parse_to_byte(second, 4, 3),
            parse_to_byte(minute, 4, 3),
            parse_to_byte(hour, 4, 2),
            parse_to_byte(Days.index(wkday), 3, 0),
            parse_to_byte(day, 4, 2),
            parse_to_byte(month, 4, 1),
            parse_to_byte(year, 4, 4),
        ])

    def read_time(self):
        date_time_bytes = self.read_time_bytes()
        return [
            Days[parse_from_byte(date_time_bytes[3], 3, 0)],
            parse_from_byte(date_time_bytes[6], 4, 4),
            parse_from_byte(date_time_bytes[5], 4, 1),
            parse_from_byte(date_time_bytes[4], 4, 2),
            parse_from_byte(date_time_bytes[2], 4, 2),
            parse_from_byte(date_time_bytes[1], 4, 3),
            parse_from_byte(date_time_bytes[0], 4, 3),
        ]
