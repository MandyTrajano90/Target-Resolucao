# 4 - Programa para faturamento total

faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

def calcular_percentual(faturamento_estado, faturamento_total):
    return (faturamento_estado / faturamento_total) * 100

print("Percentual de representação de cada estado no faturamento total:")
for estado, faturamento in faturamento_por_estado.items():
    percentual = calcular_percentual(faturamento, faturamento_total)
    print(f"{estado}: {percentual:.2f}%")
