def buscar_menor(lista):
    menor = lista[0]
    indice = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            indice = i
    return indice

def ordenacao_selecao(lista):
    novoArra = []
    for i in range(len(lista)):
        menor = buscar_menor(lista)
        novoArra.append(lista.pop(menor) )
    return novoArra

print(ordenacao_selecao([34,67,21,67]))
