class bombaCombustivel:
    def __init__(self, tipoCombustivel="", valorLitro=0, quantidadeCombustivel=0):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"Foram abastecidos {litros} litros")
        else:
            print("Não há combustível suficiente na bomba")

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print(f"Valor a pagar: R$ {valor}")
        else:
            print("Não há combustível suficiente na bomba")

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, quantidade):
        self.quantidadeCombustivel = quantidade

    def mostrarDados(self):
        return f"Combustível: {self.tipoCombustivel}, Valor/Litro: {self.valorLitro}, Quantidade: {self.quantidadeCombustivel}"


# Programa principal
bomba = bombaCombustivel("Gasolina", 5.50, 1000)

print(bomba.mostrarDados())

valor = float(input("Digite o valor para abastecer: "))
bomba.abastecerPorValor(valor)

litros = float(input("Digite a quantidade de litros: "))
bomba.abastecerPorLitro(litros)

print("Após abastecimentos:")
print(bomba.mostrarDados())