# Trilha de treinamento de classes e objetos
Criei essa lista com auxilio do ChatGPT para treinar os principais conceitos de POO em Python
***
# Nível 1 - Fundamentos de Classes e Objetos
## 1️⃣ Criando uma classe simples

Crie uma classe Carro com os atributos marca, modelo e ano.
Instancie um objeto e imprima seus atributos.
## 2️⃣ Métodos básicos

Adicione um método exibir_info() que imprime as informações do carro.
## 3️⃣ Construtores (__init__)

Modifique a classe para inicializar os atributos no construtor.
# Nível 2 - Métodos e Encapsulamento
## 4️⃣ Adicionando comportamento

Adicione um método ligar() e desligar() que muda um atributo ligado (True/False).
## 5️⃣ Encapsulamento

Torne o atributo ano privado e crie um método get_ano() para acessá-lo.
## 6️⃣ Propriedades (@property)

Use @property para permitir acesso controlado ao atributo modelo.
# Nível 3 - Herança e Polimorfismo
## 7️⃣ Criando subclasses

Crie uma classe CarroEsportivo que herda de Carro e adiciona o atributo turbo (True/False).
## 8️⃣ Sobrescrita de métodos

Modifique exibir_info() na subclasse para incluir se o carro tem turbo.
## 9️⃣ Polimorfismo

Crie outra subclasse CarroEletrico e sobrescreva exibir_info() para incluir a autonomia da bateria.
# Nível 4 - Relacionamento entre Classes
## 🔟 Agregação

Crie uma classe Motor com um atributo potencia e relacione com Carro.
## 1️⃣1️⃣ Composição

Crie uma classe Roda e faça um carro ter 4 rodas.
## 1️⃣2️⃣ Lista de Objetos

Crie uma lista de carros e itere sobre ela para exibir as informações de cada um.
# Nível 5 - Avançado
## 1️⃣3️⃣ Métodos Mágicos (__str__, __len__, __eq__)

Implemente __str__() para que print(objeto) exiba informações do carro.
Implemente __eq__() para comparar se dois carros são iguais (mesmo modelo e ano).
## 1️⃣4️⃣ Classe Abstrata (ABC)

Crie uma classe abstrata Veiculo e obrigue Carro e Moto a implementarem um método mover().
## 1️⃣5️⃣ Métodos Estáticos (@staticmethod)

Adicione um método estático exibir_contagem() que mostra quantos carros foram criados.
