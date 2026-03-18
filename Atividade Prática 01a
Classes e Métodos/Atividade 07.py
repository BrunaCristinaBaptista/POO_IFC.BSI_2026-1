class BichinhoVirtual:
    def __init__(self, nome="", fome=0, saude=100, idade=0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, nome):
        self.nome = nome

    def alterarFome(self, fome):
        self.fome = fome

    def alterarSaude(self, saude):
        self.saude = saude

    def alterarIdade(self, idade):
        self.idade = idade

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade

    def calcularHumor(self):
        humor = (self.saude - self.fome) / 2
        return humor


# Programa principal
bichinho = BichinhoVirtual("Tama", 20, 80, 2)

print(f"Nome: {bichinho.retornarNome()}")
print(f"Fome: {bichinho.retornarFome()}")
print(f"Saúde: {bichinho.retornarSaude()}")
print(f"Idade: {bichinho.retornarIdade()}")
print(f"Humor: {bichinho.calcularHumor()}")

bichinho.alterarFome(40)
bichinho.alterarSaude(60)

print("Após alterações:")
print(f"Humor: {bichinho.calcularHumor()}")