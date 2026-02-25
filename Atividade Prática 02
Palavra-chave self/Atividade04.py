class Usuario():
    primeiroNome = ""
    ultimoNome = ""
    
    def hello(self):
        return "Olá, " + self.primeiroNome + self.ultimoNome

usuario1 = Usuario()
usuario1.primeiroNome = "Jonnie "
usuario1.ultimoNome = "Bravo"

print(usuario1.hello())