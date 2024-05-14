user_input = input("Deseja entrar no sistema? [S]im/[N]ão/[C]ancelar: ")
senha = '123'

if user_input.lower() == 's':
  senha_digitada = input("Digite a senha: ")

  if senha_digitada == senha:
    print('\nBem-vindo ao sistema!')
  else:
    print('\nSenha inválida!')
elif user_input.lower() == 'n' or user_input.lower() == 'c':
  print('\nAté a próxima! Volte sempre!')
  exit()
else:
  print('Opção inválida!')
  exit()

# Versão com tentativas de acesso ao sistema:
#
# user_input = input("Deseja entrar no sistema? [S]im/[N]ão/[C]ancelar: ")
# tentativas = 3
# senha = '123'
#
# if user_input.lower() == 's':
#   while tentativas > 0:
#     tentativas -= 1
#     senha_digitada = input("Digite a senha: ")
#
#     if senha_digitada == senha:
#       print('\nBem-vindo ao sistema!')
#       exit()
#     else:
#       if tentativas > 0:
#         print(f'\nSenha inválida! Tente novamente, {tentativas} tentativa(s) restante(s).')
#       else:
#         print(f'\nSenha inválida!')
#
#   print('\nAcesso bloqueado! Tente novamente mais tarde.')
#   exit()
# elif user_input.lower() == 'n' or user_input.lower() == 'c':
#   print('\nAté a próxima! Volte sempre!')
#   exit()
# else:
#   print('\nOpção inválida!')
#   exit()
