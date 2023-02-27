from ultrasonico import UltrasonicSensor
from temperatura import temperatura
from led import led
import keyboard
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
        keyboard.wait("enter")  # espera hasta que se presione Enter
        self.enter_pressed = True
    def ultrasonico(self):
        sensor = UltrasonicSensor(trigger_pin=23, echo_pin=24)
        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        while True:
            distancia = sensor.medirDistancia()
            print("Distancia: {} cm".format(distancia))
            opcio=input()

            if opcio=="s":  # si se ha detectado la pulsación de Enter, romper el ciclo
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
            else:
                print('Leyendo...')
            opcio = input()

            if opcio == "s":  # si se ha detectado la pulsación de Enter, romper el ciclo
                return self.main()

    def led(self):
        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        led1= led(17)
        while True:
            if led1.encender() == 1:  # si se ha detectado la pulsación de Enter, romper el ciclo
                return self.main()

    def juntos(self):
        sensor = temperatura(5)
        sensorUlt = UltrasonicSensor(trigger_pin=23, echo_pin=24)

        enter_thread = threading.Thread(target=self.detectar_enter)
        enter_thread.start()
        while True:
            hum, temp = sensor.lectura()
            distancia = sensorUlt.medirDistancia()

            if hum is not None and temp is not None:
                print('Temperatura={0:0.1f}*C  Humedad={1:0.1f}%'.format(temp, hum))
            print("Distancia: {} cm".format(distancia))
            opcio = input()

            if opcio == "s":  # si se ha detectado la pulsación de Enter, romper el ciclo
                sensorUlt.liberarPin()
                return self.main()



    def menu(self):
        print("------------Menu------------")
        print("1. Ultrasonico")
        print("2. Temperatura")
        print("3. Led")
        print("4. Juntos")
        print("5. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion


if __name__ == "__main__":
    main().main()



