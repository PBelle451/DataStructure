def add_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    return total

def multiply_numbers(*args):
    total = 1
    for num in args:
        total = total * num
    return total

total1 = add_numbers(2, 4, 5, 6, 7, 8, 10)
total2 = multiply_numbers(2, 4, 5, 6, 7, 8, 10)
print("\nSum: ", total1)
print("\nMultiplication: ", total2)