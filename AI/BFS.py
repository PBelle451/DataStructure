from collections import deque

def bfs(grafo, inicio, objetivo):
    # grafo (dict): Dicionário representando o grafo como lista de adjacências
    # inicio (str): Nó inicial da busca
    # objetivo (str): No que deseja alcançar

    # Fila para armazenar os nós a serem visitados, junto com seus caminhos
    fila = deque()
    fila.append([inicio])

    # Conjunto para armazenar os nós já visitados
    visitados = set()
    visitados.add(inicio)

    while fila:
        # Pega o primeiro caminho da fila
        caminho = fila.popleft()
        # Pega o último nó do caminho
        no = caminho[-1]

        # Verifica se alcançamos o nó objetivo
        if no == objetivo:
            return caminho

        # Explora todos os vizinhos do nó atual
        for vizinho in grafo.get(no, []):
            if vizinho not in visitados:
                # Marca como visitados
                visitados.add(vizinho)
                # Cria um caminho adicionando o vizinho
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                # Adiciona o novo caminho nda fila
                fila.append(novo_caminho)
    return None

if __name__ == '__main__':
    # Define o grafo
    grafo = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    inicio = 'A'
    objetivo = 'F'

    print(f"BFS de {inicio} para {objetivo}:")
    caminho = bfs(grafo, inicio, objetivo)

    if caminho:
        print(" -> ".join(caminho))
    else:
        print(f"Não há caminho de {inicio} para {objetivo}")