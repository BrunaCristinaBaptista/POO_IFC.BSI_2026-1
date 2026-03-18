class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []


macaco1 = Macaco("Caco")
macaco2 = Macaco("Kiko")

macaco1.comer("banana")
print(f"Bucho do {macaco1.nome}: {macaco1.verBucho()}")

macaco1.comer("maçã")
print(f"Bucho do {macaco1.nome}: {macaco1.verBucho()}")

macaco1.comer("laranja")
print(f"Bucho do {macaco1.nome}: {macaco1.verBucho()}")

macaco2.comer("uva")
macaco2.comer("melancia")
macaco2.comer("pera")

print(f"Bucho do {macaco2.nome}: {macaco2.verBucho()}")

macaco1.comer(macaco2.nome)
print(f"Bucho do {macaco1.nome} após canibalismo: {macaco1.verBucho()}")