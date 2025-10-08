# Menu da Cláudia | Lista De Compras - Numerando os itens

# Criando uma lista vazia

lista_compras =  []

while True: # usa-se while true quando não tem um numero determinado para repetir tal ação
    produto = input('Digite o nome de um produto ou sair para encerrar: ')

# verificando se o usuario quer sair 
    if produto.lower() == 'sair': # .lower() deixar todas as letras minusculas
        break
# adicionando o produto na lista
    lista_compras.append(produto)

# mostrando a lista atualizada e numerada 
    print('\n ==Lista de Compras==: ')
    for i,item in enumerate(lista_compras, start=1): # para numerar, utiliza-se o comando 'enumerate' | 
        print(f'{i} - {item}')
    