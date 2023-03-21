from Sensor import Sensor
from Led import Led
from Lectura import Lectura
from MongoDB import MongoDB
from prettytable import PrettyTable
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
        tabla = PrettyTable()
        tabla.field_names = ["Nombre", "Descripción", "Valores", "Tipo de dato", "Fecha"]

        sensores = [temp, ult]
        if self.bandera2 == 1:
            listaSensores = self.lectura.mostrar()
            if len(listaSensores) >= 1: 
                for i in listaSensores:
                    if self.mongo.find_one(self.collecion, i):
                        pass
                    else:
                        self.mongo.insert_one(self.collecion, i)

                self.lectura.clearFile("Sensores.json")
            self.borrarHilo()
 
        while True:
            for sens in sensores:
                data=json.loads(sens.lectura())
                if len(data)>=1:
                    for i in data:
                        tabla.add_row([i["nombre"], i["descripcion"], i["valores"], i["dato"], i["fecha"]])
                        self.lectura.agregar(i)
                        if self.bandera2 == 1:
                            self.guardarArchivo(i)

    def encenderLed(self):
        self.led.encender()

    def apagarLed(self):
        self.led.apagar()

    def guardarArchivo(self, datos):
        if self.mongo.insert_one(self.collecion, datos) is False: 
            self.bandera2 = 2
            print("La conexión con la base de datos no se pudo establecer. Guardando en archivo...")

            ultimoSensor = datos
            self.lectura.clearFile("Sensores.json")
            self.lectura.agregar(ultimoSensor)
            self.medirTodos()

    def borrarHilo(self):
        timer = threading.Timer(self.wait, self.borrarHilo)
        timer.start()

        if self.bandera2 == 1:
            self.timer_count += 1
            if self.timer_count >= self.wait / 60:
                self.lectura.clearFile("Sensores.json")
                print("Historial local eliminado")
                self.timer_count = 0 
        else:
            print("Se reinicio el contador")
            self.timer_count = 0

if __name__ == "__main__":
    menu = Menu()
    menu.main()
