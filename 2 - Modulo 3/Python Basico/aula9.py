user_input = input("Deseja entrar no sistema? (S/N): ")
senha = '123'

if user_input.lower() != 's' and user_input.lower() != 'n':
  print('Opção inválida!')
  exit()
elif user_input.lower() == 's':
  senha_digitada = input("Digite a senha: ")
  
  if senha_digitada == senha:
    print('\nBem-vindo ao sistema!')
  else:
    print('\nSenha inválida!')
else:
  print('\nAté a próxima! Volte sempre!')
  exit()

# Versão com tentativas de acesso ao sistema:
#
# user_input = input("Deseja entrar no sistema? (S/N): ")
# tentativas = 3
# senha = '123'
#
# if user_input.lower() != 's' and user_input.lower() != 'n':
#   print('Opção inválida!')
#   exit()
# elif user_input.lower() == 's':
#   while tentativas > 0:
#     tentativas -= 1
#     senha_digitada = input("Digite a senha: ")
#
#     if senha_digitada == senha:
#       print('Bem-vindo ao sistema!')
#     else:
#       if tentativas > 0:
#         print(f'\nSenha inválida! Tente novamente, {tentativas} tentativa(s) restante(s).')
#       else:
#         print(f'\nSenha inválida!')
#
#   print('Acesso bloqueado! Tente novamente mais tarde.')
#   exit()
# else:
#   print('Até a próxima! Volte sempre!')
#   exit()
