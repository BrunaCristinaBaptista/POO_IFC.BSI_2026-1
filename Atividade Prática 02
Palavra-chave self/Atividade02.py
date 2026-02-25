class Usuario():
    primeiroNome = ""
    ultimoNome = ""
    
    def hello(self):
        return "Olá, " + self.primeiroNome

usuario1 = Usuario()
usuario1.primeiroNome = "Bruna Cristina "
usuario1.ultimoNome = "Baptista"

print(usuario1.hello())