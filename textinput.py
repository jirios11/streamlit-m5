import streamlit as st
import pandas as pd

st.title('Usando cajas de texto')

my_name = st.text_input('Nombre: ')

if (my_name):
    st.write(f'Tu nombre es: {my_name}')