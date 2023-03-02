import time

from ultrasonico import UltrasonicSensor
from temperatura import temperatura
from led import Led
import threading

class main:
    def main(self):
        opcion = ""
        while opcion != "5":
            opcion = self.menu()
            if opcion == "1":
                self.ultrasonico()
            elif opcion == "2":
                self.temperatura()
            elif opcion == "3":
                self.led()
            elif opcion == "4":
                self.juntos()
            elif opcion == "5":
                # Salir
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")


    def detectar_enter(self):
        self.enter_pressed = False
        while True:
            entrada = input()
            if not entrada:
                self.enter_pressed = True
                break



    def ultrasonico(self):
        sensor = UltrasonicSensor(trigger_pin=23, echo_pin=24)
        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        while True:
            distancia = sensor.medirDistancia()
            print("Distancia: {} cm".format(distancia))
            if self.enter_pressed:
                print("Enter presionado, deteniendo lectura de sensores")
                sensor.liberarPin()
                return self.main()

    def temperatura(self):
        sensor = temperatura(5)
        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        while True:
            hum, temp = sensor.lectura()
            if hum is not None and temp is not None:
                print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temp, hum))
            if self.enter_pressed:
                print("Enter presionado, deteniendo lectura de sensores")
                return self.main()

    def led(self):
        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        led1 = Led(17)
        led1.encender()

    def juntos(self):
        sensor = temperatura(5)
        sensorUlt = UltrasonicSensor(trigger_pin=23, echo_pin=24)
        led1 = Led(17)

        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        while True:
            hum, temp = sensor.lectura()
            distancia = sensorUlt.medirDistancia()
            print("Distancia: {} cm".format(distancia))
            led1.encender()
            self.bandera=1
            if self.bandera==1:
                led1.apagar()
                self.bandera=0
            if hum is not None and temp is not None:
                print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temp, hum))
            print("Distancia: {} cm".format(distancia))


            if self.enter_pressed:
                print("Enter presionado, deteniendo lectura de sensores")
                return self.main()

    def pruebas(self):
        while True:
            print("Probando ... ")
            time.sleep(1)
            if self.enter_pressed:
                print("Enter presionado, deteniendo lectura de sensores")
                return self.main()



    def menu(self):
        print("------------Menu------------")
        print("1. Ultrasonico")
        print("2. Temperatura")
        print("3. Led")
        print("4. Sensores")
        print("5. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion


if __name__ == "__main__":
    main().main()



