# Importa a função calendar do módulo calendar (usado para manipular calendários)
from datetime import datetime
from calendar import calendar

# Importa o módulo locale (usado para manipular configurações regionais)
from locale import getlocale, setlocale, LC_ALL, format_string

# Definindo constantes
NUMERO = 123456.7809
DATA_HOJE = datetime.now()

print(calendar(2024)) # Imprime o calendário do ano de 2024 em inglês

print('\n')

setlocale(LC_ALL, 'pt_BR.UTF-8') # Configura a localização para português do Brasil

print(calendar(2024)) # Imprime o calendário do ano de 2024 em português do Brasil

print('\n')

print('Localização atual:', getlocale()) # Imprime a localização atual

print('\n')

# Formata o número com duas casas decimais e separador de milhar
num_formatado = format_string('%0.2f', NUMERO, grouping=True)
print('Número formatado:', num_formatado)

print('\n')

str_data = '%A, %d de %B de %Y' # Formato da data que será exibido
data_formatada = DATA_HOJE.strftime(str_data) # Formata a data
print(data_formatada)
