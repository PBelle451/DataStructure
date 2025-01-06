# Bubblesort is an algorithm that sorts an array from lowest to highest value
# It reads all the numbers on the array, comparing them to the next value
# If it's lower, then it jumps to the next value, if it's higher it's thrown next to it's highest value or if it's the highest value it's thrown to the end of the array

myArray = []
while True:
    entry = int(input("Insira um número para inserir no Array: "))
    if entry == -1:
        break
    myArray.append(entry)
n = len(myArray)    # Reads the size of the array

# Reads the values from the array and sorts them into the algorithm
for i  in range(n-1):
    # This one reads the numbers in the array and throws them in the algorithm
    for j in range(n-i-1):
        # Reads if said number read is higher than the next one in the array
        if myArray[j] > myArray[j+1]:
            # If it's higher, then it's sent to the next
            myArray[j], myArray[j+1] = myArray[j+1], myArray[j]
print("Sorted array: ", myArray)