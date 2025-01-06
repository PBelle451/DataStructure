def find_max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

def numbers():
    array = []
    while True:
        number = int(input("Please insert the numbers on the array: "))
        if number == -1:
            break
        array.append(number)
    return array

if __name__ == '__main__':
    num_list = numbers()
    print("Maximum number:", find_max(num_list))