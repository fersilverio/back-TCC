import pandas as pd
from pprint import pprint
from variaveis import *
from queries import *

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

#Realiza as queries sem considerar o caso de AVC (mesmas queries sem os 'and stroke = 1')
def get_numeros_dataset(dataset):
    
    dados = []

    ################# DADOS COM RELAÇÃO AO GÊNERO ###########################################
    # Número de homens no dataset
    male = pd.read_csv(dataset)
    male.query('gender == "Male"', inplace = True)
    homens = len(male)
    dados.append(homens)

    ################# DADOS COM RELAÇÃO A HIPERTENSÃO ###########################################
    hypertension = pd.read_csv(dataset)
    hypertension.query('hypertension == 1', inplace = True)
    num_hiper = len(hypertension)
    dados.append(num_hiper)

    ################# DADOS COM RELAÇÃO A DOENÇA CARDÍACA ###########################################
    heart_disease = pd.read_csv(dataset)
    heart_disease.query('heart_disease == 1', inplace = True)
    num_doenca_cardiaca = len(heart_disease)
    dados.append(num_doenca_cardiaca)

    ################# DADOS COM RELAÇÃO A TABAGISMO ###########################################
    
    #Fuma ou Já fumou
    smokes = pd.read_csv(dataset)
    smokes.query('smoking_status == "smokes"', inplace = True)
    num_fumantes = len(smokes)
    formerly_smoked = pd.read_csv(dataset)
    formerly_smoked.query('smoking_status == "formerly smoked"', inplace = True)
    num_ja_fumaram = len(formerly_smoked)
    num_fumam_ja_fumaram = num_fumantes + num_ja_fumaram
    dados.append(num_fumam_ja_fumaram)

    ################# DADOS COM RELAÇÃO A IMC ###########################################
    
    # #Abaixo do peso ou ideal Masc.
    # abaixo_masc = pd.read_csv(dataset)
    # abaixo_masc.query('(bmi < 20.7 and gender == "Male")', inplace = True)
    # num_abaixo_masc = len(abaixo_masc)
    # ideal_masc = pd.read_csv(dataset)
    # ideal_masc.query('(bmi >= 20.7 and bmi <= 26.4 and gender == "Male")', inplace = True)
    # num_ideal_masc = len(ideal_masc)
    # num_abaixo_ideal_masc = num_abaixo_masc + num_ideal_masc
    # dados.append(num_abaixo_ideal_masc)

    #Abaixo do peso ou ideal Masc.
    abaixo = pd.read_csv(dataset)
    abaixo.query('(bmi < 19.9)', inplace = True)
    num_abaixo = len(abaixo)
    ideal = pd.read_csv(dataset)
    ideal.query('(bmi >= 19.9 and bmi <= 26.1)', inplace = True)
    num_ideal = len(ideal)
    num_abaixo_ideal = num_abaixo + num_ideal
    dados.append(num_abaixo_ideal)






    # #Abaixo do peso ou Peso ideal Fem.
    # abaixo_fem = pd.read_csv(dataset)
    # abaixo_fem.query('(bmi < 19.1 and gender == "Female")', inplace = True)
    # num_abaixo_fem = len(abaixo_fem)
    # ideal_fem = pd.read_csv(dataset)
    # ideal_fem.query('(bmi >= 19.1 and bmi <= 25.8 and gender == "Female")', inplace = True)
    # num_ideal_fem = len(ideal_fem)
    # num_abaixo_ideal_fem = num_abaixo_fem + num_ideal_fem
    # dados.append(num_abaixo_ideal_fem)

    ################# DADOS COM RELAÇÃO A GLICOSE ###########################################

    #Hipoglicemia e Glicemia normal
    
    glicemia_normal = pd.read_csv(dataset)
    glicemia_normal.query('(avg_glucose_level < 99)', inplace = True)
    num_glicemia_normal = len(glicemia_normal)
    hipoglicemia = pd.read_csv(dataset)
    hipoglicemia.query('(avg_glucose_level <= 70)', inplace = True)
    num_hipoglicemia = len(hipoglicemia)
    num_hipo_normal = num_hipoglicemia + num_glicemia_normal
    dados.append(num_hipo_normal)

    ################# DADOS COM RELAÇÃO A IDADE ###########################################
    
    #Jovens e Adultos
    jovens = pd.read_csv(dataset)
    jovens.query('(age <= 19)', inplace = True)
    num_jovens = len(jovens)
    adultos = pd.read_csv(dataset)
    adultos.query('(age >= 20 and age <= 59)', inplace = True)
    num_adultos = len(adultos)
    num_jovens_adultos = num_jovens + num_adultos
    dados.append(num_jovens_adultos)

    return dados



def get_match_from_query(query,dataset):
    res = pd.read_csv(dataset)
    res.query(query, inplace = True)
    num_matches_linha_tv = len(res)
    return num_matches_linha_tv


#Realiza as queries considerando os casos de AVC, vai contar todas as queries da tabela-verdade
def get_numeros_dataset_avc(dataset):
    dados = []
    a = teste()
    v1,v2 = get_match_from_query(a[0],dataset),get_match_from_query(a[1],dataset)
    b = []
    b.append(v1)
    b.append(v2)
    print('KKKASKA')
    pprint(b)
    queries_avc_true = enviar_lista_queries()
    queries_avc_false = enviar_queries_avc_falso()
    
    for i in range(0,len(queries_avc_true)):
        valor_cenario_true, valor_cenario_false = get_match_from_query(queries_avc_true[i],dataset), get_match_from_query(queries_avc_false[i],dataset)
        #print('ssdfjsdfsssssss')
        #print(valor_cenario_false)
        try:
            valor_final_1 = valor_cenario_true / valor_cenario_false
        except ZeroDivisionError:
            valor_final_1 = 0
        valor_final_2 = 1 - valor_final_1
        dados.append(round(valor_final_1,2))
        dados.append(round(valor_final_2,2)) 
    print('SHDUASHDUASDHUASH')
    a = open('a.txt','w')
    a.write(str(dados))
    return dados

# def gerar_probs_node_avc(dataset):
#     dados = get_numeros_dataset_avc(dataset)
#     prob_iniciais = []
#     num_avcs = get_number_of_avcs(dataset)
#     for i in dados:
#         porcentagem,contraparte = calcular_porcentagem(i,num_avcs)
#         prob_iniciais.append(porcentagem)
#         prob_iniciais.append(contraparte)

#     return prob_iniciais

# Realiza os calculos para gerar a porcentagem que será usada no nós da rede bayesiana
def calcular_porcentagem(entrada, tamanho):
    aux = (entrada * 100) / tamanho
    porcentagem = round(aux/100,2)
    aux2 = 1 - porcentagem
    contraparte = round(aux2,2)
    return porcentagem, contraparte

#para diferenciar imc masculino e feminino, a ideia é quando for masculino retirar o valor do feminino no total do dataset e vice-versa
# as entradas são num_abaixo_ideal_masc e num_abaixo_ideal_fem ou vice-versa
# o retorno será porcentagem de num_abaixo_ideal_masc (ou feminino) e sua contraparte
# def calcular_porcentagem_imc(entrada1,entrada2,tamanho):
#     aux = (entrada1 * 100) / (tamanho - entrada2)
#     porcentagem = round(aux/100,2)
#     aux2 = 1 - porcentagem
#     contraparte = round(aux2,2)
#     return porcentagem, contraparte

def gerar_probs_nos_perifericos(dataset):
    
    '''
    VARIAVEL -> INDICE
    num_homens_dataset -> 0
    num_hipertensao -> 1
    num_hist_doenca_cardiaca -> 2
    num_fumam_ja_fumaram -> 3
    num_abaixo_ideal_masc -> 4
    num_hipoglicemia_normal -> 5
    num_jovens_adultos -> 6
    '''

    dados = get_numeros_dataset(dataset)
    prob_iniciais = []
    
    tamanho_dataset = get_total_records_of_dataset(dataset)
    
    for i in range(0,len(dados)):
            porcentagem,contraparte = calcular_porcentagem(dados[i],tamanho_dataset)
            prob_iniciais.append(porcentagem)
            prob_iniciais.append(contraparte)

    '''
    VARIAVEL,NEGACAO -> INDICES
    porc_homens,porc_mulheres -> 0-1,
    porc_hipertensos,porc_nao_hipertensos -> 2-3
    porc_doenca_card,porc_nao_doenca_card -> 4-5,
    porc_fumam_ja_fumaram,porc_nunca_fumaram_desconhecido -> 6-7, 
    porc_abaixo_ideal,porc_acima_obeso -> 8-9,
    porc_hipoglicemia_normal,porc_alterado_diabetes -> 10-11,
    porc_jovens_adultos,porc_idosos -> 12-13 
    '''
    return prob_iniciais
