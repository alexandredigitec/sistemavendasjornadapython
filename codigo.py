# título - Sistema de Vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # quando eu clicar no botão -> adicinonar a venda na tabela
# Seção Vendas Cadastradas
    # Tabela com as Vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por Vendedor
    # Gráfico de Pizza -> Venda por produto

# pip install streamlit pandas plotly
# streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")


# seção de cadastro de vendas

st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1, min_value=0)
valor = st.sidebar.number_input("Valor", min_value=0.00)
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

# lógica de cadastro
if botao_cadastrar:
    if valor == 0 or quantidade == 0 or vendedor == "":
        st.warning("Verifique os campos preenchidos!")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas) # Informa quantas linhas possui a tabela
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada!")

# seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas) # Dataframe é o nome que o panda dá para uma tabela


# seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
#st.metric("Faturamento Total", f"R$ {faturamento}")
st.metric("Faturamento Total", f"R$ {faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

# Gráfico de Barra/Coluna -> Venda por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)