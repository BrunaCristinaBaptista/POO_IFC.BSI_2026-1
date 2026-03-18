class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, largura=0, altura=0, pontoInicial=None):
        self.largura = largura
        self.altura = altura
        self.pontoInicial = pontoInicial


def imprimirPonto(ponto):
    print(f"Ponto: ({ponto.x}, {ponto.y})")


def encontrarCentro(retangulo):
    xCentro = retangulo.pontoInicial.x + (retangulo.largura / 2)
    yCentro = retangulo.pontoInicial.y + (retangulo.altura / 2)
    return Ponto(xCentro, yCentro)


ponto = Ponto(0, 0)
ret = Retangulo(10, 5, ponto)

while True:
    print("\n1 - Alterar valores do retângulo")
    print("2 - Mostrar centro do retângulo")
    print("3 - Mostrar ponto inicial")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        largura = float(input("Digite a largura: "))
        altura = float(input("Digite a altura: "))
        x = float(input("Digite o x do ponto inicial: "))
        y = float(input("Digite o y do ponto inicial: "))

        ret.largura = largura
        ret.altura = altura
        ret.pontoInicial = Ponto(x, y)

    elif opcao == 2:
        centro = encontrarCentro(ret)
        print("Centro do retângulo:")
        imprimirPonto(centro)

    elif opcao == 3:
        print("Ponto inicial:")
        imprimirPonto(ret.pontoInicial)

    elif opcao == 0:
        break

    else:
        print("Opção inválida")