
import gpiozero


class Led:
    def __init__(self, pin):
        self.pin = pin
        self.led = gpiozero.LED(self.pin)
        self.estado = self.led.value
    def toggle(self, ban):
        if self.estado == 1:
            self.led.on()
        else:
            self.led.off()
        return ban
if __name__ == "__main__":
    led1=Led(17)
    estado = 1
    while True:
        print(led1.toggle(estado))
        if estado == 1:
            estado=0
        else:
            estado = 1