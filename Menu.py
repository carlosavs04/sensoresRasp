from Sensor import Sensor
from Led import Led
from Lectura import Lectura
from MongoDB import MongoDB
import threading
import time
import json
import keyboard

class Menu:
    def __init__(self):
        self.lectura = Lectura()
        self.bandera = 0
        self.led = Led(17)
        self.mongo = MongoDB()
        self.wait = 120
        self.timer_count = 0
        self.repeat = 2
        self.enter_pressed = False
        self.collecion = "Sensores"

    def contador(self, tiempo):
        for i in range(tiempo, -1, -1):
            time.sleep(1)
        return True
    
    def main(self):
        opcion = ""
        while opcion != "4":
            opcion = self.menu()
            if opcion == "1":
                self.medirTodos()
            
            if opcion == "2":
                self.encenderLed()

            if opcion == "3":
                self.apagarLed()

            elif opcion == "4":
                print("Saliendo...")

            else:
                print("Opción inválida.")

    def menu(self):
        if self.repeat == 2:
            conexion = self.mongo.createConnection()

            if conexion is not False:
                self.bandera2 = 1
                self.repeat = 1

            else:
                self.bandera2 = 2
                self.repeat = 1

        print("------------Menu------------")
        print("1. Medir todos los sensores")
        print("2. Encender led")
        print("3. Apagar led")
        print("4. Salir")

        opcion = input("Introduce una opción: ")
        return opcion

    def medirTodos(self):
        ult = Sensor("ult", [23, 24], "Sensor ultrasonico", "Sensor para medir distancia")
        temp = Sensor("tmp", [4], "Sensor DHT11", "Sensor para medir temperatura y humedad")
        sensores=[temp, ult]
        z=0
        if self.bandera2 == 1:  # si esta en conexion
            lista = self.lectura.mostrar()
            if len(lista) >= 1:  # si la lista de sensores tiene objetos, debe ingresarlos a la bd antes de los otros
                for x in lista:
                    if self.mongo.find_one(self.collecion, x):
                        pass
                    else:
                        self.mongo.insert_one(self.collecion, x)
                self.lectura.clearFile("Sensores.json")
            self.hiloBorrarPTiempo()
        while True:
            for sens in sensores:
                z=z+1
                # print(sens.lectura())
                data=json.loads(sens.lectura())
                if len(data)>=1:
                    for i in data:
                        print("|{:<3} | {:<20} | {:<25} | {:<7}{:<4} | {:<10} | ".format(z, i["nombre"],i["descripcion"],i["valores"],i["dato"],i["fecha"]))
                        self.lectura.agregar(i)
                        if self.bandera2==1:
                            self.guardar(i)

    def encenderLed(self):
        self.led.encender()

    def apagarLed(self):
        self.led.apagar()

    def guardar(self,sensor):

        if self.mongo.insert_one(self.collecion,sensor) is False:  # si no se inserto, debe cambiar la bandera
            self.bandera2 = 2
            print("Se perdio la conexion, guardando solo localmente")
            ultimoSensor = sensor  # guarda la lecutra donde sucede la desconexion
            self.lectura.clearFile("Sensores.json")  # borra datos para no repetirlos
            self.lectura.agregar(ultimoSensor)
            self.sensoresLectura()  # debe regresar al metodo para empezar a guardar solo local

    def hiloBorrarPTiempo(self):
        timer = threading.Timer(self.wait, self.hiloBorrarPTiempo)
        timer.start()

        if self.bandera2 == 1:  # si esta en conexion
            self.timer_count += 1  # incrementa el contador de tiempo
            if self.timer_count >= self.wait / 60:  # verifica si han pasado 15 minutos
                self.lectura.clearFile("Sensores.json")
                print("Se borro historial local")
                print("---------------------------------------------------------------")
                self.timer_count = 0  # resetea el contador de tiempo
        else:
            print("Se reinicio el contador")
            self.timer_count = 0

if __name__ == "__main__":
    menu = Menu()
    menu.main()
