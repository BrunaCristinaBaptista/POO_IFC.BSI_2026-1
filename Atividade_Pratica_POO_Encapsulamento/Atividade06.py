class Pessoa:
    def __init__(self, primeiroNome="", ultimoNome=""):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def getPrimeiroNome(self):
        return self.__primeiroNome
    def getUltimoNome(self):
        return self.__ultimoNome
        
    def setPrimeiroNome(self, primeiroNome=""):
        self.__primeiroNome = primeiroNome
    def setUltimoNome(self, ultimoNome=""):
        self.__ultimoNome = ultimoNome

pessoa1 = Pessoa("João", "Carvalho")
print("Primeiro Nome:", pessoa1.getPrimeiroNome())
print("Último Nome:", pessoa1.getUltimoNome())