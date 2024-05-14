"""
  Ler as entradas:
    Nome
    Idade
  
  Se ambos forem digitados:
    Imprimir:
      "Seu nome é {nome}"
      "Seu nome invertido é {nome invertido}"
      "Seu nome contém (ou não) espaços"
      "Seu nome tem {n} letras"
      "A primeira letra do seu nome é {letra}"
      "A última letra do seu nome é {letra}"
  Se nada for digitado ou apenas um dos campos for digitado:
    Imprimir:
      "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
  print(f'\nSeu nome é "{nome}"')
  print(f'Seu nome invertido é "{nome[::-1].lower()}"')

  if ' ' in nome:
    print('Seu nome contém espaços')
  else:
    print('Seu nome não contém espaços')

  print(f'Seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome é "{nome[0].upper()}"')
  print(f'A última letra do seu nome é "{nome[-1].upper()}"')
else:
  print('Desculpe, você deixou campos vazios.')