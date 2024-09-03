# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


import json

def calculate_revenue(daily_revenue):
    valid_revenues = [day['value'] for day in daily_revenue if day['value'] > 0]
    min_revenue = min(valid_revenues)
    max_revenue = max(valid_revenues)
    monthly_average = sum(valid_revenues) / len(valid_revenues)

    days_above_average = len([value for value in valid_revenues if value > monthly_average])
    return min_revenue, max_revenue, days_above_average

def main():
    with open('ex3.json', 'r') as file:
        data = json.load(file)
    daily_revenue = data['daily_revenue']
    min_revenue, max_revenue, days_above_average = calculate_revenue(daily_revenue)
    
    print(f"Minimum revenue on a single day of the month: R$ {min_revenue:.2f}")
    print(f"Maximum revenue on a single day of the month: R$ {max_revenue:.2f}")
    print(f"Number of days with revenue above the monthly average: {days_above_average}")

if __name__ == "__main__":
    main()
