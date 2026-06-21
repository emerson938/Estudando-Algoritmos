def buscar_menor(lista):
    menor = lista[0]
    indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return indice
