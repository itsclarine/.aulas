# criar classes utilizando o polimorfismo 

# LOJA
# p: livros, eletrônico, alimento

class Produto: 
    def __init__(self, preco, nome):
        self.preco = preco 
        self.nome = nome
    def apresentar(self):
        return f'O {self.nome} custa {self.preco}'

class Livro(Produto): 
    def __init__(self,preco,nome,npagina):
        super().__init__(preco,nome)
        self.npagina = npagina
    def apresentar(self):
        return f'O Livro {self.nome} tem {self.npagina} páginas'

class Eletronico(Produto):
    def __init__(self,preco,nome,tamanho):
        super().__init__(preco,nome)
        self.tamanho = tamanho 
    def apresentar(self):
        return f'O eletronico {self.nome} custa {self.preco} e tem tamanho {self.tamanho}'

class Alimento(Produto):
    def __init__(self, preco, nome,tipo):
        super().__init__(preco, nome)
        self.tipo = tipo 
        