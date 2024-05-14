verdadeiro = True
falso = not verdadeiro

print("Valor original:", verdadeiro)
print("Valor negado:", falso)

print(not(11 > 12))

senha_digitada = input("\nDigite a senha: ")
senha = '123'

if not senha:
  print("\nSenha não informada")
elif senha_digitada == senha:
  print('\nBem-vindo ao sistema!')
else:
  print('\nSenha inválida!')
