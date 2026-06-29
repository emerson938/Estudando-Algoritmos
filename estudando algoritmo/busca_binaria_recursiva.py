
def busca_binaria(lista, item):
    if len(lista) == 0:
        return -1

    meio = len(lista) //2

    if lista[meio] == item:
        return meio

    if item < lista[meio]:
        return busca_binaria(lista[:meio], item)
    return (busca_binaria(lista[meio + 1:],item))







