# Importa o módulo os (usado para manipular o sistema operacional)
from os import path, unlink

# Importa o módulo sqlite3 (usado para manipular banco de dados)
from sqlite3 import connect

# Captura o caminho absoluto do arquivo
caminho = path.abspath('.')

# Cria o nome do banco de dados
banco_nome = 'banco_de_dados.sqlite3'

# Concatena o caminho com o nome do banco
banco_caminho = path.join(caminho, banco_nome)

# Verifica se o arquivo do banco de dados já existe
banco_existe = path.exists(banco_caminho)

# Se o arquivo do banco de dados já existe
if banco_existe:
  # Remove o arquivo do banco de dados
  unlink(banco_caminho)

# Cria a conexão com o banco de dados
conexao = connect(banco_caminho)

# Cria o cursor para manipular o banco de dados
cursor = conexao.cursor()

# Executa o comando SQL para criar a tabela 'tipo_produto'
cursor.execute(
  """ 
    CREATE TABLE "tipo_produto" (
      "idTipo_produto"	INTEGER NOT NULL,
      "nome"	TEXT NOT NULL,
      PRIMARY KEY("idTipo_produto" AUTOINCREMENT)
    );
  """
)

# Executa o comando SQL para criar a tabela 'produto'
cursor.execute(
  """
    CREATE TABLE "produto" (
      "idProduto"	INTEGER NOT NULL,
      "nome"	TEXT NOT NULL,
      "preco"	REAL NOT NULL,
      "idTipo_produto"	INTEGER NOT NULL,
      PRIMARY KEY("idProduto" AUTOINCREMENT),
      FOREIGN KEY("idTipo_produto") REFERENCES "tipo_produto"("idTipo_produto")
    );
  """
)

# Executa o comando SQL para criar a tabela 'cliente'
cursor.execute(
  """
    CREATE TABLE "cliente" (
      "idCliente"	INTEGER NOT NULL,
      "nome"	TEXT NOT NULL,
      "cpf"	TEXT NOT NULL,
      PRIMARY KEY("idCliente" AUTOINCREMENT)
    );
  """
)

# Cria uma lista de tuplas com os dados para inserir na tabela 'tipo_produto'
dados_tipo_produto = [
  ('Eletrônicos', ),
  ('Eletrodomésticos', ),
  ('Informática', ),
  ('Telefonia', ),
  ('Móveis', ),
  ('Decoração', )
]

# Executa o comando SQL para inserir os dados na tabela 'tipo_produto' (usando o método executemany)
cursor.executemany(
  """
    INSERT INTO tipo_produto (nome)
      VALUES (?);
  """,
  # Passa a lista de tuplas com os dados e informa que o '?' será substituído pelos valores
  dados_tipo_produto
)

# Cria uma lista de tuplas com os dados para inserir na tabela 'produto'
dados_produto = [
  ('Smart TV 50 Polegadas', 2360.00, 1),
  ('Smartphone Samsung', 1500.00, 4),
  ('Geladeira Frost Free', 2500.00, 2),
  ('Notebook Dell', 3500.00, 3),
  ('Notebook HP', 4500.00, 3),
  ('Cadeira de Escritório', 350.00, 5),
  ('Sofá 3 Lugares', 900.00, 5),
  ('Abajur', 100.00, 6)
]

# Executa o comando SQL para inserir os dados na tabela 'produto' (usando o método executemany)
cursor.executemany(
  """
    INSERT INTO produto (nome, preco, idTipo_produto)
      VALUES (?, ?, ?);
  """,
  # Passa a lista de tuplas com os dados e informa que os '?' serão substituídos pelos valores
  dados_produto
)

# Executa o comando SQL para alterar a tabela 'tipo_produto'
cursor.execute(
  """
    ALTER TABLE tipo_produto ADD peso REAL;
  """
)

# Cria uma tupla de dicionários com os dados para atualizar o campo 'peso' da tabela 'tipo_produto'
dados_atualizacao = (
  # Dados nomeados com os campos 'peso' e 'idTipo_produto'
  {'peso': 2360, 'idTipo_produto': 1},
  {'peso': 4500, 'idTipo_produto': 2},
  {'peso': 2500, 'idTipo_produto': 3},
  {'peso': 350, 'idTipo_produto': 4},
  {'peso': 900, 'idTipo_produto': 5},
  {'peso': 100, 'idTipo_produto': 6}
)

# Executa o comando SQL para atualizar o campo 'peso' da tabela 'tipo_produto'
cursor.executemany(
  """
    UPDATE tipo_produto set peso = :peso WHERE idTipo_produto = :idTipo_produto;
  """,
  # Passa a tupla de dicionários com os dados e informa que os valores serão substituídos pelos campos
  dados_atualizacao
)

# Executa o comando SQL para deletar um registro da tabela 'tipo_produto'
cursor.execute(
  """
    DELETE FROM tipo_produto WHERE idTipo_produto = 3;
  """
)

# Executa o comando SQL para deletar todos os registros da tabela 'produto' onde o 'idTipo_produto' é igual a 3
cursor.execute(
  """
    DELETE FROM produto WHERE idTipo_produto = 3;
  """
)

# Executa o comando SQL para deletar a tabela 'cliente'
cursor.execute(
  """
    DROP TABLE cliente;
  """
)

# Realiza o commit da transação (salva as alterações no banco de dados)
conexao.commit()

# Fecha o cursor
cursor.close()

# Fecha a conexão
conexao.close()

print('Banco de dados criado com sucesso!')
print('Caminho do banco de dados:', banco_caminho)
