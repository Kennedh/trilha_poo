from abc import ABC, abstractmethod
import time

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, ligado=False):
        self.marca = marca
        self._modelo = modelo
        self.__ano = ano
        self.ligado = ligado

    @abstractmethod
    def exibir_info(self):
        """Método obrigatório para exibir informações do veículo."""
        pass

    def ligar(self):
        if self.ligado:
            print("O veículo já está ligado.")
        else:
            print("Ligando veículo...")
            time.sleep(1)
            print("Veículo ligado!")
            self.ligado = True

    def desligar(self):
        if not self.ligado:
            print("O veículo já está desligado.")
        else:
            print("Desligando veículo...")
            time.sleep(1)
            print("Veículo desligado!")
            self.ligado = False

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        if isinstance(novo_modelo, str) and novo_modelo.strip():
            self._modelo = novo_modelo
        else:
            print("Modelo inválido")

    def get_ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        if isinstance(novo_ano, int) and novo_ano > 1886:
            self.__ano = novo_ano

    def __eq__(self, outro):
        if isinstance(outro, Veiculo):
            return self.marca == outro.marca and self.modelo == outro.modelo and self.__ano == outro.__ano
        return False

    def __str__(self):
        estado = "Ligado" if self.ligado else "Desligado"
        return f"Veículo: {self.marca}, Modelo: {self.modelo}, Ano: {self.__ano}, Estado: {estado}"


class Carro(Veiculo):
    contador = 0

    def __init__(self, marca, modelo, ano, motor, roda, quantidade_rodas, ligado=False):
        super().__init__(marca, modelo, ano, ligado)
        self.motor = motor
        self.roda = roda
        self.quantidade_rodas = quantidade_rodas
        Carro.contador += 1

    def exibir_info(self):
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Carro: {self.marca}, Modelo: {self.modelo}, Estado: {estado}\nMotor-> {self.motor.exibir_info()}")
        print(f"Rodas: {self.quantidade_rodas}x {self.roda.exibir_info()}")

    def __str__(self):
        return super().__str__() + f"\nMotor -> {self.motor.exibir_info()}\nRodas: {self.quantidade_rodas}x {self.roda.exibir_info()}"

    @staticmethod
    def exibir_contagem():
        print(f"Total de carros criados: {Carro.contador}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, motor, roda, quantidade_rodas, ligado=False):
        super().__init__(marca, modelo, ano, ligado)
        self.motor = motor
        self.roda = roda
        self.quantidade_rodas = quantidade_rodas

    def exibir_info(self):
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Carro: {self.marca}, Modelo: {self.modelo}, Estado: {estado}\nMotor-> {self.motor.exibir_info()}")
        print(f"Rodas: {self.quantidade_rodas}x {self.roda.exibir_info()}")

    def __str__(self):
        return super().__str__() + f"\nMotor -> {self.motor.exibir_info()}\nRodas: {self.quantidade_rodas}x {self.roda.exibir_info()}"


class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, ano, motor, roda, quantidade_rodas, turbo=False, ligado=False):
        super().__init__(marca, modelo, ano, motor, roda, quantidade_rodas, ligado)
        self.turbo = turbo

    def exibir_info(self):
        super().exibir_info()
        print(f"Turbo: {'Sim' if self.turbo else 'Não'}")

    def __str__(self):
        return super().__str__() + f"\nTurbo: {'Sim' if self.turbo else 'Não'}"


class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, motor, roda, quantidade_rodas, autonomia, ligado=False):
        super().__init__(marca, modelo, ano, motor, roda, quantidade_rodas, ligado)
        self.autonomia = autonomia

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia: {self.autonomia} horas")

    def __str__(self):
        return super().__str__() + f"\nAutonomia: {self.autonomia} horas"


class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def exibir_info(self):
        return f"Potência: {self.potencia}"


class Roda:
    def __init__(self, tamanho, tipo):
        self.tamanho = tamanho
        self.tipo = tipo

    def exibir_info(self):
        return f"{self.tamanho}, {self.tipo}"


# Criando objetos
motor_padrao = Motor("150 cv")
motor_moto = Motor("200 cc")

roda_padrao = Roda("16 Polegadas", "Liga leve")
roda_moto = Roda("12 Polegadas", "Liga leve")

c1 = Carro("Volkswagen", "Gol", 2002, motor_padrao, roda_padrao, 4)
c2 = Carro("Chevrolet", "Onix", 2024, motor_padrao, roda_padrao, 4)
c3 = Carro("Toyota", "Corolla", 2022, motor_padrao, roda_padrao, 4)
c4 = Carro("Volkswagen", "Gol", 2002, motor_padrao, roda_padrao, 4)

m1 = Moto("Kawasaki", "Ninja 650", 2023, motor_moto, roda_moto, 2)

# Iterando em uma lista de carros
lista_de_veiculos = [c1, c2, c3, m1]

for carro in lista_de_veiculos:
    carro.exibir_info()
    print("---------------------------------------------------")

print(f"Teste str\n{c1}")

# Teste __eq__
print(c1 == c2)
print(c1 == c4)

Carro.exibir_contagem()
