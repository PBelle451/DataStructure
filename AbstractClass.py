# Abstract Class é uma classe que não pode ser instanciada diretamente e é projetada para ser herdada por outras classes.
from abc import ABC, abstractmethod

# Definindo uma classe abstrata
class Animal(ABC):

    @abstractmethod
    def fazer_som(self):
        pass    # Método abstrato é passado

    def mover(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

    def mover(self):
        return "Correndo em quatro patas"

class Passaro(Animal):
    def fazer_som(self):
        return "Piu piu!"

    def mover(self):
        return "Voando"

if __name__ == '__main__':
    cachorro = Cachorro()
    print(cachorro.fazer_som())
    print(cachorro.mover())

    passaro = Passaro()
    print(passaro.fazer_som())
    print(passaro.mover())