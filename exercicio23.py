from datetime import date

DIAS = ['Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo']

data = date(year = 2022, month = 2, day = 1)

print(data)
indice_semana = data.weekday()
print(indice_semana)

dia_semana = DIAS[indice_semana]
print(dia_semana)

numero_dia_semana = data.isoweekday()
print(numero_dia_semana)