# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;<br>
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;<br>

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
# •	SP – R$67.836,43 
# •	RJ – R$36.678,66 
# •	MG – R$29.229,88 
# •	ES – R$27.165,48 
# •	Outros – R$19.849,53 

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

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
