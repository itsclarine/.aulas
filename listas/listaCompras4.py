# importar sempre no inicio 
# biblioteca.system('cls' if biblioteca.name == 'nt' else 'clear') # limpar e tela 

# Menu da Cláudia | Lista De Compras - Removendo Itens

# importando biblioteca
import os 

# usando def | def = 'caixa' para armazenar uma variável; código mais limpo
def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear') # limpar e tela

# Criando uma lista vazia
lista_compras =  []

while True: # usa-se while true quando não tem um numero determinado para repetir tal ação
    Limpar_Tela()
    
    produto = input('Digite o nome de um produto ou sair para encerrar: ')

# verificando se o usuario quer sair 
    if produto.lower() == 'sair': # .lower() deixar todas as letras minusculas
        break
# adicionando o produto na lista
    lista_compras.append(produto)

# verificando se o usuário quer remover um produto 
    if produto[:8].lower() == 'remover ':
        item_remover = produto[8:].strip()
        if item_remover in lista_compras:
            lista_compras.remove(item_remover)
            print(f'{item_remover} foi removido da lista.')
        else:
            print(f'o produto "{item_remover}" não está na lista.')
    else:
        lista_compras.append(produto)
        print(f' {produto} foi adicionado a lista.')

    input('\n Digite qualquer tecla para continuar...')