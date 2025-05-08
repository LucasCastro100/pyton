import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_table

st.set_page_config(page_title="CAP", page_icon=":car:", layout="wide")
st.title("CAP")

data_table = get_table('cap_table')

submitted = False
data_tabel_filter = data_table.copy()

with st.form("my_form"):
    col_1, col_2, col_3 = st.columns(3)
    product = col_1.text_input("Cod. Produto", "")
    description = col_2.text_input("Descrição", "")
    marca = col_3.text_input("Marca", "")

    submitted = st.form_submit_button("Pesquisar")
    if submitted:
        data_tabel_filter = data_table[
            (data_table['codigo_fabricante'].astype(str).str.contains(product, case=False)) &
            (data_table['descricao_do_produto'].str.contains(description, case=False)) &
            (data_table['marca'].str.contains(marca, case=False))
        ]

# Exibição dos dados
if not data_tabel_filter.empty:
    if submitted:
        st.success(f"Encontrado {len(data_tabel_filter)} dado(s).")
    st.dataframe(data_tabel_filter, use_container_width=True)
elif submitted:
    st.warning("Nenhum dado encontrado.")