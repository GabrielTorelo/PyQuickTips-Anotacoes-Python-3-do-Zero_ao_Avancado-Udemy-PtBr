from datetime import datetime # Importa a classe datetime do módulo datetime (usado para manipular datas)
from pytz import timezone # Importa a função timezone do módulo pytz (usado para manipular fusos horários)

# Cria objetos datetime com o fuso horário de São Paulo e Karachi
data1 = datetime.now()
data2 = datetime.now(timezone('America/Sao_Paulo'))
data3 = datetime.now(timezone('Asia/Karachi'))
data4 = datetime(2024, 5, 28, 13, 11, 5, tzinfo=timezone('America/Sao_Paulo'))

# Exibe a data e hora atual de São Paulo
print(f'Timestamp de data_1: {data1.timestamp()}')

# Converte o timestamp para data
print(f'Data a partir do timestamp: {datetime.fromtimestamp(1716993850.77818)}\n')

# Exibe as datas e horas atuais de São Paulo e Karachi
print(f'Data_1: {data1}')
print(f'Data_2: {data2}')
print(f'Data_3: {data3}')
print(f'Data_4: {data4}')
