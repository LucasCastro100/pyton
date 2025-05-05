import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Book Review Dashboard", page_icon=":book:", layout="wide")
st.title("Book Review Dashboard")

df_reviews = pd.read_csv('files/customer_reviews.csv')
df_top_100 = pd.read_csv('files/top_100_trending_books.csv')

st.sidebar.header("Filtros")

# get_years = sorted(list(df_top_100['year of publication'].unique()), reverse=True)
# get_years.insert(0, "Todos")

# year = st.sidebar.selectbox("Ano de publicação", get_years)

rating_min = df_top_100['rating'].min()
rating_max = df_top_100['rating'].max()
rating = st.sidebar.slider("Avaliação (Livros)", rating_min, rating_max, rating_max)

price_min = df_top_100['book price'].min()
price_max = df_top_100['book price'].max()
price = st.sidebar.slider("Valor (Livros)", price_min, price_max, price_max)

# if year == "Todos":
#     df_top_100_filter = df_top_100[
#         (df_top_100['rating'] <= rating) &
#         (df_top_100['book price'] <= price)
#     ]
# else:
#     df_top_100_filter = df_top_100[
#         (df_top_100['year of publication'] == year) &
#         (df_top_100['rating'] <= rating) &
#         (df_top_100['book price'] <= price)
#     ]

df_top_100_filter = df_top_100[
    (df_top_100['rating'] <= rating) &
    (df_top_100['book price'] <= price)
]

df_top_100_filter

fig = px.bar(df_top_100['year of publication'].value_counts())
st.subheader("Avaliações dos livros")
st.plotly_chart(fig, use_container_width=True)
