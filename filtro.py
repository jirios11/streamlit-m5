import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title('filtrando ando')
data_url = 'dataset.csv'

@st.cache
def load_data_byname(name):
    #se crea dataframe con nrows, la cantidad de registros a leer
    data = pd.read_csv(data_url)
    filtered_data_byname = data[data['name'].str.contains(name)]
    return filtered_data_byname   

myname = st.text_input('Filtro: ')

if st.button('Flitrar'):
    filterbyname = load_data_byname(myname)
    count_row = filterbyname.shape[0]
    st.write(f'El numero de resultados es {count_row}')
    st.dataframe(filterbyname.groupby('sex').count  ())
    


