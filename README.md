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

IMPORTANTE: 
> a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;<br>
> b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;<br>

4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
•	SP – R$67.836,43 
•	RJ – R$36.678,66 
•	MG – R$29.229,88 
•	ES – R$27.165,48 
•	Outros – R$19.849,53 

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

```python

import json

def revenues_by_day(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    revenues = {}
    for entry in data:
        if entry['valor'] == 0.0:
            continue
        day = entry['dia']
        value = entry['valor']
        revenues[day] = value
    
    return revenues

def calculate_percentage_of_revenue(revenues_by_day):
    total_revenue = sum(revenues_by_day.values())
    
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    Outros = 19849.53

    # porcentagem de sp em relação ao total_revenue
    sp_percent = (sp / total_revenue) * 100
    rj_percent = (rj / total_revenue) * 100
    mg_percent = (mg / total_revenue) * 100
    es_percent = (es / total_revenue) * 100
    outros_percent = (Outros / total_revenue) * 100

    print(f'SP: {sp_percent:.2f}%')
    print(f'RJ: {rj_percent:.2f}%')
    print(f'MG: {mg_percent:.2f}%')
    print(f'ES: {es_percent:.2f}%')
    print(f'Outros: {outros_percent:.2f}%')

json_file_path = 'dados.json'
data = revenues_by_day(json_file_path)
calculate_percentage_of_revenue(data)
```

Saída:<br>
SP: 15.48%<br>
RJ: 8.37%<br>
MG: 6.67%<br>
ES: 6.20%<br>
Outros: 4.53%<br>

5) Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: <br>
> a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;<br>
> b) Evite usar funções prontas, como, por exemplo, reverse;<br>

```python
def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

string = input("Digite uma string: ")
print(reverse_string(string))
```