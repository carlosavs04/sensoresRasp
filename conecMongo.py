import pymongo
from pymongo.server_api import ServerApi


class MongoConexion:
    def __init__(self):
        self.client = ""
        self.database = ""

    def createConnection(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://root:admin@cluster0.jrax7sh.mongodb.net/?retryWrites=true&w=majority")
            self.database = self.client["Raspberry"]
            print("Conexión exitosa.")
            return True
        
        except Exception as e:
            print("Error al conectar a la base de datos: ", e)
            return False
        
    def insert_one(self, collection, data):
        coll = self.db[collection]
        coll.insert_one(data)
        if self.find_one(collection,data):
            return True
        else:
            return False

    def insert_many(self, collection, data_list):
        coll = self.db[collection]
        result = coll.insert_many(data_list)
        return result.acknowledged

    def find_one(self, collection, query={}):
        coll = self.db[collection]
        return coll.find_one(query)

    def find_many(self, collection, query={}):
        coll = self.db[collection]
        return coll.find(query)

    def update_one(self, collection, query, new_values):
        coll = self.db[collection]
        coll.update_one(query, {"$set": new_values})

    def delete_one(self, collection, query):
        coll = self.db[collection]
        coll.delete_one(query)

    def delete_many(self, collection, query):
        coll = self.db[collection]
        coll.delete_many(query)


if __name__ == "__main__":
    #mongodb+srv://admin:root@cluster0.hcy4jnm.mongodb.net/?retryWrites=true&w=majority

    mongo_object = MongoConexion("mongodb+srv://admin:root@cluster0.hcy4jnm.mongodb.net/?retryWrites=true&w=majority","Prueba","cluster0")
    datos={"codigo": "2333", "nombre": "214", "descripcion": "32", "precio": 23, "stat": 2}
    print(mongo_object.getStatus())
