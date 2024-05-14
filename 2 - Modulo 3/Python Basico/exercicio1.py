import datetime

today = datetime.date.today()
ano = today.year

"""
  Criar as variáveis
    'nome',
    'sobrenome',
    'idade',
    'ano_nascimento',
    'maior_de_idade',
    'altura_metros',
  e imprimir no console:
"""

nome = 'Gabriel'
sobrenome = 'Torelo'
idade = 24
ano_nascimento = ano - idade
maior_de_idade = idade >= 18
altura_metros = 1.80

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)
