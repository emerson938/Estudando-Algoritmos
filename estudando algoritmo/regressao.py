def reduzir(item):
    if (item == 0):
        return 0
    print(item)
    return reduzir(item-1)

print(reduzir(10))