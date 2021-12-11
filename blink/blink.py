from machine import Pin
import time

pin = Pin(25, Pin.OUT)

def main():
    while True:
        pin.toggle()
        time.sleep_ms(500)
