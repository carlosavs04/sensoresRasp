from JsonFile import JsonFile

class Lista:
    def __init__(self, archivo):
        self.json = JsonFile(archivo)
        self.listas = self.json.readDocument()

    def agregar(self, datos):
        self.listas.append(datos)
        self.json.writeDocument(self.listas)

    def actualizar(self, cli, datos):
        if self.listas:
            self.listas[int(cli)] = datos
            self.json.writeDocument(self.listas)

    def mostrar(self):
        return self.listas

    def eliminar(self, cli):
        self.listas.pop(int(cli))
        self.json.writeDocument(self.listas)

    def clearFile(self, archivo):
        self.listas.clear()
        self.json.writeDocument([])

