from ultrasonico import UltrasonicSensor
from temperatura import temperatura
class main:
    def main(self):
        print("----Bienvenido----")
        # sensor=UltrasonicSensor(trigger_pin=23, echo_pin=24)
        # while True:
        #     distancia = sensor.measure_distance()
        #     print("Distancia: {} cm".format(distancia))
        #     if distancia >= 1:
        #         break
        # sensor.cleanup()
        sensor=temperatura(5)
        while True:
            hum, temp = sensor.lectura()
            if hum is not None and temp is not None:
                print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temp, hum))
            else:
                print('Error al leer datos del sensor')


if __name__ == "__main__":
    main().main()



