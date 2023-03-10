from Lista import Lista
from bson import ObjectId

#clave = nombre que viene desde arduino
#nombre= nombre que el usuario da
#valor = pos el valor que tiene el sensor

class Sensores(Lista):
    def __init__(self,clave="", nombre="", tipo= "", valores="", dato="", fecha="",hora="", pines = ""):
        super().__init__("Sensores.json")
        self.nombre=nombre
        self.clave=clave
        self.tipo=tipo
        self.valores=valores
        self.dato=dato
        self.fecha=fecha
        self.hora=hora
        self.pines=pines
        self._id = ObjectId()

    def __str__(self):
        return f"{self.clave},{self.nombre},{self.tipo},{self.valores},{self.dato},{self.fecha},{self.hora},{self.pines}"

    def to_dict(self):
        listaDicc = []
        if type(self) == list:
            for item in self:
                if type(item) == dict:
                    listaDicc.append(item)
                else:
                    listaDicc.append(item.to_dict())
            return listaDicc
        elif type(self) == dict:
            listaDicc.append(self.listas)
        else:
            if self.nombre=="":
                self.nombre=self.clave
            diccionario = {"clave":self.clave, "nombre": self.nombre, "tipo":self.tipo , "valores":self.valores, "dato": self.dato,"fecha":self.fecha,"hora":self.hora,"pines":self.pines}
            listaDicc.append(diccionario)
            return diccionario

    def from_json(self):
        sensor_json = self.json.leer_de_json()
        sensor_obj = []
        for sensor in sensor_json:
            cli = Sensores(sensor["clave"], sensor["nombre"], sensor["tipo"], sensor["valores"], sensor["dato"], sensor["fecha"], sensor["hora"], sensor["pines"])
            sensor_obj.append(cli)
        return sensor_obj
