class Bola:
    def __init__(self, cor="", circunferencia=0, material=""):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, novaCor):
        self.cor = novaCor

    def mostrarCor(self):
        return f"A cor da bola é {self.cor}"


bolaDeFutebol = Bola("Branca", 70, "Couro sintético")

bolaDeFutebol.trocarCor("branca e preta")

print(bolaDeFutebol.mostrarCor())