class Retangulo:
    def __init__(self, ladoA=0, ladoB=0):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarValorDosLados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def retornarValorDosLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return self.ladoA * self.ladoB

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)


sala = Retangulo()

ladA = float(input("Digite o comprimento da sala: "))
ladB = float(input("Digite a largura da sala: "))

sala.mudarValorDosLados(ladA, ladB)

area = sala.calcularArea()
perimetro = sala.calcularPerimetro()

print(f"Área da sala: {area} m²")
print(f"Piso necessário: {area} m²")
print(f"Rodapé necessário: {perimetro} metros")