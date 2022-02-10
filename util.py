import pandas as pd

# Simplesmente retorna o numero de registros no dataset
def get_total_records_of_dataset(dataset):
    total_dataset = pd.read_csv(dataset)
    total_dataset.query('stroke == 1 or stroke == 0', inplace = True)
    return len(total_dataset)

# Simplesmente retorna o numero de avcs no dataset
def get_number_of_avcs(dataset):
    num_avc = pd.read_csv(dataset)
    num_avc.query('stroke == 1', inplace = True)
    return len(num_avc)


# Realiza os calculos para gerar a porcentagem que será usada no nós da rede bayesiana
def calcular_porcentagem(entrada, tamanho):
    aux = (entrada * 100) / tamanho
    porcentagem = round(aux/100,2)
    aux2 = 1 - porcentagem
    contraparte = round(aux2,2)
    return porcentagem, contraparte


def get_match_from_query(query,dataset):
    res = pd.read_csv(dataset)
    res.query(query, inplace = True)
    num_matches_linha_tv = len(res)
    return num_matches_linha_tv