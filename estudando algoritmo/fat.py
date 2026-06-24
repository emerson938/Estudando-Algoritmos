def fat(numero):
    if numero == 1:
        return 1
    else:
        return numero * fat(numero - 1)

print(fat(5))
