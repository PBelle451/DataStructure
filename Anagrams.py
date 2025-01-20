# Importa defaultdict para criar um dicionário com listas como valores padrão
from collections import defaultdict


# Função para agrupar palavras que são anagramas
def group_anagrams(strs):
    # Cria um dicionário onde as chaves serão tuplas de letras ordenadas e os valores serão listas de palavras
    anagrams = defaultdict(list)

    # Itera sobre cada palavra na lista de entrada
    for word in strs:
        # Ordena as letras da palavra e usa como chave no dicionário
        # Exemplo: "eat" -> ('a', 'e', 't')
        anagrams[tuple(sorted(word))].append(word)

    # Retorna apenas os valores do dicionário como uma lista de listas
    return list(anagrams.values())


# Bloco principal para execução do código
if __name__ == '__main__':
    array = []  # Inicializa uma lista para armazenar as palavras inseridas pelo usuário

    # Loop para coletar as palavras do usuário
    while True:
        strs = input("Insert anagrams to be sorted [write break to quit]: ")  # Solicita entrada
        if strs == "break":  # Condição para sair do loop
            break
        array.append(strs)  # Adiciona a palavra à lista

    # Chama a função para agrupar os anagramas e imprime o resultado
    print(group_anagrams(array))
