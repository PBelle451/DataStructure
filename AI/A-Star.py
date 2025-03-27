import heapq


def a_star(grafo, inicio, objetivo, heuristica, custo):
    """
    Implementação do algoritmo A* para busca de caminhos.

    Args:
        grafo (dict): Grafo representado como dicionário de adjacências
        inicio (str): Nó de partida
        objetivo (str): Nó objetivo
        heuristica (dict): Valores heurísticos para cada nó (estimativa para o objetivo)
        custo (dict): Dicionário de dicionários com custos entre nós conectados

    Returns:
        tuple: (caminho como lista, custo total) ou (None, 0) se não encontrar
    """

    # Fila de prioridade: (f_score, g_score, nó, caminho)
    fila = []
    heapq.heappush(fila, (heuristica[inicio], 0, inicio, [inicio]))

    # Dicionário para registrar o melhor custo conhecido para cada nó
    g_scores = {inicio: 0}

    while fila:
        _, g_score_atual, no_atual, caminho = heapq.heappop(fila)

        if no_atual == objetivo:
            return caminho, g_score_atual

        for vizinho in grafo[no_atual]:
            # Calcula o custo acumulado até o vizinho
            custo_tentativo = g_score_atual + custo[no_atual][vizinho]

            # Se encontrou um caminho melhor para este vizinho
            if vizinho not in g_scores or custo_tentativo < g_scores[vizinho]:
                g_scores[vizinho] = custo_tentativo
                f_score = custo_tentativo + heuristica[vizinho]
                novo_caminho = caminho + [vizinho]
                heapq.heappush(fila, (f_score, custo_tentativo, vizinho, novo_caminho))

    return (None, 0)  # Não encontrou caminho


# Exemplo de uso
if __name__ == "__main__":
    # Grafo de exemplo
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Custo entre os nós (matriz de adjacências com pesos)
    custo = {
        'A': {'B': 1, 'C': 3},
        'B': {'D': 5, 'E': 2},
        'C': {'F': 2},
        'D': {},
        'E': {'F': 1},
        'F': {}
    }

    # Heurística (distância estimada até F)
    heuristica = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 2,
        'E': 1,
        'F': 0
    }

    inicio = 'A'
    objetivo = 'F'

    print(f"A* search de {inicio} para {objetivo}:")
    caminho, custo_total = a_star(grafo, inicio, objetivo, heuristica, custo)

    if caminho:
        print("Caminho encontrado:", " -> ".join(caminho))
        print(f"Custo total: {custo_total}")
    else:
        print(f"Não há caminho de {inicio} para {objetivo}")