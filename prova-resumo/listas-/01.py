# criando um menu simples | + lista 

# criando lista e definindo opções como 0 - 
lista = []
opcoes = 0

# while | tabela de opções
while opcoes != '4':
    print('===MENU===')
    print('| 1: ADICIONAR ITEM NA LISTA ')
    print('| 2: REMOVER ITEM DA LISTA')
    print('| 3: VER LISTA')
    print('| 4: SAIR')

# solicitando ao usuário 
    opcoes = input('Digite uma opção: ')

# verificando opções
    if opcoes == '1':
        item_ = input('Digite o item para adiciona-lo na lista: ')
        lista.append(item_)
        print(lista)
    elif opcoes == '2':
        item_ = input('Digite o item para remove-lo da lista: ')
        lista.pop(item_)
        print(lista)
    elif opcoes == '3':
        print(lista)
    elif opcoes == '4':
        print('saindo...')
        break 
    else:
        print('opção inválida! tente novamente')