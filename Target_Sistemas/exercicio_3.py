import json

# funcao para carregar os dados do arquivo .json
def dados_json(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados

# funcao para calcular os faturamentos
def calcular_faturamento(dados):
    faturamentos = [dia["faturamento"] for dia in dados if dia["faturamento"] > 0]
    
    if not faturamentos:
        print("nao houve faturamento em nenhum dia.")
        return
    
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_da_media = len([f for f in faturamentos if f > media_mensal])
    
    print(f"menor valor de faturamento em um dia do mes: {menor_faturamento}")
    print(f"maior valor de faturamento em um dia do mes: {maior_faturamento}")
    print(f"numero de dias com faturamento acima da media mensal: {dias_acima_da_media}")

# carregando os dados do .json
dados_faturamento = dados_json('faturamento.json')

# calculado a media
calcular_faturamento(dados_faturamento)
