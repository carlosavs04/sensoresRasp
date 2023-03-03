import RPi.GPIO as GPIO
import time
import keyboard
import threading

class Led:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.led_pin = pin
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, GPIO.LOW)
        self.stop_event = threading.Event()

    def encender(self):
        GPIO.output(self.led_pin, GPIO.HIGH)
        return 1

    def apagar(self):
        GPIO.output(self.led_pin, GPIO.LOW)
        return 0

    def loop(self):
        estado = GPIO.input(self.led_pin)
        ban = 0
        if estado == GPIO.LOW:
            ban= self.encender()
        else:
            ban = self.apagar()
        return ban

