# Criando a classe CallMe
class CallMe:

  # Método construtor
  def __init__(self, phone):
    self.phone = phone

  # Método que permite chamar a instância da classe como uma função
  def __call__(self, nome):
    print(nome, 'está chamando', self.phone)

# Criando uma instância da classe CallMe
call = CallMe('(11) 91111-1111')

# Chamando o método '__call__' e passando um parâmetro para ele
retorno = call('Marcos Vinícius')
