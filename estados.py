faturamento_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calcular_percentuais(faturamento_estado):
    # Calcular o valor total de faturamento
    total_faturamento = sum(faturamento_estado.values())
    
    # Calcular o percentual de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento_estado.items()}
    
    return percentuais

percentuais = calcular_percentuais(faturamento_estado)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
