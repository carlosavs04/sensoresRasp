import time
from gpiozero import LED


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = LED(self.pin)
        self.estado_actual = False  # establecer el estado inicial como apagado

    def toggle(self):
        if self.estado_actual:
            self.led.off()
            self.estado_actual = False
            return 0
        else:
            self.led.on()
            self.estado_actual = True
            return 1




if __name__ == "__main__":
    led1=Led(17)
    while True:
        led1.led.on()
