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
        self.tipoDato = ""
    def tipoSensor(self):
        valores=[]
        self.tipo=""

        if self.path == "ult":
            self.tipo="Ultrasonico"
            sensorUlt = UltrasonicSensor(trigger_pin=self.pin[0], echo_pin=self.pin[1])
            distancia = sensorUlt.medirDistancia()
            valores.append(distancia)
            self.tipoDato="Cm"

        elif self.path=="tmp":
            self.tipo="Temperatura"
            sensor = temperatura(self.pin[0])
            hum, temp = sensor.lectura()
            if hum is not None:
                valores.append(hum)
                valores.append(temp)

        elif self.path=="led":
            self.tipo="Led"
            stat = self.led1.toggle()
            valores.append(stat)
        return valores

    def lectura(self):
        arreglo = self.tipoSensor()
        timestamp = time.time()
        fecha_hora = datetime.datetime.fromtimestamp(timestamp)
        cadena_fecha_hora = fecha_hora.strftime('%H:%M:%S')
        print(arreglo)
        if self.path == "tmp" and arreglo < 0:
            data=[]
            data0 = {
                "nombre": self.nombre,
                "tipo": self.tipo,
                "valores": arreglo[0],
                "dato":"°C",
                "fecha": cadena_fecha_hora,
                "pines": self.pin
            }
            data.append(data0)
            data1={
                "nombre":self.nombre,
                "tipo":"hum",
                "valores":arreglo[1],
                "dato":"hum",
                "fecha":cadena_fecha_hora,
                "pines":self.pin
            }
            data.append(data1)
            jsonS = json.dumps(data)

        else:
            data = {
                "nombre": self.nombre,
                "tipo": self.tipo,
                "valores": arreglo,
                "dato":self.tipoDato,
                "fecha": cadena_fecha_hora,
                "pines": self.pin
            }
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
