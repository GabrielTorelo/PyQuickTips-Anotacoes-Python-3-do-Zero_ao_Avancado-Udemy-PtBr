# Importa o módulo threading (usado para criar threads)
from threading import Lock, Thread

# Importa o módulo time (usado para manipular a execução do script)
from time import sleep

class Ingresso:
  # Método construtor
  def __init__(self, estoque):
    self.estoque = estoque
    self.lock = Lock() # Cria um objeto do tipo Lock (usado para bloquear o acesso a um recurso compartilhado)

  # Método para comprar ingressos
  def comprar(self, quantidade):
    
    # Bloqueia o acesso ao método comprar, para que apenas uma thread por vez possa executá-lo
    self.lock.acquire()

    # Verifica se a quantidade de ingressos solicitada é maior que o estoque
    if self.estoque < quantidade:

      # Verifica se o estoque é igual a 0
      if self.estoque == 0:
        # Se sim, exibe uma mensagem informando que não há mais ingressos disponíveis
        print('Não temos mais ingressos disponíveis.')
                
        # Libera o acesso ao método comprar
        self.lock.release()

        return
      else:
        # Se não, exibe uma mensagem informando a quantidade de ingressos disponíveis
        print(f'Temos apenas {self.estoque} ingresso(s) disponível(is). Você tentou comprar {quantidade} ingressos.\n')
        
        # Libera o acesso ao método comprar
        self.lock.release()

      return
    
    # Exibe uma mensagem informando que a compra está sendo processada
    print(f'Aguarde (2 segundos), processando compra de {quantidade} ingresso(s)...')
    sleep(2) # Aguarda 2 segundos

    # Se possuir ingressos disponíveis, decrementa a quantidade de ingressos solicitada do estoque
    self.estoque -= quantidade
    print(f'Você comprou {quantidade} ingresso(s). Temos {self.estoque} em estoque.\n')

    # Libera o acesso ao método comprar
    self.lock.release()

# Criando uma instância da classe Ingresso
ingresso = Ingresso(8) # Cria instância com 8 ingresso disponíveis

# Criando threads para simular a compra de ingressos
compra1 = Thread(target=ingresso.comprar, args=(2,))
compra2 = Thread(target=ingresso.comprar, args=(4,))
compra3 = Thread(target=ingresso.comprar, args=(3,))
compra4 = Thread(target=ingresso.comprar, args=(3,))
compra5 = Thread(target=ingresso.comprar, args=(1,))
compra6 = Thread(target=ingresso.comprar, args=(5,))

# Iniciando as threads
compra1.start()
compra3.start()
compra2.start()
compra4.start()
compra5.start()
compra6.start()
