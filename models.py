from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

#cria a conexao do seu banco
dv = create_engine("sqlite:///database/banco.db")

# cria a base do banco de dados
base = declarative_base()

#cria classes/tabelas do banco


#executa criaçao dos metadados do seu banco (cria evetivamente o banco de dados)
