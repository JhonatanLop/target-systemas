# target-systemas
Repositório dedicado a desafios técnicos do processo seletivo da empresa Target Systemas


1)	Exercício 1
Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0; 
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA); 
Ao final do processamento, qual será o valor da variável SOMA? 

```python
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)
# 91
```

2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

```python
def fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return f'O número {n} pertence a sequência de Fibonacci.'
    else:
        return f'O número {n} não pertence a sequência de Fibonacci.'

print(fibonacci(13))
# O número 13 pertence a sequência de Fibonacci.
```

3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
• O menor valor de faturamento ocorrido em um dia do mês; 
• O maior valor de faturamento ocorrido em um dia do mês; 
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

```python
def find_min_max_and_days_above_average(daily_revenues):
    min_revenue = min(daily_revenues)
    max_revenue = max(daily_revenues)
    average_revenue = sum(daily_revenues) / len(daily_revenues)
    days_above_average = len([revenue for revenue in daily_revenues if revenue > average_revenue])
    return min_revenue, max_revenue, days_above_average

daily_revenues = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
min_revenue, max_revenue, days_above_average = find_min_max_and_days_above_average(daily_revenues)
print(f"Menor valor: {min_revenue}")
print(f"Maior valor: {max_revenue}")
print(f"Número de dias acima da média: {days_above_average}")
# Menor valor: 100
# Maior valor: 1000
# Número de dias acima da média: 5
```
