"""
  Criar um sistema bancário (extremamente simples) que tem clientes, contas e
  um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
  possa sacar/depositar nessa conta.
  
    Contas corrente tem um limite extra:
      - Conta corrente tem um limite de R$ 1000.00 para saque
      - Conta poupança tem um limite de R$ 300.00 para saque

    Conta (ABC)
      ContaCorrente
      ContaPoupanca

    Pessoa (ABC)
      Cliente
        Cliente -> Conta

    Banco
      Banco -> Cliente

  Dicas:
    1 - Criar classe Cliente que herda da classe Pessoa (herança)
      1.1 - Pessoa tem nome e idade (com getters)
      1.2 - Cliente tem conta (agregação da classe ContaCorrente ou ContaPoupanca)
    
    2 - Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
      2.1 - ContaCorrente deve ter um limite extra
      2.2 - Contas têm agência, número da conta e saldo
      2.3 - Contas devem ter método para depósito
      2.4 - Conta (super classe) deve ter o método sacar abstrato (abstração e
            polimorfismo - as subclasses que implementam o método sacar)
    
    3 - Criar classe Banco para AGREGAR classes de clientes (agregação)
      3.1 - Banco será responsável autenticar o cliente da seguinte forma:
        3.1.1 - Checar se a agência é daquele banco
      3.2 - Só será possível sacar e depositar se passar na autenticação do banco (descrita acima)
      3.3 - Banco autentica por um método.
"""

# Importando o módulo abc - Necessário para manipulação de classes abstratas
from abc import ABC, abstractmethod

# Criando a classe Conta
class Conta(ABC):

  # Método construtor
  def __init__(self, agencia: int, numero_conta: int, saldo: float = 0):
    self.agencia = agencia
    self.numero_conta = numero_conta
    self.saldo = saldo

  # Método para realização de depósito
  def deposito(self, valor: float) -> bool:
    if valor > 0: # Verifica se o valor é maior que zero
      self.saldo += valor # Adiciona o valor ao saldo
      print(f'Depósito de R$ {valor} realizado com sucesso!')
      return True
    
    print('Valor inválido! Tente novamente!')
    return False

  # Método abstrato (deve ser implementado nas classes filhas)
  @abstractmethod
  def sacar(self, valor: float) -> bool:
    pass
    
  @property # Getter
  def get_agencia(self):
    return self._agencia

  @property # Getter
  def get_numero_conta(self):
    return self._numero_conta

  @property # Getter
  def get_saldo(self):
    return self._saldo

  @get_agencia.setter # Setter
  def agencia(self, agencia: int):
    self._agencia = agencia

  @get_numero_conta.setter # Setter
  def numero_conta(self, numero_conta: int):
    self._numero_conta = numero_conta

  @get_saldo.setter # Setter
  def saldo(self, saldo: float):
    self._saldo = saldo

# Criando a classe ContaCorrente
class ContaCorrente(Conta):
  LIMITE = 1000 # Limite extra para a conta corrente

  # Método para realizar saque
  def sacar(self, valor: float) -> bool:
    if valor > self.LIMITE: # Verifica se o valor é maior que o limite
      print('Valor solicitado maior que o seu limite! Limitado a R$ 1000.00 por saque!')
    elif valor > self.saldo: # Verifica se o valor é maior que o saldo
      print(f'Saldo insuficiente! Seu saldo é de R$ {self.saldo:.2f}')
    else: # Caso contrário
      self.saldo -= valor # Subtrai o valor do saldo
      print(f'Saque de R$ {valor} realizado com sucesso!')
      return True
    
    return False

# Criando a classe ContaPoupanca
class ContaPoupanca(Conta):
  LIMITE = 300 # Limite para a conta poupança

  # Método para realizar saque
  def sacar(self, valor: float) -> bool:
    if valor > self.LIMITE: # Verifica se o valor é maior que o limite
      print('Valor solicitado é maior que o seu limite! Limitado a R$ 300.00 por saque!')
    elif valor > self.saldo: # Verifica se o valor é maior que o saldo
      print(f'Saldo insuficiente! Seu saldo é de R$ {self.saldo:.2f}')
    else: # Caso contrário
      self.saldo -= valor # Subtrai o valor do saldo
      print(f'Saque de R$ {valor} realizado com sucesso!')
      return True
    
    return False

# Criando a classe Pessoa
class Pessoa(ABC):

  # Método construtor
  def __init__(self, nome: str, idade: int) -> None:
    self.nome = nome
    self.idade = idade

  @property # Getter
  def get_nome(self):
    return self._nome

  @property # Getter
  def get_idade(self):
    return self._idade

  @get_nome.setter # Setter
  def nome(self, nome: str):
    self._nome = nome
  
  @get_idade.setter # Setter
  def idade(self, idade: int):
    self._idade = idade

# Criando a classe Cliente
class Cliente(Pessoa):

  # Método para representar a classe (retorna uma string ao chamar a classe)
  def __str__(self) -> str:
    saldo = self.get_conta_cliente.get_saldo
    return f'{self.get_nome} o seu saldo é de R$ {saldo:.2f}'
  
  # Método para associar a conta do cliente
  def associar_conta(self, conta: Conta):
    self._conta_cliente = conta

  @property # Getter
  def get_conta_cliente(self):
    return self._conta_cliente

# Criando a classe Banco
class Banco:
  AGENCIA = 1234 # Agência do banco

  # Método para verificar os dados do cliente
  def autenticar(self, cliente: Cliente):

    # Verifica se a agência é do banco
    if cliente.get_conta_cliente.get_agencia != self.AGENCIA:
      print('Verificação falhou!' + '\n' + 'Essa agência não pertence ao nosso banco!')
    else: # Caso contrário
      print(f'Olá {cliente.get_nome}! Seja bem-vindo(a) ao banco!')
      return True
    
    return False

# Criando uma instância da classe Banco
banco = Banco()

# Criando instâncias da classe ContaCorrente
conta_corrente_1 = ContaCorrente(1234, 123456, 1000)
conta_corrente_2 = ContaCorrente(1235, 234566, 5000)

# Criando uma instância da classe ContaPoupanca
conta_poupanca_1 = ContaPoupanca(1234, 123456, 1000)

# Criando instâncias da classe Cliente
c1 = Cliente('João', 25)
c2 = Cliente('Maria', 30)
c3 = Cliente('José', 35)

# Associando as contas dos clientes
c1.associar_conta(conta_corrente_1)
c2.associar_conta(conta_corrente_2)
c3.associar_conta(conta_poupanca_1)


# Verifica se os dados do cliente são válidos
if banco.autenticar(c1):
  print(c1)
  c1.get_conta_cliente.sacar(1000)
  c1.get_conta_cliente.deposito(50)
  print(c1)

print('\n')

# Verifica se os dados do cliente são válidos
if banco.autenticar(c2):
  print(c2)
  c2.get_conta_cliente.sacar(1001)
  c2.get_conta_cliente.deposito(500)
  print(c2)

print('\n')

# Verifica se os dados do cliente são válidos
if banco.autenticar(c3):
  print(c3)
  c3.get_conta_cliente.sacar(2000)
  c3.get_conta_cliente.deposito(500)
  print(c3)
