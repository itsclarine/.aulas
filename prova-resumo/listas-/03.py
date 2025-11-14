# criando menu simples | + lista + enumerate + remover item 

# criando lista 
lista = []
opcao = 0

# menu
while opcao != '4':
    print('-----menu-----')
    print('1---adicionar item')
    print('2---remover item')
    print('3---ver lista')
    print('4---sair')

    opcao = input('digite uma opção: ')

    if opcao == '1': 
        item_ = input('digite um item para adicionar: ')
        lista.append(item_)
        print(lista)
    elif opcao == '2':
        item_ = input('digite um item para remover: ')
        if item_ in lista:
            lista.remove(item_)
        else:
            print('produto não encontrado! tente novamente!')
    elif opcao == '3':
        print(lista)
    elif opcao == '4':
        print('saindo')
        break
    else:
        print('opcao inválida! tente novamente!')