from json import dump, load

'''
  Salvar a lista de tarefas feita no 'exercicio26.py' em um arquivo JSON
'''

def ler_arquivo():
  dados = []

  try:
    with open('exercicio27.json', 'r', encoding='utf8') as arquivo:
      dados = load(arquivo)
      print('Dados carregados com sucesso!')
  except FileNotFoundError:
    print('Dados salvos não encontrados! Criando nova lista...')
  except Exception:
    print('Ocorreu um erro inesperado ao tentar salvar o arquivo!')

  return dados

def salvar_arquivo(lista):
  try:
    with open('exercicio27.json', 'w', encoding='utf8') as arquivo:
      dump(lista, arquivo, indent=2, ensure_ascii=False)
      print('Tarefas salvas com sucesso!')
  except PermissionError:
    print('Tarefas não foram salvas! Você não tem permissão para salvar arquivos!')
  except Exception:
    print('Tarefas não foram salvas! Ocorreu um erro inesperado ao tentar salvar o arquivo!')


tarefas = ler_arquivo() # Lista de tarefas (recebendo do arquivo)
desfazer = [] # Lista de desfazer
refazer = [] # Lista de refazer

print('.: Lista de tarefas :.')

while True:
  # Menu de opções
  user_input = input('\nO que deseja fazer? [L]istar todos | [A]dicionar novo | [R]emover último | [V]oltar último | [S]air : ').lower()

  if user_input == 'l': # Listar tarefas
    if not tarefas: # Se não houver tarefas
      print('Nada a mostrar')
    else: # Se houver tarefas
      print(f'\nTarefas: {tarefas}')
  elif user_input == 'a': # Adicionar tarefas
    task_user_input = input('O que deseja inserir: ').title()
    tarefas.append(task_user_input) # Adiciona tarefa
  elif user_input == 'r': # Remover tarefas
    if not tarefas: # Se não houver tarefas para remover
      print('Nada a remover')
    else: # Se houver tarefas para remover
      task_user_pop = tarefas.pop() # Remove tarefa
      desfazer.append(task_user_pop) # Adiciona tarefa removida a lista de desfazer
      print(f'"{task_user_pop}" removido da lista!\n')
  elif user_input == 'v': # Voltar tarefas
    if not desfazer: # Se não houver tarefas para voltar
      print('Nada a voltar')
    else: # Se houver tarefas para voltar
      desfazer_user_pop = desfazer.pop() # Remove tarefa da lista de desfazer
      tarefas.append(desfazer_user_pop) # Adiciona tarefa removida a lista de tarefas
      print(f'"{desfazer_user_pop}" retornado a lista!\n')
  elif user_input == 's': # Sair
    # Pergunta se deseja sair
    ask_user = input('\nDeseja sair? [S]im | [N]ão : ').lower()
    if ask_user == 's': # Se sim, salvar e sair
      print('Salvando tarefas...')
      
      salvar_arquivo(tarefas)

      print('\nAté mais!\n')
      break
  else: # Se opção inválida
    print('Opção inválida!')
