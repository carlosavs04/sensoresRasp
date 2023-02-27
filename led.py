import RPi.GPIO as GPIO
import time
import keyboard
class led:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.led_pin = pin
        GPIO.setup(self.led_pin, GPIO.OUT)
        GPIO.output(self.led_pin, GPIO.LOW)

    def encender(self):
        try:
            teclas = keyboard.record(until='enter')
            if teclas=="1":
                print("Encendiendo LED")
                GPIO.output(self.led_pin, GPIO.HIGH)
            elif teclas == "2":
                print("Parpadeando LED")
                for i in range(3):
                    GPIO.output(self.led_pin, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(self.led_pin, GPIO.LOW)
                    time.sleep(0.5)
            elif teclas=="3":
                return 1
            elif teclas == "0":
                print("Apagando LED")
                GPIO.output(self.led_pin, GPIO.LOW)
            else:
                print("Valor inválido")
        except KeyboardInterrupt:
            GPIO.cleanup()

