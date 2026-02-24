class Usuario:
  primeiroNome = ""
  sobrenome =""

  def dizer_ola(self):
    return f"Olá, {self.primeiroNome} {self.sobrenome}."

usuario1 = Usuario()  
usuario1.primeiroNome = "Bruna"
usuario1.sobrenome = "Baptista"
print (usuario1.primeiroNome)
print (usuario1.sobrenome)