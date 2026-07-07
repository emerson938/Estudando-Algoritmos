# Cria uma fila vazia
fila = []

# Enfileirar (adicionar ao final)
fila.append("Ana")
fila.append("Bruno")
fila.append("Carlos")

print(fila)

# Desenfileirar (remover o primeiro)
primeiro = fila.pop(0)

print("Saiu da fila:", primeiro)
print("Fila:", fila)