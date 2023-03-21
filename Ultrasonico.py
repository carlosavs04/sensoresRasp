import RPi.GPIO as GPIO
import time

class Ultrasonico:
    def __init__(self, trigger, echo):
        self.trigger = trigger
        self.echo = echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trigger, GPIO.LOW)
        time.sleep(0.2) 
        GPIO.setwarnings(False)

    def medirDistancia(self):
        GPIO.setwarnings(False)
        
        GPIO.output(self.trigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(self.trigger, GPIO.LOW)
        while GPIO.input(self.echo) == GPIO.LOW:
            pulse_start = time.time()
        while GPIO.input(self.echo) == GPIO.HIGH:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance
    
    def cleanup(self):
        GPIO.cleanup()

if __name__ == "__main__":
    sensor = Ultrasonico(23, 24)
    distancia = sensor.medirDistancia()
    print("Distancia: {} cm".format(distancia))
    sensor.cleanup()   