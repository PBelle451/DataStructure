def dfs(grafo, inicio, objetivo, visitado=None, caminho=None):
    """
    Implementação recursiva da Busca em Profundidade (DFS).

    Args:
        grafo (dict): Dicionário representando o grafo como lista de adjacências
        inicio (str): Nó inicial da busca
        objetivo (str): Nó que se deseja alcançar
        visitado (set, optional): Conjunto de nós já visitados. Default é None.
        caminho (list, optional): Lista com o caminho percorrido. Default é None.

    Returns:
        list: Caminho do início ao objetivo, ou None se não existir caminho
    """

    # Inicializa o conjunto de visitados na primeira chamada
    if visitado is None:
        visitado = set()

    # Inicializa o caminho na primeira chamada
    if caminho is None:
        caminho = []

    # Marca o nó atual como visitado e adiciona ao caminho
    visitado.add(inicio)
    caminho = caminho + [inicio]

    # Verifica se alcançamos o nó objetivo
    if inicio == objetivo:
        return caminho

    # Explora todos os vizinhos do nó atual
    for vizinho in grafo.get(inicio, []):
        # Se o vizinho não foi visitado, faz uma chamada recursiva
        if vizinho not in visitado:
            novo_caminho = dfs(grafo, vizinho, objetivo, visitado, caminho)

            # Se encontrou um caminho válido, retorna-o
            if novo_caminho:
                return novo_caminho

    # Se nenhum caminho foi encontrado a partir deste nó, retorna None
    return None


# Exemplo de uso
if __name__ == "__main__":
    # Define um grafo como dicionário de adjacências
    # Exemplo:
    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F
    grafo = {
        'A': ['B', 'C'],  # A está conectado a B e C
        'B': ['D', 'E'],  # B está conectado a D e E
        'C': ['F'],  # C está conectado a F
        'D': [],  # D não tem vizinhos
        'E': ['F'],  # E está conectado a F
        'F': []  # F não tem vizinhos
    }

    # Define os nós de início e objetivo da busca
    inicio = 'A'
    objetivo = 'F'

    print(f"DFS de {inicio} para {objetivo}:")

    # Executa a DFS
    caminho = dfs(grafo, inicio, objetivo)

    # Exibe o resultado
    if caminho:
        print(" -> ".join(caminho))
    else:
        print(f"Não há caminho de {inicio} para {objetivo}")