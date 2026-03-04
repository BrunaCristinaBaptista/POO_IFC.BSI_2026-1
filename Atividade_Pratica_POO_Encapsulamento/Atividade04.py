class Robo():
    def __init__(self, nome="", ano_construcao=0):
        self.__nome = nome
        self.__ano_construcao = ano_construcao
    def setDiga_alo(self, nome, ano_construcao):
        self.__nome = nome
        self.__ano_construcao = ano_construcao
    def getDiga_alo(self):
        return f"O nome do Robô é {self.__nome} e seu ano de contrução é {self.__ano_construcao}"
    
robo1 = Robo("Aroldo", 2026)
print(robo1.getDiga_alo())

