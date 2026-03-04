class Laptop:
    def __init__(self, preco=0):
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

preco1 = Laptop()
print("Preço inicial:", preco1.get_preco())
preco1.set_preco(3999)
print("Novo preço:", preco1.get_preco())