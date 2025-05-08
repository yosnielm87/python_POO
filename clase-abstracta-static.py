#Clase Abstracta: la plantilla o modelo de las clases que se heredan

from abc import ABC, abstractmethod

class Animal(ABC):
    #Atributo estatico (atributo de clase): va a estar disponible independiente de la instancia
    cantidad_de_animales = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Animal.cantidad_de_animales += 1

    @abstractmethod
    def hacer_sonido(self):
        pass

    #Metodo de clase: es un metodo que se puede ejecutar desde la misma clase
    #cls: se refiere a la clase [al ser un atributo estatico le pertenece a la clase y no a la instancia]
    @classmethod
    def obtenerCntAnimales(cls):
        print(f"La cantidad de animales actual es de: {cls.cantidad_de_animales}")

#Clase derivada Perro
class Perro(Animal):
    def hacer_sonido(self):
        print(f"Me llamo {self.nombre} y hago Guau Guau")

    def mover_cola(self):
        print(f"{self.nombre} mueve la cola de felicidad")     
       
#Clase derivada Gato
class Gato(Animal):
    def hacer_sonido(self):
        print(f"Me llamo {self.nombre} y hago Miau Miau")

    def ronronear(self):
        print(f"{self.nombre} ronronea de felicidad")

perrito = Perro("Manchita")
gatito = Gato("Pelusa")

perrito.hacer_sonido()
perrito.mover_cola()
gatito.hacer_sonido()
gatito.ronronear()

Animal.obtenerCntAnimales()