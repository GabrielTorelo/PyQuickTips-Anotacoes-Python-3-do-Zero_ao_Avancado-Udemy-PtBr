# Importa a classe datetime do módulo datetime (usado para manipular datas)
from datetime import datetime

# Cria um formato para a data e hora
formato = '%d/%m/%Y %H:%M:%S'

# Cria um objeto datetime com a data e hora atual
data = datetime.now()

# Formata a data e hora, conforme o formato passado
print(data.strftime(formato))
