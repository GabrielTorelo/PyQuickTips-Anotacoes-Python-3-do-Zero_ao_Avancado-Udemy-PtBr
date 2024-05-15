"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

user_int = input("Digite um número inteiro: ")

try:
  user_int = int(user_int)
except ValueError:
  print("O valor digitado não é um número inteiro")
  exit()

if (user_int % 2 == 0):
  print("O número é par")
else:
  print("O número é ímpar")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

user_hour = input("\nDigite a hora atual: ")

try:
  user_hour = int(user_hour)
except ValueError:
  print("O valor digitado não é um número inteiro")
  exit()

if (user_hour >= 0 and user_hour <= 11):
  print("Bom dia")
elif (user_hour >= 12 and user_hour <= 17):
  print("Boa tarde")
elif (user_hour >= 18 and user_hour <= 23):
  print("Boa noite")
else:
  print("Hora inválida")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

user_name = input("\nDigite seu primeiro nome: ")

if (len(user_name) < 1):
  print("Nome inválido")
  exit()

if (len(user_name) <= 4):
  print("Seu nome é curto")
elif (len(user_name) >= 5 and len(user_name) <= 6):
  print("Seu nome é normal")
else:
  print("Seu nome é muito grande")
