

# criando a função
def pesquisa_binaria(lista, item):
    baixo = 0
#Definindo o que o valor mais alto será o tamanho da lista - 1
    alto = len(lista) - 1
#Aqui nós definimos o meio e que o chute vai ser sempre o meio da lista
    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        # se o chute for o item que estamos procurando, retornamos o meio
        if chute == item:
            return meio
        # se o chute for maior que o item, descartamos a metade superior da lista e definimos o alto - 1 como novo meio
        if chute > item:
            alto = meio - 1
            print('Chute maior que o item.')
        else:
            print('Chute menor que o item.')
            baixo = meio + 1
            
    print('Não encontrei o item!')
    return None

minha_lista = [1,2,3,4,5,6,7,8,9,10]

print(pesquisa_binaria(minha_lista, 6))



