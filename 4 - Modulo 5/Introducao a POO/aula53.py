# Criando uma classe Endereco
class Endereco:

  # Método construtor
  def __init__(self, rua, numero):
    self.rua = rua
    self.numero = numero

  # Método para imprimir
  def __str__(self) -> str:
    return f'{self.get_rua}, {self.get_numero}'

  # Método para fazer algo quando o objeto for removido
  def __del__(self):
    print(f'Removendo o endereço: {self.get_rua}')

  @property # Getter
  def get_rua(self):
    return self._rua

  @property # Getter
  def get_numero(self):
    return self._numero

  @get_rua.setter # Setter
  def rua(self, rua):
    self._rua = rua

  @get_numero.setter # Setter
  def numero(self, numero):
    self._numero = numero

# Criando a classe Cliente
class Cliente:

  # Método construtor
  def __init__(self, nome: str, enderecos: list[Endereco]):
    self.nome = nome
    self.enderecos = enderecos

  # Método para imprimir
  def __str__(self) -> str:
    return f'"{self.get_nome}" possui os endereços: {self.get_endereco}'

  # Método para fazer algo quando o objeto for removido
  def __del__(self):
    print(f'Removendo o cliente: {self.get_nome}')

  @property # Getter
  def get_nome(self):
    return self._nome

  @property # Getter
  def get_endereco(self):
    return list(map(str, self._enderecos)) # Mapeando e retornando a lista de endereços

  @get_nome.setter # Setter
  def nome(self, nome: str):
    self._nome = nome

  @get_endereco.setter # Setter
  def enderecos(self, enderecos: list[Endereco]):
    ender = []

    # Adicionando os endereços na lista
    for end in enderecos:
      ender.append(Endereco(end.get_rua, end.get_numero))

    # Atribuindo a lista de endereços
    self._enderecos = ender

# Instanciando objetos do tipo Endereco
end1 = Endereco('Rua das Ruas', 1234)
end2 = Endereco('Rua sem nome', 4321)
end3 = Endereco('Rua São Judas', 334)

# Instanciando objetos do tipo Cliente
cli1 = Cliente('Jose', [end1, end2])
cli2 = Cliente('Maria', [end3])

del end1, end2, end3

print(f'\n{cli1}\n')

del cli1

print(f'\n{cli2}')

print('\n\nFim do programa\n')
