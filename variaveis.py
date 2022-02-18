VERDADEIRO_ABAIXO_IDEAL = '((bmi < 19.9 or bmi <= 26.1))'
FALSO_ABAIXO_IDEAL = '((bmi >= 26.2 or bmi >= 31.7))'

VERDADEIRO_FUMA_JA_FUMOU = '(smoking_status == "smokes" or smoking_status == "formerly smoked")'
FALSO_FUMA_JA_FUMOU = '(smoking_status == "never smoked" or smoking_status == "unknown")'

VERDADEIRO_GENERO_MASC = '(gender == "Male")'
FALSO_GENERO_MASC = '(gender == "Female")'

VERDADEIRO_HIPERTENSAO = '(hypertension == 1)'
FALSO_HIPERTENSAO = '(hypertension == 0)'

VERDADEIRO_DOENCA_CARD = '(heart_disease == 1)'
FALSO_DOENCA_CARD = '(heart_disease == 0)'

VERDADEIRO_HIPOGLICEMIA_NORMAL = '(avg_glucose_level <= 70 or avg_glucose_level < 99)'
FALSO_HIPOGLICEMIA_NORMAL = '((avg_glucose_level >= 100 and avg_glucose_level <= 125) or avg_glucose_level >= 126)'

VERDADEIRO_JOVENS_ADULTOS = '(age <= 19 or (age >= 20 and age <= 59))'
FALSO_JOVENS_ADULTOS = '(age >= 60)'

VERDADEIRO_AVC = '(stroke == 1)'
FALSO_AVC = '(stroke == 0)'