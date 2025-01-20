# Classe que define um nó em uma lista ligada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # Valor armazenado no nó
        self.next = next  # Pont                                                    eiro para o próximo nó na lista

# Função para reordenar a lista ligada
def reorder_list(head):
    # Se a lista estiver vazia ou tiver apenas um elemento, não há nada a reordenar
    if not head:
        return

    # Passo 1: Encontrar o meio da lista
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next  # Avança um nó por vez
        fast = fast.next.next  # Avança dois nós por vez

    # Passo 2: Reverter a segunda metade da lista
    prev, curr = None, slow.next  # `slow.next` é o início da segunda metade
    slow.next = None  # Desconecta a primeira metade da segunda
    while curr:
        temp = curr.next  # Armazena o próximo nó
        curr.next = prev  # Inverte o ponteiro do nó atual
        prev = curr  # Avança o ponteiro `prev`
        curr = temp  # Avança para o próximo nó

    # Passo 3: Intercalar as duas metades da lista
    first, second = head, prev  # `head` é o início da primeira metade; `prev` é o início da segunda
    while second:  # Continua enquanto houver elementos na segunda metade
        temp1, temp2 = first.next, second.next  # Armazena os próximos nós
        first.next = second  # Conecta um nó da primeira metade com um da segunda-
        second.next = temp1  # Conecta o nó da segunda metade com o próximo da primeira
        first, second = temp1, temp2  # Avança ambos os ponteiros

# Bloco principal para teste da função
if __name__ == '__main__':
    # Criação de uma lista ligada: 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    # Chama a função para reordenar a lista
    reorder_list(head)

    # Imprime a lista reordenada
    while head:
        print(head.val, end=" -> ")  # Saída esperada: 1 -> 4 -> 2 -> 3 ->
        head = head.next
