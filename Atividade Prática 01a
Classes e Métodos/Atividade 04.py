class Pessoa:
    def __init__(self, nome="", idade=0, peso=0, altura=0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for i in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.altura += 0.005 

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura


pessoa = Pessoa("Lais Regina", 18, 59.0, 1.56)

anos = int(input("Quantos anos Lais Regina envelheceu? "))
pessoa.envelhecer(anos)

novoPeso = float(input("Quantos kg ela ganhou? "))
pessoa.engordar(novoPeso)

print("Nome:", pessoa.nome)
print("Idade:", pessoa.idade)
print("Peso:", pessoa.peso)
print("Altura:", pessoa.altura)