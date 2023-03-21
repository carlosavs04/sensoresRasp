import json
import os

class JsonFile:
    def __init__(self, archivo):
        self.archivo = archivo

    def writeDocument(self, datos):
        with open(self.archivo, 'w') as archivo_json:
            json.dump(datos, archivo_json)

    def readDocument(self):
        try:
            with open(self.archivo, 'r') as archivo_json:
                datos = json.load(archivo_json)
            return datos
        
        except FileNotFoundError:
            with open(self.archivo, 'w') as archivo_json:
                json.dump([], archivo_json)
            return []

    def clearAllFiles(self):
        for file in os.listdir():
            if file.endswith(".json"):
                os.remove(file)

    def removeFile(self, archivo):
        os.remove(archivo)