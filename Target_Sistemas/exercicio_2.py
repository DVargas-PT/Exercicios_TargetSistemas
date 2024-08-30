def sequencia_fibonacci_ate(n):
    """gera a sequencia de fibonacci ate um valor igual ou maior que n."""

    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def pertence_a_fibonnaci(n):
    """verifica se o numero informado pertence a sequencia de fibonacci."""
    fib_sequence = sequencia_fibonacci_ate(n)
    return n in fib_sequence


# solicita um numero ao usuario
numero = int(input("informe um numero: "))


# calcula se o numero pertence a sequencia de fubonnaci
if pertence_a_fibonnaci(numero):

    print(f"o numero {numero} pertence a sequencia de fibonacci.")
else:
    print(f"o numero {numero} nao pertence a sequencia de fibonacci.")

