from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    ordem = []
    fila = deque([inicio])

    while fila:
        vertice = fila.popleft()

        if vertice not in visitados:
            visitados.add(vertice)
            ordem.append(vertice)

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    fila.append(vizinho)

    return ordem


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

print(bfs(grafo, "A"))