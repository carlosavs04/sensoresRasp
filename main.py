import time

from sensores import sensor
import json

class main:
    def main(self):
        opcion = ""
        while opcion != "5":
            opcion = self.menu()
            if opcion == "1":
                self.juntos()
            elif opcion == "5":
                # Salir
                print("Saliendo del sistema...")
                break
            else:
                print("Opción inválida, intente de nuevo.")
                input("Presione Enter para continuar...")

    def juntos(self):

        # led1 = Led(17)

        temp = sensor("tmp", [5], "Cocina")
        ult = sensor("ult",[23,24],"Puerta")
        led = sensor("led",[17],"Foco")
        sensores=[temp,ult,led]
        print("|{:<3} | {:<20} | {:<25} | {:<10} | {:<10} | {:<5}|".format("#","Nombre", "Tipo", "Valores", "Tiempo", "Pines"))

        while True:
            i=0
            for sens in sensores:
                i=i+1
                # print(sens.lectura())
                data=json.loads(sens.lectura())
                if len(data)>=1:
                 print(data)
                # for i in data:
                #     print(i)
                    # if len(data["pines"]) == 1:
                    #     print("|{:<3} | {:<20} | {:<25} | {:<8}{:<2} | {:<10} | {:<5}|".format(i,data["nombre"], data["tipo"],
                    #                                                                     data["valores"],
                    #                                                                     data["dato"],
                    #                                                                     data["fecha"],
                    #                                                                     data["pines"][0]))
                    # elif len(data["pines"]) == 2:
                    #     print(
                    #         "|{:<3} | {:<20} | {:<25} | {:<8}{:<2} | {:<10} | {:<2} {:<2}|".format(i,data["nombre"],
                    #                                                                         data["tipo"],
                    #                                                                         data["valores"],
                    #                                                                            data["dato"],
                    #
                    #                                                                            data["fecha"],
                    #                                                                         data["pines"][0],
                    #                                                                         data["pines"][1]))

    def menu(self):
        print("------------Menu------------")
        print("1. Sensores")
        print("5. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion


if __name__ == "__main__":
    main().main()
