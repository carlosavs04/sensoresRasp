import RPi.GPIO as GPIO
import time

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def medirDistancia(self):
        GPIO.output(self.trigger_pin, GPIO.LOW)
        time.sleep(0.2)
        GPIO.output(self.trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, GPIO.LOW)
        while GPIO.input(self.echo_pin) == GPIO.LOW:
            start_time = time.time()
        while GPIO.input(self.echo_pin) == GPIO.HIGH:
            end_time = time.time()
        pulse_duration = end_time - start_time
        distance = pulse_duration * 17150
        return round(distance, 2)

    def liberarPin(self):
        GPIO.cleanup()


if __name__ == "__main__":
    sensor = UltrasonicSensor(trigger_pin=23, echo_pin=24)
    distancia = sensor.measure_distance()
    print("Distancia: {} cm".format(distancia))
    sensor.cleanup()
