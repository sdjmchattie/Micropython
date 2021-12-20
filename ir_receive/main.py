from machine import Pin
from ir_rx.nec import NEC_8  # NEC remote, 8 bit addresses.

def ir_received(data, addr, ctrl):
    if data >= 0:  # Not a repeat of the previous code.
        # For now, just print what was received,
        # but can trigger whatever action we want from here.
        print('Data {:02x} Addr {:04x}'.format(data, addr))

# Data leg from IR receiver on GPIO pin 22 (physical pin 29).
ir = NEC_8(Pin(22, Pin.IN), ir_received)

while True:
    # Do nothing while we're waiting for IR signals.
    pass
