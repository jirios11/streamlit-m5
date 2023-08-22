import streamlit as st
import pandas as pd
import numpy as np

st.title('Prueba netflix')

movies_link = ('movies.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(movies_link, nrows= nrows)
    return data

data = load_data(1000)

if st.sidebar.checkbox('Mostrar todos los filmes'):
    st.subheader('Todos los filmes')
    st.dataframe(data)

titulo = st.sidebar.text_input('Buscar por título')
buscar = st.sidebar.button('Filtar')

if (buscar):
    data_filme = data[data['name'].str.upper().str.contains(titulo.upper())]
    count_rows = data_filme.shape[0]
    st.dataframe(data_filme)

director = st.sidebar.selectbox('Directores', data['director'].unique)

