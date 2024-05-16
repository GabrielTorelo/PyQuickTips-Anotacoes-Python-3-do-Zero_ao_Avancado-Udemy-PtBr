"""
  Faça uma lista de comprar com listas
  O usuário deve ter a possibilidade de
  inserir, apagar e listar valores da sua lista
  Não permita que o programa quebre com 
  erros de índices inexistentes na lista.
"""

lista = []

while True:
  print('Selecione uma opção')
  opcao = input('[I]nserir [A]pagar [L]istar: ').lower()

  if opcao == 'i':
    valor = input('Valor: ')
    lista.append(valor)
  elif opcao == 'a':
    user_indice = input('Qual índice deseja apagar? ')

    try:
      indice = int(user_indice)
      lista.pop(indice)
    except ValueError:
      print('\nPor favor digite um número inteiro.')
      continue
    except IndexError:
      print('\nO índice não existe na lista')
      continue
    except Exception:
      print('\nErro desconhecido')
      continue
  elif opcao == 'l':
    if len(lista) == 0:
      print('\nNão possui nada para ser listado!')

    for i, valor in enumerate(lista):
      print('\n', i, valor)
  else:
      print('\nPor favor, escolha i, a ou l.')
