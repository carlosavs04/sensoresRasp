
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)

    def toggle(self):
        ban=0
        self.led.toggle()
        if self.led.is_active:
            ban = 1
        else:
            ban = 0
        return ban
