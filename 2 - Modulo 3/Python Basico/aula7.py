user_input = input("Deseja entrar no sistema? (S/N): ")

if user_input.lower() == 's':
  print('Bem-vindo ao sistema!')
elif user_input.lower() == 'n':
  print('Não logado!')
else:
  print('Opção inválida!')
