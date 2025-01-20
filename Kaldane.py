# Algoritmo de Kadane para encontrar a soma máxima de uma subarray contígua
# Objetivo: Encontrar a maior soma de elementos consecutivos dentro de um array

def max_subarray(nums):
    # Inicializa as variáveis para rastrear a soma máxima e a soma atual
    max_sum = current_sum = nums[0]  # Começa com o primeiro elemento do array

    # Itera sobre os elementos do array a partir do segundo elemento
    for num in nums[1:]:
        # Atualiza a soma atual:
        # - Se adicionar o número atual resultar em uma soma menor que o próprio número, reinicia a soma
        current_sum = max(num, current_sum + num)

        # Atualiza a soma máxima:
        # - Verifica se a soma atual é maior que a soma máxima registrada
        max_sum = max(max_sum, current_sum)

    # Retorna a maior soma encontrada
    return max_sum


# Bloco principal para testar o algoritmo
if __name__ == '__main__':
    array = []
    while True:
        nums = int(input("Insert here the numbers of the array [type 0 to quit]: "))
        if nums == 0:
            break
        array.append(nums)
    print("Largest sum of the array: ", max_subarray(array))