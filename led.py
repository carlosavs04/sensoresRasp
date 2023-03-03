import time
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)
        self.estado = self.led.value
    def toggle(self):
        time.sleep(2)
        if self.estado == 1:
            self.led.on()
        else:
            self.led.off()


    def check(self):
        print(self.led.active_high)

if __name__ == "__main__":
    led1=Led(17)
    while True:
        led1.led.on()
        led1.check()
        input()