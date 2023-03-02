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
        print("Iniciando LED")
        self.stop_event.clear()
        self.thread = threading.Thread(target=self.led_loop)
        self.thread.start()

    def led_loop(self):
        while not self.stop_event.is_set():
            print("Encendiendo LED")
            GPIO.output(self.led_pin, GPIO.HIGH)
            time.sleep(5)
            print("Apagando LED")
            GPIO.output(self.led_pin, GPIO.LOW)

        GPIO.output(self.led_pin, GPIO.LOW)
        self.thread = None

    def detener(self):
        self.stop_event.set()
        self.thread.join()
        GPIO.cleanup()


