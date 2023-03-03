
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)
        self.estado = self.led.value
    def toggle(self):
        ban=0
        if self.estado == 1:
            self.led.on()
            ban = 1
        else:
            self.led.off()
            ban = 0
        return ban
if __name__ == "__main__":
    led1=Led(17)
    print(led1.toggle())