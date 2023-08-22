import streamlit as st
import pandas as pd

st.title('Streamlit con cache')
#set dataset url 
DATA_URL = 'dataset.csv'

@st.cache
def load_data(nrows):
    #se crea dataframe con nrows, la cantidad de registros a leer
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data   

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done ! using cache...')

st.dataframe(data)
