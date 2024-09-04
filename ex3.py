# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
# • O menor valor de faturamento ocorrido em um dia do mês; 
# • O maior valor de faturamento ocorrido em um dia do mês; 
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

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