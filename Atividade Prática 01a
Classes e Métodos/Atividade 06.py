class TV:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, novoCanal):
        if 1 <= novoCanal <= 100:
            self.canal = novoCanal
        else:
            print("Canal inválido")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo atingido")

    def mostrarDados(self):
        return f"Canal: {self.canal}, Volume: {self.volume}"


# Programa principal
tv = TV()

canal = int(input("Digite o canal: "))
tv.mudarCanal(canal)

tv.aumentarVolume()
tv.aumentarVolume()

tv.diminuirVolume()

print(tv.mostrarDados())