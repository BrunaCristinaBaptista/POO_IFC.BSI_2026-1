class Empregado():
    def __init__(self, nome="", salario=0, projeto=""):
        self.nome = nome
        self.projeto = projeto
        self.__salario = salario

    def setSalario(self, salario):
        self.__salario = salario

    def trabalho(self):
        return f"{self.nome} está no projeto: {self.projeto}"

    def mostrar(self):
        return f"{self.nome}recebe o seguinte salario: R${self.__salario}"


empregado1 = Empregado("Bruna", 1200, "BSI")    
print(empregado1.trabalho())
print(empregado1.mostrar())