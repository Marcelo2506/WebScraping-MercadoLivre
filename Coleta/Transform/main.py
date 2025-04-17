import pandas as pd
import sqlite3
from datetime import datetime
from sqlalchemy import create_engine

df = pd.read_json(r'data\data.json')

pd.options.display.max_columns = None

# Registrar o link que foi extraído
df['source'] = "https://lista.mercadolivre.com.br/notebook#D[A:notebook]"

# Registrar data da raspagem de dados
df['Data'] = datetime.now()

# Tratando Nulos None converter para 0

df['old_money'] = df['old_money'].fillna('0')
df['new_money'] = df['new_money'].fillna('0')
df['reviews_rating_number'] = df['reviews_rating_number'].fillna('0')
df['reviews_amount'] = df['reviews_amount'].fillna('0')

# Limpando Colunas
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(
    str).str.replace(r'[()]', '', regex=True)

# conversão para números
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)


# Criando Banco de Dados
'''
conn = sqlite3.connect('data/mercadolivre.db')

# Salvar df no banco de dados
df.to_sql('notebook', conn, if_exists='replace', index=False)

# Fechar a conexao
conn.close()
'''

# Acrescentando ao Projeto Exportação Direto para o PostgreSQL

# dados da conexao
usuario = 'postgres'
senha = '2506'
host = 'localhost'
porta = '5432'
banco = 'Mercado Livre'

# criação da engine de conexão
engine = create_engine(
    f'postgresql+psycopg2://{usuario}:{senha}@{host}:{porta}/{banco}')

df.to_sql('Notebooks_WS', con=engine, if_exists='replace', index=False)
