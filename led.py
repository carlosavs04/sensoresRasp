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
        print("Encendiendo LED")
        GPIO.output(self.led_pin, GPIO.HIGH)

    def apagar(self):
        print("Apagando LED")
        GPIO.output(self.led_pin, GPIO.LOW)
    def led_loop(self):
        while not self.stop_event.is_set():

            time.sleep(5)


        GPIO.output(self.led_pin, GPIO.LOW)
        self.thread = None

    def detener(self):
        self.stop_event.set()
        self.thread.join()
        GPIO.cleanup()


