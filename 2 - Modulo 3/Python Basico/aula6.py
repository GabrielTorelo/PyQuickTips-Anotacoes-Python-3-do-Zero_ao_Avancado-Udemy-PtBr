user_input = input('Insira um valor: ')
print(f'O dobro do valor é {int(user_input) * 2}')

# Versão com validação de tipo de dado inserido pelo usuário (valor deve ser numérico):
#
# user_input = input('Insira um valor: ')
#
# if user_input.isnumeric():
#   print(f'O dobro do valor é {int(user_input) * 2}')
# else:
#   print('O valor inserido deve ser um número.')
