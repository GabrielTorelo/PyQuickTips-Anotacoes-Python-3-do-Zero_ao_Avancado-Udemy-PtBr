# Importa a classe datetime do módulo datetime (usado para manipular datas)
from datetime import datetime

# Cria objetos datetime com 'dia', 'mês' e 'ano' passados como argumentos
d1 = datetime(2024, 5, 29)

# Cria objetos datetime com 'dia', 'mês', 'ano', 'hora', 'minuto' e 'segundo' passados como argumentos
d2 = datetime(2024, 5, 28, 13, 11, 5)

# Criando objetos datetime com a data e o formato passada como string
d3 = datetime.strptime('2024-05-29 13:17:09', '%Y-%m-%d %H:%M:%S')

print(f'Data_1: {d1}')
print(f'Data_2: {d2}')
print(f'Data_3: {d3}')
