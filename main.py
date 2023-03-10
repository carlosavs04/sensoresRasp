import time
from interBD import interBD
from Mongo import Mongo
from sensores import sensor
import json
from ultimaLectura import Sensores
import threading
class main:
    def __init__(self):
        self.sensores = Sensores()
        self.bandera = 0
        self.dispositivo = ""
        self.mongo = Mongo()
        self.obj = Mongo()
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
                self.lectura2()
            if opcion == "2":
                interBD().mainBd()
            # elif opcion == "7":
            #     self.juntos()
            elif opcion == "5":
                # Salir
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")

    def sensoresLectura(self, arreglo):
        # temp = sensor("tmp", [5], "Cocina")
        # ult = sensor("ult",[23,24],"Puerta")
        # led = sensor("led",[17],"Foco")
        # sensores=[temp,led, ult]
        sensores=arreglo
        # sensores=[temp]
        x=0
        for sens in sensores:
            x=x+1
            # print(sens.lectura())
            data=json.loads(sens.lectura())
            if len(data)>=1:
                for i in data:
                    # print(i)
                    # i es el json
                    if len(i["pines"]) == 1:
                        # print(i["nombre"])
                        # print(i["tipo"])
                        # print(i["valores"])
                        # print(i["dato"])
                        # print(i["fecha"])
                        # print(i["pines"][0])
                        print("|{:<3} | {:<20} | {:<25} | {:<7}{:<4} | {:<10} | {:<10} | {:<5}|".format(x, i["nombre"],
                                                                                           i["tipo"],
                                                                                           i["valores"],
                                                                                           i["dato"],
                                                                                           i["fecha"],
                                                                                           i["hora"],
                                                                                           i["pines"][0]))
                    elif len(i["pines"]) == 2:
                        # print(i["nombre"])
                        # print(i["tipo"])
                        # print(i["valores"])
                        # print(i["dato"])
                        # print(i["fecha"])
                        # print(i["pines"][0])
                        # print(i["pines"][1])
                        print("|{:<3} | {:<20} | {:<25} | {:<7}{:<4} | {:<10} | {:<2} {:<2}|".format(x,i["nombre"],
                                                                                            i["tipo"],
                                                                                            i["valores"],
                                                                                            i["dato"],
                                                                                            i["fecha"],
                                                                                            i["hora"],
                                                                                            i["pines"][0],
                                                                                            i["pines"][1]))
                    return i

    #                     Logica para insertar en docs:

    def lectura2(self):
        temp = sensor("tmp", [5], "Cocina")
        ult = sensor("ult", [23, 24], "Puerta")
        led = sensor("led", [17], "Foco")
        sensores = [temp, led, ult]
        i = self.sensoresLectura(sensores)

        if self.bandera2 == 1:  # si esta en conexion
            lista = self.sensores.mostrar()
            if len(lista) >= 1:  # si la lista de sensores tiene objetos, debe ingresarlos a la bd antes de los otros
                for x in lista:
                    if self.obj.find_one(self.colecion, x):
                        pass
                    else:
                        self.obj.insert_one(self.colecion, x)
                self.sensores.borrarInfo("Sensores.json")
            self.hiloBorrarPTiempo()

            while True:  # tiempo en segundos
                # aux = self.sensores.mostrar()
                # if len(aux) >= 1:
                #     ubi = len(aux) - 1
                #     if self.obj.find_one(self.colecion, aux[ubi]):
                #         pass
                #     else:
                #         self.obj.insert_one(self.colecion, aux[ubi])

                self.sensores.agregar(i)

                if self.obj.insert_one(self.colecion,i) is False:  # si no se inserto, debe cambiar la bandera
                    self.bandera2 = 2
                    print("Se perdio la conexion, guardando solo localmente")
                    ultimoSensor = i  # guarda la lecutra donde sucede la desconexion
                    self.sensores.borrarInfo("Sensores.json")  # borra datos para no repetirlos
                    self.sensores.agregar(ultimoSensor)
                    self.lectura2()  # debe regresar al metodo para empezar a guardar solo local


        else:  # guarda solo local-----ya funciona este
            print("Guardando localmente..")
            print(
                "|{:<3} | {:<20} | {:<25} | {:<11} | {:<10} | {:<10} | {:<5}|".format("#", "Nombre", "Tipo", "Valores",
                                                                                      "Fecha", "Hora", "Pines"))
            while True:
                # user_input = input()
                # if user_input == " ":
                #     break
                self.sensores.agregar(i)


    def menu(self):
        print("----------------------------------------------")
        print("Sistema de gestión de dispositivos raspberry")
        if self.veces == 2:
            resultado = interBD().checkarConexionEnUso()
            if resultado:
                self.bandera2 = 1
                self.obj = resultado[0]
                self.obj.conect()
                self.bandera = resultado[1]
                print(f"Datos de conexion: {self.obj.user}-{self.obj.cluster}-{self.obj.bd}------")
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

    def ultimaLectura(self):
        sensores = self.sensores.from_json()
        print("|{:<25} {:<5}|".format("Sensor", "Valor"))
        for sens in sensores:
            print("|{:<25} {:<5}|".format(sens.nombre, sens.valor))

    def hiloBorrarPTiempo(self):
        timer = threading.Timer(self.tiempoEspera, self.hiloBorrarPTiempo)
        timer.start()

        if self.bandera2 == 1:  # si esta en conexion
            self.timer_count += 1  # incrementa el contador de tiempo
            if self.timer_count >= self.tiempoEspera / 60:  # verifica si han pasado 15 minutos
                self.sensores.borrarInfo("Sensores.json")
                print("Se borro historial local")
                print("---------------------------------------------------------------")
                self.timer_count = 0  # resetea el contador de tiempo
        else:
            print("Se reinicio el contador")
            self.timer_count = 0

if __name__ == "__main__":
    main().main()
