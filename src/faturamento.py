# 3 - Manipulação de arquivo XML
from bs4 import BeautifulSoup
from os import path  

# Função para ler o arquivo XML e retornar os dados de faturamento
def ler_faturamento_xml(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        soup = BeautifulSoup(file, 'lxml')  
    faturamentos = []
    
    for row in soup.find_all('row'):
        valor = row.find('valor').text
        valor = float(valor) 
        if valor > 0:  
            faturamentos.append(valor)
    
    return faturamentos

def menor_faturamento(faturamentos):
    return min(faturamentos)

def maior_faturamento(faturamentos):
    return max(faturamentos)

def media_mensal(faturamentos):
    return sum(faturamentos) / len(faturamentos) if faturamentos else 0

def dias_acima_da_media(faturamentos, media):
    return sum(1 for f in faturamentos if f > media)

# Caminho do arquivo XML
caminho_arquivo = path.join(path.dirname(__file__), 'dados.xml') 
faturamentos = ler_faturamento_xml(caminho_arquivo)

if faturamentos:
    menor = menor_faturamento(faturamentos)
    maior = maior_faturamento(faturamentos)
    media = media_mensal(faturamentos)
    dias_acima = dias_acima_da_media(faturamentos, media)

    print(f"Menor valor de faturamento: {menor:.2f}")
    print(f"Maior valor de faturamento: {maior:.2f}")
    print(f"Média de faturamento mensal: {media:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima}")
else:
    print("Não há dados de faturamento válidos no arquivo.")
