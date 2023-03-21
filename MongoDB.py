import pymongo

class MongoDB:
    def __init__(self):
        self.client = ""
        self.db = ""

    def createConnection(self):
        try:
            self.client = pymongo.MongoClient("mongodb+srv://root:admin@cluster0.jrax7sh.mongodb.net/?retryWrites=true&w=majority")
            self.db = self.client["Raspberry"]
            print("Conexión exitosa.")
            return True
        
        except Exception as e:
            print("Error al conectar a la base de datos: ", e)
            return False
        
    def insert_one(self, collection, data):
        col = self.db[collection]
        col.insert_one(data)
        if self.find_one(collection,data):
            return True
        else:
            return False

    def insert_many(self, collection, data_list):
        col = self.db[collection]
        result = col.insert_many(data_list)
        return result.acknowledged

    def find_one(self, collection, query={}):
        col = self.db[collection]
        return col.find_one(query)

    def find_many(self, collection, query={}):
        col = self.db[collection]
        return col.find(query)

    def update_one(self, collection, query, new_values):
        col = self.db[collection]
        col.update_one(query, {"$set": new_values})

    def delete_one(self, collection, query):
        col = self.db[collection]
        col.delete_one(query)

    def delete_many(self, collection, query):
        col = self.db[collection]
        col.delete_many(query)
