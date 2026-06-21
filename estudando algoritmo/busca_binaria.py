def busca_binaria(lista, item):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) //2
        if lista[meio] == item:
            return "encontrado"
        elif lista[meio] <= item:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

print(busca_binaria([0,1,2,3,4,5,6,7], 9))
