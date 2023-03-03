import time
from gpiozero import LED


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(self.pin)
    def toggle(self):
        if self.led.is_active:
            self.led.off()
            return 0

        else:
            self.led.on()
            return 1



if __name__ == "__main__":
    led1=Led(17)
    while True:
        led1.led.on()
