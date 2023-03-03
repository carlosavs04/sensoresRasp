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
        sensores=[temp,ult]
        print("{:<20} {:<25} {:<20} {:<20} {:<20}".format("Nombre", "Tipo", "Valores", "Tiempo", "Pines"))

        while True:

            for sens in sensores:
                # print(sens.lectura())
                data=json.loads(sens.lectura())
                print(data["nombre"])
                # print("{:<20} {:<25} {:<20} {:<20} {:<20} {:<20}".format(data["nombre"], data["tipo"], data["valores"], data["fecha"],data["pines"]))

    def menu(self):
        print("------------Menu------------")
        print("1. Sensores")
        print("5. Salir")
        print("----------------------------")
        opcion = input("Seleccione una opción: ")
        return opcion


if __name__ == "__main__":
    main().main()
