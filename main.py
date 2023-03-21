import time
from MongoDB import MongoDB
from sensores import sensor
import json
from Lectura import Lectura
import threading
class main:
    def __init__(self):
        self.sensores = Lectura()
        self.bandera = 0
        self.dispositivo = ""
        self.obj = MongoDB()
        self.tiempoEspera = 120  # tiempo en segundos
        self.timer_count = 0  # contador de tiempo para borrar historial local
        self.veces = 2
        self.colecion = "Sensores"

    def contador(self, tiempo):
        for i in range(tiempo, -1, -1):
            time.sleep(1)
        return True
    def main(self):
        opcion = ""
        while opcion != "5":
            opcion = self.menu()
            if opcion == "1":
                self.sensoresLectura()
            elif opcion == "5":
                # Salir
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")

    def sensoresLectura(self):
        temp = sensor("tmp", [4], "Cocina")
        ult = sensor("ult",[23,24],"Puerta")
        led = sensor("led",[17],"Foco")
        sensores=[temp,led, ult]
        # sensores=[temp]
        z=0
        if self.bandera2 == 1:  # si esta en conexion
            lista = self.sensores.mostrar()
            if len(lista) >= 1:  # si la lista de sensores tiene objetos, debe ingresarlos a la bd antes de los otros
                for x in lista:
                    if self.obj.find_one(self.colecion, x):
                        pass
                    else:
                        self.obj.insert_one(self.colecion, x)
                self.sensores.clearFile("Sensores.json")
            self.hiloBorrarPTiempo()
        while True:
            for sens in sensores:
                z=z+1
                # print(sens.lectura())
                data=json.loads(sens.lectura())
                if len(data)>=1:
                    for i in data:
                        print("|{:<3} | {:<20} | {:<25} | {:<7}{:<4} | {:<10} |".format(z, i["nombre"],i["descripcion"],i["valores"],i["dato"],i["fecha"]))
                        self.sensores.agregar(i)
                        if self.bandera2==1:
                            self.guardar(i)

    def guardar(self,sensor):

        if self.obj.insert_one(self.colecion,sensor) is False:  # si no se inserto, debe cambiar la bandera
            self.bandera2 = 2
            print("Se perdio la conexion, guardando solo localmente")
            ultimoSensor = sensor  # guarda la lecutra donde sucede la desconexion
            self.sensores.clearFile("Sensores.json")  # borra datos para no repetirlos
            self.sensores.agregar(ultimoSensor)
            self.sensoresLectura()  # debe regresar al metodo para empezar a guardar solo local

    def menu(self):
        print("----------------------------------------------")
        print("Sistema de gestión de dispositivos raspberry")
        if self.veces == 2:
            conexion = self.obj.createConnection()
            if conexion is not False:
                self.bandera2 = 1
                print(f"Estado: {self.bandera}")
                self.veces = 1

            else:
                self.bandera2 = 2
                self.veces = 1
                print("No hay conexion activa")
        print("------------Menu------------")
        print("1. Sensores")
        print("2. Configuracion Bd")
        print("5. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion

    def hiloBorrarPTiempo(self):
        timer = threading.Timer(self.tiempoEspera, self.hiloBorrarPTiempo)
        timer.start()

        if self.bandera2 == 1:  # si esta en conexion
            self.timer_count += 1  # incrementa el contador de tiempo
            if self.timer_count >= self.tiempoEspera / 60:  # verifica si han pasado 15 minutos
                self.sensores.clearFile("Sensores.json")
                print("Se borro historial local")
                print("---------------------------------------------------------------")
                self.timer_count = 0  # resetea el contador de tiempo
        else:
            print("Se reinicio el contador")
            self.timer_count = 0

if __name__ == "__main__":
    main().main()
