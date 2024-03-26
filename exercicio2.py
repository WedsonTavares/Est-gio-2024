def fibonacci_sequence(n):
    # Inicializa a sequência de Fibonacci com os dois primeiros valores
    fibonacci = [0, 1]

    # Calcula os valores seguintes da sequência até atingir ou ultrapassar o número informado
    while fibonacci[-1] < n:
        next_number = fibonacci[-1] + fibonacci[-2]  # Próximo número é a soma dos dois últimos
        fibonacci.append(next_number)

    # Verifica se o número informado está na sequência de Fibonacci
    if n in fibonacci:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Número para verificar se pertence à sequência de Fibonacci
numero = int(input("Informe um número: "))

# Chamada da função para verificar se o número está na sequência de Fibonacci
resultado = fibonacci_sequence(numero)

# Imprime o resultado
print(resultado)
