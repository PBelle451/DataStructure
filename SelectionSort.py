# SelectionSort is an algorithm that finds the lowest value in an array and moves it to the front of the array
# The algorithm will read the entire array and read the lowest number in the array, if the current number read is lower than the current lowest, then it's thrown to the beginning of the array
# This process repeats until the array is sorted

myArray = []
while True:
    entry = int(input("Insira um número para inserir no Array: "))
    if entry == -1:
        break
    myArray.append(entry)

n = len(myArray)
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if myArray[j] < myArray[min_index]:
            min_index = j
    myArray[i], myArray[min_index] = myArray[min_index], myArray[i]
print("Sorted array:", myArray)