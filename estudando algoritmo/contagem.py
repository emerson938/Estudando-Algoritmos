def contItem(lista):
    if lista == []:
        return 0
    else:
        return 1 + contItem(lista[1:])

print(contItem([1,2,3,4,5]))