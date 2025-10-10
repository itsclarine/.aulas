class Esporte: 
    def __init__(self,nome,uniforme):
        self.nome = nome
        self.uniforme = uniforme
    def apresentar(self):
        return f'O {self.nome} usa  {self.uniforme}'
    
class Volei(Esporte):
    def __init__(self,nome,uniforme,posicao):
        super().__init__(nome,uniforme)
        self.posicao = posicao
    def apresentar(self):
        return f'A {self.nome} usa {self.uniforme} e tem as posições {self.posicao}'
    
esporte1 = Esporte('Golden State', 'uniforme branco')
print(esporte1.apresentar())

posicaos = ['Líbero', 'Oposto', 'Ponteiro', 'Central', 'Levantador']
voley = Volei('Seleção Brasileira','Uniforme Azul' , posicaos)
print(voley.apresentar())