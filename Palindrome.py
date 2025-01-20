# Função para verificar se uma string é um palíndromo
def is_palindrome(s):
    # Remove caracteres não alfanuméricos e converte tudo para minúsculo
    s = ''.join(c.lower() for c in s if c.isalnum())
    # Verifica se a string processada é igual à sua reversa
    return s == s[::-1]

# Bloco principal para executar a verificação
if __name__ == '__main__':
    # Solicita ao usuário que insira uma string
    s = input("Please insert a string and check if it's Palindrome or not: ")
    # Verifica se a string é um palíndromo e exibe o resultado
    print(is_palindrome(s))
