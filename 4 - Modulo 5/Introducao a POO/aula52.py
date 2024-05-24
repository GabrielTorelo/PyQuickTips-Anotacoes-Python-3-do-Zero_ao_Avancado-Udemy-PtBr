# Criando a classe Produto
class Produto:

  # Método construtor
  def __init__(self, nome: str, preco: float):
    self.nome = nome
    self.preco = preco

  @property # Getter
  def get_nome(self):
    return self._nome

  @property # Getter
  def get_preco(self):
    return self._preco

  @get_nome.setter # Setter
  def nome(self, nome: str):
    self._nome = nome

  @get_preco.setter # Setter
  def preco(self, preco: float):
    self._preco = preco

# Criando a classe CarrinhoCompras
class CarrinhoCompras:

  # Método construtor (recebe um objeto do tipo Produto e uma quantidade)
  def __init__(self, produto: Produto, quantidade: int):
    self.produto = produto
    self.quantidade = quantidade

  # Método para imprimir
  def __str__(self) -> str:
    return f'O carrinho possui {self.get_quantidade} unidade(s) do '\
      f'produto: {self.get_produto.get_nome} | '\
      f'Total: R$ {self.total():.2f}'

  def total(self) -> float:
    return round(self.get_produto.get_preco * self.get_quantidade, 2)

  @property # Getter
  def get_produto(self):
    return self._produto

  @property # Getter
  def get_quantidade(self):
    return self._quantidade

  @get_produto.setter # Setter
  def produto(self, produto: Produto):
    self._produto = produto

  @get_quantidade.setter # Setter
  def quantidade(self, quantidade: int):
    self._quantidade = quantidade

# Instanciando os objetos do tipo Produto
p1 = Produto('Celular', 1600)
p2 = Produto('Mouse', 79.70)

# Instanciando os objetos do tipo CarrinhoCompras
car1 = CarrinhoCompras(p1, 2)
car2 = CarrinhoCompras(p2, 5)

print(car1)
print(car2)
