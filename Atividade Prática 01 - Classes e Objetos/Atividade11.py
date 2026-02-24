class Usuario:
  primeiroNome = ""
  sobrenome =""

  def dizer_ola(self):
    return f"Olá, {self.primeiroNome} {self.sobrenome}."

usuario2 = Usuario()    
usuario2.primeiroNome = "Jane"
usuario2.sobrenome = "Silva"
print (usuario2.dizer_ola())