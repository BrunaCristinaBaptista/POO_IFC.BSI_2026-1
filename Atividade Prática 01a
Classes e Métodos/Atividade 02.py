class Quadrado:
    def __init__(self, tamanhoDoLado=0):
        self.tamanhoDoLado = tamanhoDoLado

    def mudarValorDoLado(self, tamanhoDoLado):
        self.tamanhoDoLado = tamanhoDoLado

    def retornarValorDoLado(self):
        return self.tamanhoDoLado

    def calcularArea(self):
        return self.tamanhoDoLado ** 2


quadrado = Quadrado()

lado = float(input("Digite o valor do lado: "))
quadrado.mudarValorDoLado(lado)

print(f"O lado do quadrado é {quadrado.retornarValorDoLado()}")
print(f"A área do quadrado é {quadrado.calcularArea()}")