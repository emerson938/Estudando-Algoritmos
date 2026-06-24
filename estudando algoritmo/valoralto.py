def valor_alto(lista):
    #utilizando for
    maior = lista[0]
    for i in lista[1:]:
        if i > maior:
            maior = i
    return maior

def valor_alto2(lista):
    #utilizando recursividade
    if len(lista) == 1:
        return lista[0]

    maior_resto = valor_alto2(lista[1:])

    if lista[0] > maior_resto:
        return lista[0]
    else:
        return maior_resto


print(valor_alto2([1,2,3]))