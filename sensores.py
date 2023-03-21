from Ultrasonico import Ultrasonico
from Temperatura import Temperatura
from led import Led
import time
import json
import datetime
from bson import ObjectId
from Lectura import Lectura
class sensor:
    def __init__(self,path="",pin=[],nombre=""):
        self.path=path
        self.pin=pin
        self.nombre=nombre
        self.sens=Lectura()
        if nombre == "":
            self.nombre = self.path
        if self.path == "led":
            self.led1 = Led(self.pin[0])
        self.tipoDato = [""]
        self._id = ObjectId()
    def tipoSensor(self):
        valores=[]

        if self.path == "ult":
            sensorUlt = Ultrasonico(self.pin[0], self.pin[1])
            distancia = sensorUlt.medirDistancia()
            valores.append(distancia)
            self.tipoDato=["Cm"]
        elif self.path=="tmp":

            self.tipoDato=["°C"," h"]
            sensor = Temperatura(self.pin[0])
            hum, temp = sensor.medirTemperatura()
            if hum is not None and temp is not None:
                valores.append(hum)
                valores.append(temp)

        elif self.path=="led":
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
                sensor1=Lectura(self.path,self.nombre,arreglo[0],self.tipoDato[0],cadena_fecha,cadena_fecha_hora,self.pin,)
                data.append(sensor1.getDict())
                sensor2=Lectura(self.path,self.nombre,arreglo[1],self.tipoDato[1],cadena_fecha,cadena_fecha_hora,self.pin,)
                data.append(sensor2.getDict())

        else:
            sensor1 = Lectura(self.path, self.nombre, arreglo[0], self.tipoDato[0], cadena_fecha, cadena_fecha_hora, self.pin, )
            data.append(sensor1.getDict())
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
