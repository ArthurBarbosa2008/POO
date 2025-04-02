class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.quantidade = quantidade
        
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("Preço Inválido!")
        
# Criação dos produtos  
objeto1 = Produto("Mouse gamer", 60, 3)

# Chamando as funções
print(objeto1.get_nome())
print(objeto1.get_preco())
objeto1.set_nome("Mouse comum")
objeto1.set_preco(50)
print(objeto1.get_nome())
print(objeto1.get_preco())
