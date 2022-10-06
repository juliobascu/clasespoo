#clases

class Animal():
    def __init__(self,nombre) -> None:
        self.nombre=nombre


class Gato(Animal):
    def __init__(self, nombre,cant_bigotes) -> None:
        super().__init__(nombre)
        self.cant_bigotes=cant_bigotes

    def hablar(self):
        print("Miau Miau Miau")

class Perro(Animal):
    def __init__(self, nombre,muerde) -> None:
        super().__init__(nombre)
        self.muerde=muerde

    def hablar(self):
        print("Guau Guau Guau")

class Vaca(Animal):
    def __init__(self, nombre,es_lechera) -> None:
        super().__init__(nombre)
        self.es_lechera=es_lechera
    
    def hablar(self):
        print("Muuu Muuu Muuu")

animal1=Gato("Michi",23)
animal2=Perro("Firulai",True)
animal3=Vaca("Lola",False)

def hablar(objeto):
    objeto.hablar()

hablar(animal1)
hablar(animal2)
hablar(animal3)