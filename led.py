
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)

    def toggle(self):
        ban=0

        if self.led.is_active:
            self.led.on()
            ban = 1
        else:
            self.led.off()
            ban = 0
        return ban
