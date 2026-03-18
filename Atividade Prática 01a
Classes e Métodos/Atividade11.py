class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  # km por litro
        self.combustivel = 0

    def andar(self, distancia):
        litrosNecessarios = distancia / self.consumo

        if litrosNecessarios <= self.combustivel:
            self.combustivel -= litrosNecessarios
            print(f"O carro andou {distancia} km")
        else:
            print("Combustível insuficiente para andar essa distância")

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, litros):
        self.combustivel += litros


meuFusca = Carro(15)

meuFusca.adicionarGasolina(20)
print(f"Combustível atual: {meuFusca.obterGasolina()} litros")

meuFusca.andar(100)

print(f"Combustível restante: {meuFusca.obterGasolina()} litros")