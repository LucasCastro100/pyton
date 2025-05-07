import streamlit as st
import pandas as pd

st.set_page_config(page_title="Book Review Dashboard", page_icon=":book:", layout="wide")

df_reviews = pd.read_csv('files/customer_reviews.csv')
df_top_100 = pd.read_csv('files/top_100_trending_books.csv')

st.title("Book Reviews")
st.sidebar.header("Filtros")

books = sorted(df_top_100['book title'].unique())
book = st.sidebar.selectbox("Livros", books)

df_top_100_filter = df_top_100[df_top_100['book title'] == book]
df_reviews_filter = df_reviews[df_reviews['book name'] == book]

book_title = df_top_100_filter['book title'].iloc[0]
book_genre = df_top_100_filter['genre'].iloc[0]
book_price = f"${df_top_100_filter['book price'].iloc[0]}"
book_rating = df_top_100_filter['rating'].iloc[0]
book_year = df_top_100_filter['year of publication'].iloc[0]

st.subheader(book_title)

book_genre = ', '.join(sorted([g.strip() for g in book_genre.split(',')]))
st.write("Genereo: ", book_genre)

#metric ele cria como se fosse paineis de dados
col_1, col_2, col_3 = st.columns(3)
col_1.metric("Avaliação", book_rating)
col_2.metric("Preço", book_price)
col_3.metric("Ano lançamento", book_year)
st.divider()

