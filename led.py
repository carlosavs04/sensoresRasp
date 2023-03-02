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
            user_input = input("Ingrese un valor (0, 1 o 2), o presione Enter para salir: ")
            if user_input == "1":
                print("Encendiendo LED")
                GPIO.output(self.led_pin, GPIO.HIGH)
            elif user_input == "2":
                print("Parpadeando LED")
                for i in range(3):
                    GPIO.output(self.led_pin, GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(self.led_pin, GPIO.LOW)
                    time.sleep(0.5)
            elif user_input == "0":
                print("Apagando LED")
                GPIO.output(self.led_pin, GPIO.LOW)
            elif user_input == "3":
                break
            elif not user_input:  # si se presiona enter (string vacío), detener el loop
                break
            else:
                print("Valor inválido")
        GPIO.output(self.led_pin, GPIO.LOW)
        self.thread = None

    def detener(self):
        self.stop_event.set()
        self.thread.join()
        GPIO.cleanup()


