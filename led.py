import time
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)
    def toggle(self):
        if self.led.active_high:
            self.led.on()
            return 1


        else:
            self.led.off()
            return 0


if __name__ == "__main__":
    led1=Led(17)
    while True:
        led1.led.on()
