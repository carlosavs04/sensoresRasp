from Lista import Lista
from bson import ObjectId

class Lectura(Lista):
    def __init__(self, key = "", nombre = "", descripcion = "", valores = "", dato = "", fecha = ""):
        super().__init__("Sensores.json")
        self.key = key
        self.nombre = nombre
        self.descripcion = descripcion
        self.valores = valores
        self.dato = dato
        self.fecha = fecha
        self._id = ObjectId()

    def __str__(self):
        return f"{self.key}, {self.nombre}, {self.descripcion}, {self.valores}, {self.dato}, {self.fecha}"

    def getDict(self):
        listaDicc = []
        if type(self) == list:
            for item in self:
                if type(item) == dict:
                    listaDicc.append(item)
                else:
                    listaDicc.append(item.getDict())
            return listaDicc
        
        elif type(self) == dict:
            listaDicc.append(self.listas)
        
        else:
            diccionario = {'_id': str(self._id), "key": self.key, "nombre": self.nombre, "descripcion": self.descripcion, "valores": self.valores, "dato": self.dato,"fecha": self.fecha}
            listaDicc.append(diccionario)
            return diccionario

    def getObject(self):
        sensor_json = self.json.readDocument()
        sensor_obj = []
        for i in sensor_json:
            cli = Lectura(i["key"], i["nombre"], i["descripcion"], i["valores"], i["dato"], i["fecha"])
            sensor_obj.append(cli)
        return sensor_obj
