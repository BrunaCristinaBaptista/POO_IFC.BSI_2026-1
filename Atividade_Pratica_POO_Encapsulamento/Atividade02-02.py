class Usuario:
	def __init__(self, primeiroNome=""):
		self.__primeiroNome = primeiroNome

	def setPrimeiroNome(self, primeiroNome):
		usuariosPermitidos = ["Joe"]
		if primeiroNome in usuariosPermitidos:
			self.__primeiroNome = primeiroNome
		else:
			self.__primeiroNome = "Usuário não permitido."

	def getPrimeiroNome(self):
		return "O primeiro nome do usuário é " + self.__primeiroNome


usuario1 = Usuario("Joe")
print(usuario1.getPrimeiroNome())
