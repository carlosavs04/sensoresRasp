from Lista import Lista
from bson import ObjectId

class Sensores(Lista):
    def __init__(self, key="", nombre="", valores="", dato="", fecha="",hora="", pines = ""):
        super().__init__("Sensores.json")
        self.nombre=nombre
        self.key=key
        self.valores=valores
        self.dato=dato
        self.fecha=fecha
        self.hora=hora
        self.pines=pines
        self._id = ObjectId()

    def __str__(self):
        return f"{self.key},{self.nombre},{self.valores},{self.dato},{self.fecha},{self.hora},{self.pines}"

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
                self.nombre=self.key
            diccionario = {'_id': str(self._id),"key":self.key, "nombre": self.nombre, "valores":self.valores, "fecha":self.fecha,"hora":self.hora,"pines":self.pines}
            listaDicc.append(diccionario)
            return diccionario

    def from_json(self):
        sensor_json = self.json.readDocument()
        sensor_obj = []
        for sensor in sensor_json:
            cli = Sensores(sensor["key"], sensor["nombre"], sensor["valores"], sensor["fecha"], sensor["hora"], sensor["pines"])
            sensor_obj.append(cli)
        return sensor_obj
