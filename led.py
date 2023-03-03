import time
from gpiozero import LED


class Led:
    estado_actual=False
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(self.pin)

    def toggle(self):
        if self.estado_actual:
            self.led.off()
            self.estado_actual = False
            return 0

        else:
            self.led.on()
            self.estado_actual = True
            return 1

    def estado(self):
        if self.led.is_lit:
            return 1
        else:
            return 0


if __name__ == "__main__":
    led1=Led(17)
    print(led1.estado())
