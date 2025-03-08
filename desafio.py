import time

class Carro:
    def __init__(self, marca, modelo, ano, motor, roda, quantidade_rodas, ligado=False):
        self.marca = marca
        self._modelo = modelo
        self.__ano = ano
        self.ligado = ligado
        self.motor = motor
        self.roda = roda
        self.quantidade_rodas = quantidade_rodas

    def exibir_info(self):
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Carro: {self.marca}, Modelo: {self.modelo}, Estado: {estado}\nMotor-> {self.motor.exibir_info()}")
        print(f"Rodas: {self.quantidade_rodas}x {self.roda.exibir_info()}")

    def ligar(self):
        if self.ligado:
            print("O carro já está ligado.")
        else:
            print("Ligando carro...")
            time.sleep(1)
            print("Carro ligado!")
            self.ligado = True

    def desligar(self):
        if not self.ligado:
            print("O carro já está desligado.")
        else:
            print("Desligando carro...")
            time.sleep(1)
            print("Carro desligado!")
            self.ligado = False

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        if isinstance(novo_modelo, str) and novo_modelo.strip():
            self._modelo = novo_modelo
        else:
            print("Modelo invalido")

    def get_ano(self):
        return self.__ano

    def set_ano(self, novo_ano):
        if isinstance(novo_ano, int) and novo_ano > 1886:
            self.__ano = novo_ano

class CarroEsportivo(Carro):
    def __init__(self, marca, modelo, ano, ligado=False, turbo=False):
        super().__init__(marca, modelo, ano, ligado=False)
        self.turbo = turbo

    def exibir_info(self):
        super().exibir_info()
        print(f"Turbo: {"Sim" if self.turbo else "Não"}")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo, ano, autonomia, ligado=False):
        super().__init__(marca, modelo, ano, ligado=False)
        self.autonomia = autonomia

    def exibir_info(self):
        super().exibir_info()
        print(f"Autonomia: {self.autonomia} horas")

class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def exibir_info(self):
        return f"Potencia: {self.potencia}cv"

class Roda:
    def __init__(self, tamanho, tipo):
        self.tamanho = tamanho
        self.tipo = tipo

    def exibir_info(self):
        return f"{self.tamanho}, {self.tipo}"

motor_padrao = Motor(150)
roda_padrao = Roda("16 Polegadas", "Liga leve")

c1 = Carro("Volkswagen", "Gol", 2002, motor_padrao, roda_padrao, 4)
c2 = Carro("Chevrolet", "Onix", 2024, motor_padrao, roda_padrao, 4)
c3 = Carro("Toyotta", "Corolla", 2022, motor_padrao, roda_padrao, 4)

lista = [c1,c2,c3]

for carro in lista:
    carro.exibir_info()
    print("\n")