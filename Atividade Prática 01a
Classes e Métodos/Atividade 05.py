class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def mostrarDados(self):
        return f"Conta: {self.numeroConta}, Nome: {self.nomeCorrentista}, Saldo: {self.saldo}"


# Programa principal
conta = ContaCorrente(12345, "João")

print(conta.mostrarDados())

conta.deposito(500)
print(f"Após depósito: {conta.saldo}")

conta.saque(200)
print(f"Após saque: {conta.saldo}")

conta.alterarNome("Maria")
print(conta.mostrarDados())