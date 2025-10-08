# Fazer menu de compras usando lista // novos comandos

lista = []
opcoes = 0 

while opcoes != '4':
    print('===LISTA DE COMPRAS==')
    print('| 1 - ADICIONAR ITEM     |')
    print('| 2 - REMOVER ITEM       |')
    print('| 3 - VER LISTA          |')
    print('| 4 - SAIR               |')
    print('======')

# solicitando opção ao usuário 
    opcoes = input('Digite uma opção: ')

# opções 
    if opcoes == '1': 
        compre = input('Digite um item para adicionar a lista: ')
        lista.append(compre)
        print(lista)
    elif opcoes == '2':
        compre = input('Digite um item para remover: ')
        lista.pop()
        print(lista)
    elif opcoes == '3':
        print(lista)
    elif opcoes == '4':
        print('saindo')
    else:
        print('opção inválida! tente novamente!')
