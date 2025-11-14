# criando um menu simples | // + limpar tela 

# importando biblioteca 

import os 

# criando def 
def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# criando lista 
lista = []
opcao = 0

# while...
while True:
    print('==MENU==')
    print('1| Adicionar item')
    print('2| Remover item')
    print('3| Ver lista ')
    print('4| sair')

    opcao = input('digite uma opcao: ')

    if opcao == '1': 
        item = input('digite um item para adiciona-lo a lista: ')
        lista.append(item)
        print(lista)
    elif opcao == '2': 
        item = input('digite um item para remove-lo da lista: ')
        if item in lista:
            lista.remove(item)
            print(lista)
        else:
            print('item não encontrado. tente novamente!')
    elif opcao == '3':
        print(lista)
    elif opcao == '4': 
        print('saindo...')
        break
    else: 
        print('opcao invalida. tente novamente!')

    input('\n pressione ENTER para continuar....')
    Limpar_Tela()