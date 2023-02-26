import Adafruit_DHT

class temperatura:
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin

    def lectura(self):
        hum, temp = Adafruit_DHT.read(self.sensor, self.pin)
        return  hum, temp

