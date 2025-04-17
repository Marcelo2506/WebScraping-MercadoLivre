
import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect(r'data\mercadolivre.db')

df = pd.read_sql_query("SELECT * FROM notebook", conn)

print('Conexão feita!')

conn.close()

print('Conexão fechada!')

st.title('📊 Pesquisa de Mercado - Notebooks no Mercado Livre')

st.subheader("💡 Principais KPI'S")
col1, col2, col3 = st.columns(3)

# KPI 1 TOTAL DE ITENS
total_itens = df.shape[0]
col1.metric(label="🖥️ Total de Notebooks", value=total_itens)

# KPI 2 NÚMERO DE MARCAS NO MERCADO
unique_brands = df['brand'].nunique()
col2.metric(label="Marcas Únicas", value=unique_brands)

# KPI 3 Preço atual
average_new_money = df['new_money'].mean()
col3.metric(label='Preço Médio (R$)', value=f"{average_new_money:.2f}")

# Marcas mais frequentes
st.subheader('🏆 Marcas mais encontradas do catálogo:')
col1, col2 = st.columns([4, 2])
top_brands = df['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_brands)
col2.write(top_brands)

# Preço Médio por Marca
st.subheader('💵 Preço Médio por Marca')
col1, col2 = st.columns([4, 2])
df_non_zero_prices = df[df['new_money'] > 0]
average_price_by_brand = df_non_zero_prices.groupby(
    'brand')['new_money'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Satisfação por marca
st.subheader('⭐ Satisfação Média por Marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby(
    'brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)
