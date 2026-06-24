def soma(lista):
    total = 0
    for i in lista:
        total += i
    return total





def soma(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma(lista[1:])

print(soma([1,2,3,4,5]))