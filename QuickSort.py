# The Quicksort algorithm is an algorithm that chooses an element in the array as the "pivot"
# The values are sorted as lower or higher than the pivot until the array is sorted
# Any value can be chosen as the pivot but it's generally the last one

def partition(array, low, high):
    pivot = array[high] # Pivot is the highest value in the array
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1
        # If the array has

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

if __name__ == '__main__':
    myArray = []
    while True:
        entry = int(input("Insira um número para inserir no Array: "))
        if entry == -1:
            break
        myArray.append(entry)
    n = len(myArray)
    quicksort(myArray)
    print("Sorted array:", myArray)
