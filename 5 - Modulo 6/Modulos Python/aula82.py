# Importa a classe datetime do módulo datetime (usado para manipular datas)
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# Cria objetos datetime com a data e o formato passada como string
d1 = datetime.strptime('28/05/2024', '%d/%m/%Y')
d2 = datetime.strptime('29/05/2024 12:00:00', '%d/%m/%Y %H:%M:%S')

# Comparando datas
print(f'{d1.date()} > {d2.date()} = {d1.date() > d2.date()}')
print(f'{d1.date()} < {d2.date()} = {d1.date() < d2.date()}')
print(f'{d1.date()} == {d2.date()} = {d1.date() == d2.date()}')
print(f'{d1.date()} != {d2.date()} = {d1.date() != d2.date()}')

# --------------------------------------------

print('\n')

# --------------------------------------------

# Comparando horários
print(f'{d1.time()} < {d2.time()} = {d1.time() < d2.time()}')
print(f'{d1.time()} > {d2.time()} = {d1.time() > d2.time()}')
print(f'{d1.time()} == {d2.time()} = {d1.time() == d2.time()}')
print(f'{d1.time()} != {d2.time()} = {d1.time() != d2.time()}')

# --------------------------------------------

print('\n')

# --------------------------------------------

# Calculando a diferença entre datas e horários
print(f'{d2.date()} - {d1.date()} = {d2 - d1}')

# Cria um objeto timedelta com 10 dias e 5 horas
dias = timedelta(days=10, hours=5)

# Adiciona 10 dias e 5 horas na data d1
d3 = d1 + dias

print(f'{d1.date()} + 10 dias = {d3.date()}')

# --------------------------------------------

print('\n')

# --------------------------------------------

# Cria um objeto relativedelta com 60 segundos
segundos = relativedelta(seconds=60)

# Adiciona 60 segundos na data d2
d4 = d2 + segundos

print(f'{d2.time()} + 60 segundos = {d4.time()}')


# --------------------------------------------

print('\n')

# --------------------------------------------

# Cria objeto datetime com a data e o formato passada como string
d5 = datetime.strptime('28/09/2021 09:03:56', '%d/%m/%Y %H:%M:%S')

# Calculando de forma detalhada a diferença entre datas
d6 = relativedelta(d2, d5)

print(f'{d2} - {d5} = {d6.years} anos, {d6.months} meses, {d6.days} dias, {d6.hours} horas, {d6.minutes} minutos e {d6.seconds} segundos')
