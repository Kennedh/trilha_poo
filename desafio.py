import time

class Carro:
    def __init__(self, marca, modelo, ano, ligado=False):
        self.marca = marca
        self._modelo = modelo
        self.__ano = ano
        self.ligado = ligado

    def exibir_info(self):
        estado = "Ligado" if self.ligado else "Desligado"
        print(f"Carro: {self.marca}, Modelo: {self.modelo}, Estado: {estado}")

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

c1 = Carro("Volkswagen", "Gol", 2002)
c1.exibir_info()

c1.modelo = "fox"
print(c1.modelo)
