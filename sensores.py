from ultrasonico import UltrasonicSensor
from temperatura import temperatura
from led import Led
import time
import json

class sensor:
    def __init__(self,path="",pin=[],nombre=""):
        self.path=path
        self.pin=pin
        self.nombre=nombre

    def tipoSensor(self):
        valores=[]
        self.tipo=""

        if self.path == "ult":
            self.tipo="Ultrasonico"
            sensorUlt = UltrasonicSensor(trigger_pin=self.pin[0], echo_pin=self.pin[1])
            distancia = sensorUlt.medirDistancia()
            valores.append(distancia)

        elif self.path=="tmp":
            self.tipo="Temperatura-Humedad"
            sensor = temperatura(self.pin[0])
            hum, temp = sensor.lectura()
            valores.append(hum)
            valores.append(temp)

        elif self.path=="led":
            self.tipo="Led"
            led1 = Led(self.pin[0])
            if self.bandera==1:
                led1.apagar()
                self.bandera=0
            else:
                led1.encender()
                self.bandera = 1
        return valores

    def lectura(self):
        arreglo = self.tipoSensor()
        data={
            "nombre":self.nombre,
            "tipo":self.tipo,
            "valores":arreglo,
            "fecha":time.time(),
            "pines":self.pin
        }
        jsonS=json.dumps(data)
        return jsonS
