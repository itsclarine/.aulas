# Menu da Cláudia | Lista de Compras - Adiciona Itens 

# Criando uma lista vazia

lista_compras =  []

while True: # usa-se while true quando não tem um numero determinado para repetir tal ação
    produto = input('Digite o nome de um produto ou sair para encerrar: ')

# verificando se o usuario quer sair 
    if produto.lower() == 'sair': # .lower() deixar todas as letras minusculas
        break
# adicionando o produto na lista
    lista_compras.append(produto)

# mostrando a lista atualizada 
    print('\n Lista de Compras: ')
    for item in lista_compras:
        print(f' - {item}')
