# 2 - Sequencia de Fibonacci 
def pertence_fibonacci(num):
    fib1, fib2 = 0, 1
    if num == 0 or num == 1:
        return True
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
    return fib2 == num

numero = input("Informe um número para verificar se pertence à sequência de Fibonacci: ")

try:
    numero = int(numero)
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")