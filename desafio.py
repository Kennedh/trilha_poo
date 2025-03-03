class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_info(self):
        print(f"{self.__class__.__name__} {", ".join(f"{chave.title()}: {valor}" for chave, valor in self.__dict__.items())}")

c1 = Carro("Volkswagen", "Gol", 2002)

c1.exibir_info()
