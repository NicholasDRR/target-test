# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  


revenue_by_state = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Others": 19849.53
}

total_revenue = sum(revenue_by_state.values())

for state, revenue in revenue_by_state.items():
    percentage = (revenue / total_revenue) * 100
    print(f"{state} - R$ {revenue:.2f} - {percentage:.2f}% of the total")
