import time
from gpiozero import LED


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(self.pin)

    def toggle(self):
        if self.led.is_lit:
            self.led.off()
            return 0

        else:
            self.led.on()
            return 1

    def estado(self):
        if self.led.is_lit:
            return 1
        else:
            return 0


if __name__ == "__main__":
    led1=Led(17)
    print(led1.toggle())
    input()
    print(led1.toggle())
    input()
    print(led1.toggle())
    input()

