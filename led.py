import time
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)
    def toggle(self):
        time.sleep(2)
        if self.led.active_high:
            self.led.off()
            return 0
        else:
            self.led.on()
            return 1



if __name__ == "__main__":
    led1=Led(17)
    while True:
        led1.led.on()
