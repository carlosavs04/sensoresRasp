from ultrasonico import UltrasonicSensor
from temperatura import temperatura
from led import Led
import time
import json
import datetime

class sensor:
    def __init__(self,path="",pin=[],nombre=""):
        self.path=path
        self.pin=pin
        self.nombre=nombre
        if nombre == "":
            self.nombre = self.path
        if self.path == "led":
            self.led1 = Led(self.pin[0])
        self.tipoDato = [""]
    def tipoSensor(self):
        valores=[]
        self.tipo=""

        if self.path == "ult":
            self.tipo=["Ultrasonico"]
            sensorUlt = UltrasonicSensor(trigger_pin=self.pin[0], echo_pin=self.pin[1])
            distancia = sensorUlt.medirDistancia()
            valores.append(distancia)
            self.tipoDato=["Cm"]
        elif self.path=="tmp":
            self.tipo=["Temperatura","Humedad"]
            self.tipoDato=["°C"," h"]
            sensor = temperatura(self.pin[0])
            hum, temp = sensor.lectura()
            if hum is not None and temp is not None:
                valores.append(hum)
                valores.append(temp)

        elif self.path=="led":
            self.tipo=["Led"]
            stat = self.led1.toggle()
            if stat == 1:
                self.tipoDato= ["On"]
            else:
                self.tipoDato=["Off"]
            valores.append(stat)
        return valores

    def lectura(self):
        arreglo = self.tipoSensor()
        timestamp = time.time()
        fecha_hora = datetime.datetime.fromtimestamp(timestamp)
        cadena_fecha_hora = fecha_hora.strftime('%H:%M:%S')
        cadena_fecha= fecha_hora.strftime('%Y-%m-%d')
        data=[]
        if self.path == "tmp":
            if len(arreglo) > 1:
                data1 = {
                    "clave": self.path,
                    "nombre": self.nombre,
                    "tipo": self.tipo[0],
                    "valores": arreglo[0],
                    "dato": self.tipoDato[0],
                    "fecha":cadena_fecha,
                    "hora": cadena_fecha_hora,
                    "pines": self.pin
                }
                data.append(data1)
                data2 = {
                    "clave": self.path,
                    "nombre": self.nombre,
                    "tipo": self.tipo[1],
                    "valores": arreglo[1],
                    "dato": self.tipoDato[1],
                    "fecha": cadena_fecha,
                    "hora": cadena_fecha_hora,
                    "pines": self.pin
                }
                data.append(data2)
        else:
            data1 = {
                "clave": self.path,
                "nombre": self.nombre,
                "tipo": self.tipo[0],
                "valores": arreglo[0],
                "dato":self.tipoDato[0],
                "fecha": cadena_fecha,
                "hora": cadena_fecha_hora,
                "pines": self.pin
            }
            data.append(data1)
        jsonS = json.dumps(data)
        return jsonS


if __name__ == "__main__":
    led = sensor("led",[17],"Foco")
    print(led.lectura())
    input()
    print(led.lectura())
    input()
    print(led.lectura())
    input()
    print(led.lectura())
    input()
