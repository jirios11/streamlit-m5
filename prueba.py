import pandas as pd
import streamlit as st

new_file = 'dataset.csv'
df = pd.read_csv(new_file)

#Comentario
#Crear pagina web

st.title ('Prueba streamlit pandas')

#Imprimir dataframe
st.dataframe(df)