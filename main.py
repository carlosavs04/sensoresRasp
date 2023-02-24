from ultrasonico import UltrasonicSensor

class main:
    def main(self):
        print("Si ejectura")
        sensor=UltrasonicSensor(trigger_pin=23, echo_pin=24)
        while True:
            distancia = sensor.measure_distance()
            print("Distancia: {} cm".format(distancia))
            if distancia >= 1:
                break
        sensor.cleanup()

if __name__ == "__main__":
    main().main()