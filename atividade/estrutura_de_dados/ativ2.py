# ==========================================
# Exercício: Estrutura de dados
# Arquivo: ativ2.py
# Objetivo: mostrar como usar lista, dicionário e DataFrame em Streamlit.
# ==========================================

import pandas as pd
import streamlit as st

# Configura a página do app Streamlit com título, ícone e layout largo.
st.set_page_config(page_title="Painel de vendas", page_icon="📦", layout="wide")

# 1) Criando uma lista com valores em ordem.
# A lista guarda vários itens em sequência, como uma fila de dados.
lista = ["a", "b", "c", "d", "e"]

# 2) Acessando o primeiro elemento da lista.
# Em Python, o índice 0 representa o primeiro item da lista.
primeiro_item = lista[0]

# 3) Criando um dicionário com chaves e valores.
# O dicionário armazena informações em pares: chave -> valor.
# Exemplo: "01" é a chave e 10001 é o valor correspondente.
dic = {"01": 10001, "02": 10002, "03": 10003}

# Acessa o valor que está associado à chave "01".
valor_dic = dic["01"]

# 4) Criando um dicionário com listas de dados.
# Cada chave vira uma coluna da tabela e cada lista vira uma coluna de valores.
# A posição 0 de cada lista está ligada à mesma linha.
dados = {
    "produto": ["arroz", "feijao", "farinha", "sal"],
    "quantidade": [2300, 2900, 3000, 4000],
    "preco": [20.50, 18.90, 27.50, 12.50]
}

# 5) Transformando o dicionário em uma tabela (DataFrame).
# DataFrame é uma estrutura da biblioteca pandas que organiza os dados em colunas e linhas.
df = pd.DataFrame(dados)

# Cria uma nova coluna chamada valor_total, calculando quantidade * preco.
df["valor_total"] = df["quantidade"] * df["preco"]

# 6) Filtros na barra lateral.
# A sidebar permite selecionar quais produtos aparecerão no painel.
st.sidebar.header("Filtros")
produtos_selecionados = st.sidebar.multiselect(
    "Selecione os produtos:",
    options=df["produto"].unique(),
    default=df["produto"].unique().tolist(),
)

# Filtra o DataFrame de acordo com os produtos escolhidos.
# Se nenhum produto for selecionado, retorna uma tabela vazia.
df_filtrado = df[df["produto"].isin(produtos_selecionados)] if produtos_selecionados else df.iloc[0:0]

# 7) Métricas da página.
# As métricas mostram resumos rápidos do conjunto de dados.
st.title("📦 Painel de vendas")

col1, col2, col3 = st.columns(3)
col1.metric("Total em estoque", f"{df_filtrado['quantidade'].sum():,} kg")
col2.metric("Valor total", f"R$ {df_filtrado['valor_total'].sum():,.2f}")

# Se a tabela não estiver vazia, mostra o produto com maior quantidade.
# Caso contrário, mostra "Nenhum".
col3.metric("Produto com maior quantidade", df_filtrado.loc[df_filtrado['quantidade'].idxmax(), 'produto'] if not df_filtrado.empty else "Nenhum")

# 8) Exibindo a lista e o dicionário na interface.
with st.container():
    st.subheader("Lista")
    st.write(lista)
    st.write(f"Primeiro item da lista: {primeiro_item}")

    st.subheader("Dicionário")
    st.json(dic)
    st.write(f"Valor da chave 01: {valor_dic}")

# 9) Tabela e gráfico.
# Exibe os dados filtrados em formato de tabela e depois em gráfico de barras.
st.subheader("Produtos")
st.dataframe(df_filtrado, use_container_width=True)

if not df_filtrado.empty:
    st.subheader("Quantidade por produto")
    st.bar_chart(df_filtrado.set_index("produto")["quantidade"])
else:
    st.warning("Nenhum produto selecionado. Ajuste os filtros na barra lateral.")