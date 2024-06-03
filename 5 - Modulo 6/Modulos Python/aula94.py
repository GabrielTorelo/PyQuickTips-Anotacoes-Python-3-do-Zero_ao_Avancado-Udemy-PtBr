# Importa o módulo json (usado para manipular arquivos JSON)
from json import loads, dumps

# Importa o módulo TypedDict (usado para definir um dicionário tipado)
from typing import TypedDict

# Define um dicionário tipado
class Pessoa(TypedDict):
  nome: str
  sobrenome: str
  idade: int

# Cria uma string que contém um objeto JSON
string_json = """
  {
    "nome": "João",
    "sobrenome": "Silva",
    "idade": 30
  }
"""

# Tenta converter uma string JSON em um dicionário
try:
  # Convertendo para um dicionário
  dicionario: Pessoa = loads(string_json)

  print(dicionario)
  print(f'Nome: {dicionario["nome"]}\n')

  # Convertendo dicionário para uma string JSON
  dicionario_string = dumps(dicionario, ensure_ascii=False, indent=2)
  print(f'String JSON: \n{dicionario_string}')

except Exception as e: # Trata caso ocorra algum erro
  print('Erro ao converter JSON:', e)
