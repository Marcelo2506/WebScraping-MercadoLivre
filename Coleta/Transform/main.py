import pandas as pd
import sqlite3
from datetime import datetime

df = pd.read_json(r'data\data.json')

pd.options.display.max_columns = None

# Registrar o link que foi extraído
df['source'] = "https://lista.mercadolivre.com.br/notebook#D[A:notebook]"

# Registrar data da raspagem de dados
df['Data'] = datetime.now()

# Limpando Colunas
df['old_money'] = df['old_money'].astype(str).str.replace('.', '', regex=False)
df['new_money'] = df['new_money'].astype(str).str.replace('.', '', regex=False)
df['reviews_amount'] = df['reviews_amount'].astype(
    str).str.replace('[\(\)]', '', regex=False)

# conversão para números
df['old_money'] = df['old_money'].astype(float)
df['new_money'] = df['new_money'].astype(float)
df['reviews_amount'] = df['reviews_amount'].astype(int)
df['reviews_rating_number'] = df['reviews_rating_number'].astype(float)

# None converter para 0


print(df)
