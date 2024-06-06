# Importa o módulo threading (usado para criar threads)
from threading import Thread

# Importa o módulo time (usado para manipular a execução do script)
from time import sleep

# Criando uma classe SubThread que herda de Thread
class SubThread(Thread):

  # Método construtor
  def __init__(self, texto, tempo):
    self.texto = texto
    self.tempo = tempo

    super().__init__()

  # Método run (executado quando a thread é iniciada)
  def run(self):
    sleep(self.tempo)
    print(self.texto)

# Criando duas threads
t1 = SubThread('Thread 1', 10)
t2 = SubThread('Thread 2', 5)

# Iniciando as threads
t1.start()
t2.start()

# Rodando um loop independente das threads (main thread)
for i in range(1, 11):
  print(i)
  sleep(1)

# --------------------------------------------

print('\n')

# --------------------------------------------

# Criando uma função que será executada por uma thread
def func_atraso(texto, tempo):
  sleep(tempo)
  print(texto)

# Criando uma thread a partir de uma função
t3 = Thread(target=func_atraso, args=('Thread 3', 5))

# Iniciando a thread
t3.start()

# Aguardando a thread 't3' terminar
while t3.is_alive():
  print('A thread 3 está ativa...')
  
  # Rodando um loop independente das threads (main thread)
  for i in range(1, 6):
    print(i)
    sleep(1)
