import heapq  # Importa a biblioteca heapq para manipulação de heaps

# Função para encontrar o k-ésimo maior elemento em um array
def find_kth_largest(nums, k):
    # Usa heapq.nlargest para obter os k maiores elementos do array
    # Retorna o último elemento da lista resultante (o k-és imo maior)
    return heapq.nlargest(k, nums)[-1]

if __name__ == '__main__':
    # Array de entrada
    array = []
    while True:
        nums = int(input("Insert here the numbers of the array [type -1 to quit]: "))
        if nums == -1:
            break
        array.append(nums)
    k = int(input("What element in the array do you want to find?: "))
    print(f"Array: {array}")
    print(find_kth_largest(array, k))