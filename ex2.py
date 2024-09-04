# Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5,
# 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma 
# ensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return f'O número {n} pertence a sequência de Fibonacci.'
    else:
        return f'O número {n} não pertence a sequência de Fibonacci.'

print(fibonacci(13))