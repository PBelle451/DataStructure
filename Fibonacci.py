n1 = 0
n2 = 1
count = 2

#Implementando o algoritmo com loop com recursão
def fibonacci(n1, n2):
    global count
    if count <= 19:
        newFibo = n1 + n2
        print(newFibo)
        n2 = n1
        n1 = newFibo
        count += 1
        fibonacci(n1, n2)
    else:
        return

#Implementando o algoritmo diretamente na função por meio da fórmula
#F(n) = F(n - 1) + F(n - 2)
def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

if __name__ == '__main__':
    fibonacci(1, 0)
    #print(F(19))