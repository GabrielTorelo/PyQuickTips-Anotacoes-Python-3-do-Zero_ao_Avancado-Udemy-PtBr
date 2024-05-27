# Criando a classe MyContextManager
class MyContextManager:

  # Método construtor
  def __init__(self, file_path, mode):
    self.file_path = file_path
    self.mode = mode
    self._file = None

  # Método __enter__ que será chamado quando o bloco "with" for iniciado
  def __enter__(self):
    print('Abrindo o arquivo...')
    self._file = open(self.file_path, self._mode, encoding='utf8') # Abrindo o arquivo
    return self._file # Retornando o arquivo

  # Método __exit__ que será chamado quando o bloco "with" for finalizado
  def __exit__(self, exc_type, exc_value, exc_traceback):
    print('\nFechando o arquivo...')
    self._file.close() # Fechando o arquivo

    # Verificando se houve algum erro
    if exc_type is not None:
      if exc_type == FileNotFoundError: # Verificando se o erro foi de arquivo não encontrado
        print(f'\nArquivo não encontrado: {exc_value}')
      elif exc_type == PermissionError: # Verificando se o erro foi de permissão negada
        print(f'\nPermissão negada: {exc_value}')
      else: # Caso contrário, exibir o erro genérico
        print(f'\nOcorreu um erro: {exc_value}')

    return True # Retornando True para indicar que o erro foi tratado

  @property # Getter
  def get_file_path(self):
    return self._file_path
  
  @property # Getter
  def get_mode(self):
    return self._mode
  
  @get_file_path.setter # Setter
  def file_path(self, file_path):
    self._file_path = file_path

  @get_mode.setter # Setter
  def mode(self, mode):
    self._mode = mode

# Criando uma instância da classe MyContextManager
my_instance = MyContextManager('aula70.txt', 'r')

# Utilizando o bloco "with" para chamar a instância da classe MyContextManager
with my_instance as my:
  print(f'1ª linha: {my.readline()}', end='') # Lendo a 1ª linha do arquivo
  lines = my.readlines() # Lendo as linhas restantes do arquivo
  
  print('\nRestante do conteúdo do arquivo:')
  
  # Imprimindo o conteúdo do arquivo
  for line in lines:
    print(line, end='')

  my.write('Escrevendo no arquivo...') # Tentando escrever no arquivo
