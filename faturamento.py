import json

def carregar_faturamento():
    with open('faturamento.json', 'r') as file:
        return json.load(file)

def calcular_estatisticas(faturamento):
    # Filtrar os dias com faturamento maior que zero
    faturamento_filtrado = [dia['valor'] for dia in faturamento if dia['valor'] > 0]
    
    # Calcular o menor e o maior valor de faturamento
    menor_valor = min(faturamento_filtrado)
    maior_valor = max(faturamento_filtrado)
    
    # Calcular a média mensal dos dias com faturamento
    media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)
    
    # Contar os dias em que o faturamento foi superior à média mensal
    dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)
    
    return menor_valor, maior_valor, dias_acima_da_media


faturamento = carregar_faturamento()

# Calcular as estatísticas
menor_valor, maior_valor, dias_acima_da_media = calcular_estatisticas(faturamento)


print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media}")
