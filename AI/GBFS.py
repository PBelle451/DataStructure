import heapq

def gbfs(grafo, inicio, objetivo, heuristica):
    # grafo (dict): Dicionário representando o grafo como lista e adjacências
    # inicio (str): Nó inicial da busca
    # objetivo (str): Nó objetivo a ser alcançado
    # heuristica (dict): Dicionário com valores heurísticos para cada nó

    # fila prioridade (heap) para nós a serem explorados
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica[inicio], [inicio]))

    # Conjunto para armazenar nós visitados
    visitados = set()
    visitados.add(inicio)

    while fila_prioridade:
        _, caminho = heapq.heappop(fila_prioridade)
        no_atual = caminho[-1]

        # Verifica se alcançamos o objetivo
        if no_atual == objetivo:
            return caminho

        # Explora os vizinhos no nó atual
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                # Adiciona à fila com base na heurística do vizinho
                heapq.heappush(fila_prioridade, (heuristica[vizinho], novo_caminho))

    return None

if __name__ == '__main__':
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Valores heurísticos (estimativa de distância até o objetivo 'F')
    heuristica = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 4,
        'E': 1,
        'F': 0
    }

    inicio = 'A'
    objetivo = 'F'

    print(f"Greedy BFS de {inicio} para {objetivo}:")
    caminho = gbfs(grafo, inicio, objetivo, heuristica)

    if caminho:
        print(" -> ".join(caminho))
    else:
        print(f"Não há caminho de {inicio} para {objetivo}")