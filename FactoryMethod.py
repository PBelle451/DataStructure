from abc import ABC, abstractmethod

#Criação da classe abstrata que define a interface
class Veiculo(ABC):

    @abstractmethod
    def entregar(self):
        pass

class Carro(Veiculo):
    def entregar(self):
        return "Entregando um carro!"

class Caminhao(Veiculo):
    def entregar(self):
        return "Entregando um caminhão!"

class Moto(Veiculo):
    def entregar(self):
        return "Entregando uma moto!"

class Transportadora(ABC):

    @abstractmethod
    def criar_veiculo(self) -> Veiculo:
        pass

    def realizar_entrega(self):
        veiculo = self.criar_veiculo()
        resultado = veiculo.entregar()
        print(resultado)

# Implementando métodos concretos do Factory Method
class TransportadoraCarro(Transportadora):
    def criar_veiculo(self) -> Veiculo:
        return Carro()

class TransportadoraCaminhao(Transportadora):
    def criar_veiculo(self) -> Veiculo:
        return Caminhao()

class TransportadoraMoto(Transportadora):
    def criar_veiculo(self) -> Veiculo:
        return Moto()

# Simulação do uso do Factory Method
def cliente(transportadora: Transportadora):
    transportadora.realizar_entrega()

if __name__ == '__main__':
    print("Usando a Transportadora de Carros:")
    cliente(TransportadoraCarro())

    print("\nUsando a Transportadora de Caminhões:")
    cliente(TransportadoraCaminhao())

    print("\nUsando a Transportadora de Motos:")
    cliente(TransportadoraMoto())