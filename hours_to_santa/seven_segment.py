from machine import Pin, Timer

SEGMENTS = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
]

class SevenSegment:
    def __init__(self, a, b, c, d, e, f, g, dp, digit_1, digit_2, digit_3, digit_4):
        self.digits = []
        self.dp_pos = -1
        self._cur_digit = 3
        self.segment_pins = [
            Pin(a, Pin.OUT),
            Pin(b, Pin.OUT),
            Pin(c, Pin.OUT),
            Pin(d, Pin.OUT),
            Pin(e, Pin.OUT),
            Pin(f, Pin.OUT),
            Pin(g, Pin.OUT),
        ]
        self.dp_pin = Pin(dp, Pin.OUT)
        self.digit_pins = [
            Pin(digit_1, Pin.OUT),
            Pin(digit_2, Pin.OUT),
            Pin(digit_3, Pin.OUT),
            Pin(digit_4, Pin.OUT),
        ]
        self._timer = Timer(period=4, mode=Timer.PERIODIC, callback=self.update_display)
    
    def dp_value(self):
        return 1 if self.dp_pos == self._cur_digit else 0
    
    def update_display(self, timer):
        prev_digit = self._cur_digit
        self._cur_digit = (self._cur_digit + 1) % 4
        
        try:
            digit = self.digits[self._cur_digit]
        except:
            digit = 0

        # Set segment values
        self.digit_pins[prev_digit].value(1)
        for i in range(7):
            self.segment_pins[i].value(SEGMENTS[digit][i])
        self.dp_pin.value(self.dp_value())
        self.digit_pins[self._cur_digit].value(0)