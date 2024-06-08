# Importa o módulo os (usado para manipular o sistema operacional)
from os import path

# Importa o módulo sqlite3 (usado para manipular banco de dados)
from sqlite3 import connect

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

# Passa o nome do banco de dados
banco_nome = 'banco_de_dados.sqlite3'

# Concatena o caminho com o nome do banco
banco_caminho = path.join(caminho, banco_nome)

# Cria a conexão com o banco de dados
conexao = connect(banco_caminho)

# Cria o cursor para manipular o banco de dados
cursor = conexao.cursor()

# Executa o comando SQL para consultar uma junção de tabelas ('produto' e 'tipo_produto')
consulta_produtos = cursor.execute(
  """
    SELECT prod.idProduto, prod.nome, prod.preco, t.nome 
      FROM produto AS prod
      INNER JOIN tipo_produto AS t
      ON prod.idTipo_produto = t.idTipo_produto;
  """
).fetchall() # O 'fetchall()' retorna todas as tuplas

print('Produtos:', consulta_produtos)

# Executa o comando SQL para consultar o 'produto' mais caro
consulta_produto_mais_caro = cursor.execute(
  """
    SELECT nome, MAX(preco) FROM produto;
  """
).fetchone() # O 'fetchone()' retorna a primeira tupla

print('\nProduto mais caro:', consulta_produto_mais_caro)

# Executa o comando SQL para consultar o valor total dos produtos
consulta_produto_total = cursor.execute(
  """
    SELECT SUM(preco) FROM produto;
  """
).fetchone() # O 'fetchone()' retorna a primeira tupla

print('\nValor total dos produtos:', consulta_produto_total[0]) # O '[0]' indica a primeira tupla

# Executa o comando SQL para consultar o valor médio dos produtos
consulta_produto_media = cursor.execute(
  """
    SELECT ROUND(AVG(preco), 2) FROM produto;
  """
).fetchone() # O 'fetchone()' retorna a primeira tupla

print('\nValor médio dos produtos:', consulta_produto_media[0]) # O '[0]' indica a primeira tupla

# Executa o comando SQL para consultar o valor médio dos produtos por tipo
consulta_produto_media_tipo = cursor.execute(
  """
    SELECT idTipo_produto, AVG(preco) FROM produto GROUP BY idTipo_produto;
  """
).fetchall() # O 'fetchall()' retorna todas as tuplas

print('\nValor médio dos produtos por tipo:', consulta_produto_media_tipo)

# Executa o comando SQL para consultar os produtos com 'preco' maior que 1000
consulta_produto = cursor.execute(
  """
    SELECT idTipo_produto, MAX(preco) FROM produto GROUP BY idTipo_produto HAVING MAX(preco) > 1000;
  """
).fetchall() # O 'fetchall()' retorna todas as tuplas

print('\nProdutos com preço maior que R$ 1.000:', consulta_produto)

# Executa o comando SQL para consultar os produtos ordenados por 'preco' decrescente
consulta_produto_desc = cursor.execute(
  """
    SELECT nome, preco FROM produto ORDER BY preco DESC;
  """
).fetchall() # O 'fetchall()' retorna todas as tuplas

print('\nProdutos ordenados por preço decrescente:', consulta_produto_desc)

# Executa o comando SQL para consultar a data e hora atual no formato brasileiro
data_atual = cursor.execute(
  """
    SELECT strftime('%d/%m/%Y - %H:%M:%S', datetime('now', 'localtime'))
  """
).fetchone() # O 'fetchone()' retorna a primeira tupla

print('\nData e hora atual no formato brasileiro:', data_atual[0]) # O '[0]' indica a primeira tupla

# Fecha o cursor
cursor.close()

# Fecha a conexão
conexao.close()
