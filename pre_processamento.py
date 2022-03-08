import pandas as pd
from queries import enviar_lista_queries, enviar_queries_avc_falso
from util import get_total_records_of_dataset, calcular_porcentagem, get_match_from_query



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

    #Abaixo do peso ou ideal
    abaixo = pd.read_csv(dataset)
    abaixo.query('(bmi < 19.9)', inplace = True)
    num_abaixo = len(abaixo)
    ideal = pd.read_csv(dataset)
    ideal.query('(bmi >= 19.9 and bmi <= 26.1)', inplace = True)
    num_ideal = len(ideal)
    num_abaixo_ideal = num_abaixo + num_ideal
    dados.append(num_abaixo_ideal)


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


#Realiza as queries considerando os casos de AVC, vai contar todas as queries da tabela-verdade
def gerar_probs_node_avc(dataset):
    dados = []
    queries_avc_true = enviar_lista_queries()
    queries_avc_false = enviar_queries_avc_falso()
    for i in range(0,len(queries_avc_true)):
        valor_cenario_true, valor_cenario_false = get_match_from_query(queries_avc_true[i],dataset), get_match_from_query(queries_avc_false[i],dataset)
        try:
            valor_final_1 = valor_cenario_true / valor_cenario_false
        except ZeroDivisionError:
            valor_final_1 = 0
        valor_final_2 = 1 - valor_final_1
        dados.append(round(valor_final_1,2))
        dados.append(round(valor_final_2,2))
    return dados





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