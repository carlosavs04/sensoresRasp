from Ultrasonico import Ultrasonico
from Temperatura import Temperatura
from led import Led
import time
import json
import datetime
from bson import ObjectId
from ultimaLectura import Sensores
class sensor:
    def __init__(self,path="",pin=[],nombre=""):
        self.path=path
        self.pin=pin
        self.nombre=nombre
        self.sens=Sensores()
        if nombre == "":
            self.nombre = self.path
        if self.path == "led":
            self.led1 = Led(self.pin[0])
        self.tipoDato = [""]
        self._id = ObjectId()
    def tipoSensor(self):
        valores=[]
        self.tipo=""

        if self.path == "ult":
            self.tipo=["Ultrasonico"]
            sensorUlt = Ultrasonico(self.pin[0], self.pin[1])
            distancia = sensorUlt.medirDistancia()
            valores.append(distancia)
            self.tipoDato=["Cm"]
        elif self.path=="tmp":
            self.tipo=["Temperatura","Humedad"]
            self.tipoDato=["°C"," h"]
            sensor = Temperatura(self.pin[0])
            hum, temp = sensor.medirTemperatura()
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
        try:
            self._id.is_valid()
        except:
            pass
        else:
            self._id=ObjectId
        if self.path == "tmp":
            if len(arreglo) > 1:
                sensor1=Sensores(self.path,self.nombre,self.tipo[0],arreglo[0],self.tipoDato[0],cadena_fecha,cadena_fecha_hora,self.pin,)
                data.append(sensor1.to_dict())
                sensor2=Sensores(self.path,self.nombre,self.tipo[1],arreglo[1],self.tipoDato[1],cadena_fecha,cadena_fecha_hora,self.pin,)
                data.append(sensor2.to_dict())

        else:
            sensor1 = Sensores(self.path, self.nombre, self.tipo[0], arreglo[0], self.tipoDato[0], cadena_fecha, cadena_fecha_hora, self.pin, )
            data.append(sensor1.to_dict())
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
