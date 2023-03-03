from gpiozero import LED


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)

    def toggle(self):
        self.led.toggle()

