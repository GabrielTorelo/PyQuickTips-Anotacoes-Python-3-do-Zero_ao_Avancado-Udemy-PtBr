idade = '24'

if (type(idade) is int):
  print("Idade é um inteiro")
else:
  idade = int(idade)
  print("Idade agora é um inteiro")

if (type(idade) is not int and type(idade) is str):
  print("Idade é uma string")
elif (type(idade) is int):
  print("Idade é um inteiro")
else:
  print("Idade não é uma string nem um inteiro")
