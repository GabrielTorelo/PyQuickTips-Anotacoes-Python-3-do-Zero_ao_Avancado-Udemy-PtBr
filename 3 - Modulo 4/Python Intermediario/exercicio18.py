"""
  Crie um sistema de perguntas e respostas
  - Crie um dicionário vazio chamado 'perguntas'
  - Adicione 3 perguntas ao dicionário
  - Cada pergunta deve ser um dicionário com as chaves 'Pergunta', 'Opções' e 'Resposta'
  - As opções devem ser uma lista de strings
  - Imprima todas as perguntas com as opções
  - Peça para o usuário responder as perguntas
  - Verifique se a resposta está correta
  - Imprima a quantidade de respostas corretas
"""

perguntas = [
  {
    'Pergunta': 'Quanto é 2 + 2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4',
  },
  {
    'Pergunta': 'Quanto é 5 * 5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25',
  },
  {
    'Pergunta': 'Quanto é 10 / 2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5',
  },
]

respostas_corretas = 0

for pergunta in perguntas:
  print(pergunta['Pergunta'])

  for index, opcao in enumerate(pergunta['Opções']):
    print(f'{index+1}) {opcao}')

  resposta = input('\nQual a opção correta? ')

  print('\n')

  try:
    resposta = int(resposta)
  except ValueError:
    print('Por favor, digite apenas números inteiros.\n')
    continue

  if resposta < 1 or resposta > 4:
    print('\nPor favor, digite um número entre 1 e 4.\n')
    continue

  if pergunta['Opções'][resposta-1] == pergunta['Resposta']:
    respostas_corretas += 1

if respostas_corretas <= 0:
  print('Você não acertou nenhuma pergunta! 😔')
elif respostas_corretas >= 1 and respostas_corretas <= 2:
  print(f'Você acertou {respostas_corretas} perguntas! 😊')
else:
  print(f'Você acertou todas as perguntas! 🎉🎉🎉')
