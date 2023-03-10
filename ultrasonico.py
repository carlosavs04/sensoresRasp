import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setwarnings(False)

    def medirDistancia(self):
        GPIO.setwarnings(False)
        num_intentos = 3
        intento_actual = 0

        while intento_actual < num_intentos:
            intento_actual += 1

            GPIO.output(self.trigger_pin, GPIO.LOW)
            time.sleep(0.2)
            GPIO.output(self.trigger_pin, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.trigger_pin, GPIO.LOW)

            start_time = 0
            end_time = 0

            while GPIO.input(self.echo_pin) == GPIO.LOW:
                start_time = time.time()
            while GPIO.input(self.echo_pin) == GPIO.HIGH:
                end_time = time.time()

            if start_time == 0 or end_time == 0:
                continue

            pulse_duration = end_time - start_time
            distance = pulse_duration * 17150

            if distance > 0:
                return round(distance, 2)

        return "fallo"

    def liberarPin(self):
        GPIO.cleanup()


if __name__ == "__main__":
    sensor = UltrasonicSensor(trigger_pin=23, echo_pin=24)
    distancia = sensor.measure_distance()
    print("Distancia: {} cm".format(distancia))
    sensor.cleanup()
