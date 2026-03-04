class Usuario:
    def __init__(self, primeiroNome):
        self.__primeiroNome = primeiroNome
    def setPrimeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome
    def getPrimeiroNome(self):
        return self.__primeiroNome
    
usuario1 = Usuario("Joe")
print(usuario1.getPrimeiroNome())