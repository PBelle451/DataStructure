def minimax(estado, profundidade, maximizando, jogador, oponente, avaliar_estado, gerar_movimentos, alpha=float('-inf'),
            beta=float('inf')):
    """
    Implementação do algoritmo Minimax com poda Alpha-Beta.

    Args:
        estado: Estado atual do jogo
        profundidade (int): Profundidade máxima da busca
        maximizando (bool): True se é a vez do jogador maximizador
        jogador: Identificador do jogador maximizador
        oponente: Identificador do jogador minimizador
        avaliar_estado (function): Função que avalia um estado do jogo
        gerar_movimentos (function): Função que gera movimentos possíveis
        alpha: Valor alpha para poda
        beta: Valor beta para poda

    Returns:
        tuple: (valor do estado, melhor movimento)
    """
    if profundidade == 0 or estado.terminou():
        return avaliar_estado(estado, jogador), None

    if maximizando:
        valor = float('-inf')
        melhor_movimento = None

        for movimento in gerar_movimentos(estado, jogador):
            novo_estado = estado.fazer_movimento(movimento, jogador)
            novo_valor, _ = minimax(novo_estado, profundidade - 1, False, jogador, oponente, avaliar_estado,
                                    gerar_movimentos, alpha, beta)

            if novo_valor > valor:
                valor = novo_valor
                melhor_movimento = movimento

            alpha = max(alpha, valor)
            if beta <= alpha:
                break  # Poda beta

        return valor, melhor_movimento
    else:
        valor = float('inf')
        melhor_movimento = None

        for movimento in gerar_movimentos(estado, oponente):
            novo_estado = estado.fazer_movimento(movimento, oponente)
            novo_valor, _ = minimax(novo_estado, profundidade - 1, True, jogador, oponente, avaliar_estado,
                                    gerar_movimentos, alpha, beta)

            if novo_valor < valor:
                valor = novo_valor
                melhor_movimento = movimento

            beta = min(beta, valor)
            if beta <= alpha:
                break  # Poda alpha

        return valor, melhor_movimento


# Exemplo de uso para o Jogo da Velha
if __name__ == "__main__":
    class JogoDaVelha:
        def __init__(self):
            self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
            self.vencedor = None

        def terminou(self):
            # Verifica linhas
            for linha in self.tabuleiro:
                if linha[0] == linha[1] == linha[2] != ' ':
                    self.vencedor = linha[0]
                    return True

            # Verifica colunas
            for col in range(3):
                if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != ' ':
                    self.vencedor = self.tabuleiro[0][col]
                    return True

            # Verifica diagonais
            if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != ' ':
                self.vencedor = self.tabuleiro[0][0]
                return True
            if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != ' ':
                self.vencedor = self.tabuleiro[0][2]
                return True

            # Verifica empate
            return all(self.tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

        def fazer_movimento(self, movimento, jogador):
            novo_estado = JogoDaVelha()
            novo_estado.tabuleiro = [linha.copy() for linha in self.tabuleiro]
            i, j = movimento
            novo_estado.tabuleiro[i][j] = jogador
            return novo_estado

        def __str__(self):
            return "\n".join(["|".join(linha) for linha in self.tabuleiro]) + "\n"


    def avaliar_estado(estado, jogador):
        if estado.vencedor == jogador:
            return 10
        elif estado.vencedor is not None:
            return -10
        else:
            return 0


    def gerar_movimentos(estado, jogador):
        movimentos = []
        for i in range(3):
            for j in range(3):
                if estado.tabuleiro[i][j] == ' ':
                    movimentos.append((i, j))
        return movimentos


    # Testando o algoritmo
    jogo = JogoDaVelha()
    jogador = 'X'
    oponente = 'O'

    print("Tabuleiro inicial:")
    print(jogo)

    # Jogada do computador (X)
    _, movimento = minimax(jogo, 3, True, jogador, oponente, avaliar_estado, gerar_movimentos)
    jogo = jogo.fazer_movimento(movimento, jogador)

    print(f"Jogada do computador ({jogador}):")
    print(jogo)

    # Jogada do oponente (O) - simulando jogada humana
    jogo = jogo.fazer_movimento((0, 1), oponente)

    print(f"Jogada do oponente ({oponente}):")
    print(jogo)

    # Jogada do computador (X) novamente
    _, movimento = minimax(jogo, 3, True, jogador, oponente, avaliar_estado, gerar_movimentos)
    jogo = jogo.fazer_movimento(movimento, jogador)

    print(f"Jogada do computador ({jogador}):")
    print(jogo)