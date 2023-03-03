import RPi.GPIO as GPIO
import threading

class Led:
    def __init__(self, pin):
        self.pin = pin
        self.estado = False  # Agregamos un atributo para rastrear el estado del LED
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def loop(self):
        self.estado = not self.estado  # Cambiamos el estado del LED en cada llamada al método
        GPIO.output(self.pin, self.estado)
        return self.estado  # Devolvemos el estado actual del LED
