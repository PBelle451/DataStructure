def findLowestValue():
    my_array = []
    while True:
        entry = int(input("Insira um número para inserir no Array: "))
        if entry == -1:
            break
        my_array.append(entry)
    minVal = my_array[0]

    for i in my_array:
        if i < minVal:
            minVal = i
    print("Lowest value: ", minVal)

if __name__ == '__main__':
    findLowestValue()
