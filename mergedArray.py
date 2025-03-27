def misturar_arrays(array1, array2):
    resultado = []
    i = j = 0

    # Intercala os elementos dos dois arrays, ignorando o valor 0
    while i < len(array1) or j < len(array2):
        # Adiciona elementos de array2, ignorando o 0
        if j < len(array2) and array2[j] != 0:
            resultado.append(array2[j])
            j += 1
        # Adiciona elementos de array1
        if i < len(array1):
            resultado.append(array1[i])
            i += 1

    # Ordena o resultado final
    resultado.sort()

    return resultado


# Entradas
a = [1, 5, 7, 7]
b = [0, 1, 2, 3]

# Mistura os arrays
resultado = misturar_arrays(a, b)

# Imprime a saída no formato desejado
print(", ".join(map(str, resultado)))