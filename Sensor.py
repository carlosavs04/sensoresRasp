from Ultrasonico import Ultrasonico
from Temperatura import Temperatura
import time
import json
import datetime
from bson import ObjectId
from Lectura import Lectura

class Sensor:
    def __init__(self, key = "", pines = [], nombre = "", descripcion = ""):
        self.key = key
        self.pines = pines
        self.nombre = nombre
        self.descripcion = descripcion
        self.sens = Lectura()
        self.tipoDato = [""]
        self._id = ObjectId()

    def sensores(self):
        valores = []

        if self.key == "ult":
            sensorUltrasonico = Ultrasonico(self.pines[0], self.pines[1])
            distancia = sensorUltrasonico.medirDistancia()
            valores.append(distancia)
            self.tipoDato=["cm"]

        elif self.key == "tmp":
            self.tipoDato = ["°C","%"]
            sensorDht = Temperatura(self.pines[0])
            hum, temp = sensorDht.medirTemperatura()
            if hum is not None and temp is not None:
                valores.append(hum)
                valores.append(temp)

        else: 
            print("Sensor no encontrado")
            return None

        return valores

    def lectura(self):
        arreglo = self.sensores()
        timestamp = time.time()
        fecha = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        data=[]

        try:
            self._id.is_valid()

        except:
            pass

        else:
            self._id = ObjectId

        if self.key == "tmp":
            if len(arreglo) > 1:
                sensor1 = Lectura(self.key, self.nombre, self.descripcion, arreglo[0], self.tipoDato[0], fecha)
                data.append(sensor1.getDict())
                sensor2 = Lectura(self.key, self.nombre, self.descripcion, arreglo[1], self.tipoDato[1], fecha)
                data.append(sensor2.getDict())

        else:
            sensor1 = Lectura(self.key, self.nombre, self.descripcion, arreglo[0], self.tipoDato[0], fecha)
            data.append(sensor1.getDict())

        jsonS = json.dumps(data)
        return jsonS
