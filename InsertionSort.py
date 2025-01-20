# Insertionsort in an algorithm where it separates the array into two parts, one where the elementes are sorted and the other are elements yet to be sorted
# The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place in the sorted part of the array, until the array is sorted.
# If the number read on the array is lower than the number read next then it's thrown to the sorted part of the algorithm. This goes until there no more elements to be sorted

myArray = []
while True:
    entry = int(input("Insira um número para inserir no Array: "))
    if entry == -1:
        break
    myArray.append(entry)

n = len(myArray)
for i in range(1,n):
    insert_index = i
    current_value = myArray[i]
    for j in range(i-1, -1, -1):
        if myArray[j] > current_value:
            myArray[j+1] = myArray[j]
            insert_index = j
        else:
            break
    myArray[insert_index] = current_value

print("Array organizado: ", myArray)