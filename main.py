from ultrasonico import UltrasonicSensor

class main:
    def main(self):
        sensor=UltrasonicSensor(trigger_pin=23, echo_pin=24)
        while True:
            distancia = sensor.measure_distance()
            print("Distancia: {} cm".format(distancia))
            if distancia >= 1:
                break
        sensor.cleanup()