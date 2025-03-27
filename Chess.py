class Peca:
    def __init__(self, tipo, cor):
        self.tipo = tipo
        self.cor = cor

    def __repr__(self):
        return f"{self.cor[0]}{self.tipo[0]}"

# Classe do tabuleiro
class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.inicializar_tabuleiro()

    def inicializar_tabuleiro(self):
        # Peças brancas
        self.tabuleiro[0] = [
            Peca("Torre", "Branco"), Peca("Cavalo", "Branco"), Peca("Bispo", "Branco"), Peca("Rainha", "Branco"),
            Peca("Rei", "Branco"), Peca("Bispo", "Branco"), Peca("Cavalo", "Branco"), Peca("Torre", "Branco")
        ]
        self.tabuleiro[1] = [Peca("Peao", "Branco") for _ in range(8)]

        # Peças Pretas
        self.tabuleiro[6] = [Peca("Peao", "Preto") for _ in range(8)]
        self.tabuleiro[7] = [
            Peca("Torre", "Preta"), Peca("Cavalo", "Preto"), Peca("Bispo", "Preto"), Peca("Rainha", "Preto"),
            Peca("Rei", "Preto"), Peca("Bispo", "Preto"), Peca("Cavalo", "Preto"), Peca("Torre", "Preto")
        ]

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(linha)

    def mover_peca(self, inicio, fim):
        x1, y1 = inicio
        x2, y2 = fim
        peca = self.tabuleiro[x1][y1]
        if peca is None:
            print("Movimento inválido: não há peça na posição inicial")
            return False

        if self.tabuleiro[x2][y2] is not None and self.tabuleiro[x2][y2].cor == peca.cor:
            print("Movimento inválido: não se pode capturar a própria peça.")
            return False

        self.tabuleiro[x2][y2] = peca
        self.tabuleiro[x1][x2] = None
        return True

class JogoXadrez:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.turno = "Branco"

    def jogar(self):
        while True:
            self.tabuleiro.mostrar_tabuleiro()
            print(f"Turno do {self.turno}")
            inicio = input("Digite a posição inicial (x y): ").split()
            fim = input("Digite a posição final (x y): ").split()
            inicio = tuple(map(int, inicio))
            fim = tuple(map(int, fim))

            if self.tabuleiro.mover_peca(inicio, fim):
                self.turno = "Preto" if self.turno == "Branco" else "Branco"
            else:
                print("Movimento inválido, tente novamente")

if __name__ == '__main__':
    jogo = JogoXadrez()
    jogo.jogar()