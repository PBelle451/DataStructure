# Função para encontrar dois números em um array que somam a um valor alvo
def two_sum(nums, target):
    # Dicionário para armazenar os números já vistos e seus índices
    seen = {}

    # Itera sobre o array, obtendo o índice e o valor de cada elemento
    for i, num in enumerate(nums):
        # Calcula a diferença necessária para atingir o alvo
        diff = target - num

        # Verifica se a diferença já foi vista
        if diff in seen:
            # Se encontrada, retorna os índices do número atual e do número visto anteriormente
            return [seen[diff], i]

        # Se a diferença não foi vista, armazena o número atual com seu índice
        seen[num] = i

    # Retorna uma lista vazia se não houver dois números que somem ao alvo
    return []


# Bloco principal para teste da função
if __name__ == '__main__':
    # Array de números de entrada
    nums = [2, 7, 11, 15]

    # Valor alvo
    target = 9

    # Chama a função e imprime o resultado
    print(two_sum(nums, target))  # Saída esperada: [0, 1]
