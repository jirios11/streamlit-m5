import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

new_file = 'dataset.csv'

@st.cache
def load_data(nrows):
    #se crea dataframe con nrows, la cantidad de registros a leer
    data = pd.read_csv(new_file, nrows=nrows)
    return data   

st.title('Pie chart genero')


data = load_data(1000)

sns.countplot(data, x = 'sex')
plt.show()
