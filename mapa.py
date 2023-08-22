import streamlit as st
import pandas as pd
import numpy as np

#Titulo
st.title('Mapa prueba')
st.header('espacio para probar mapas')

map_data = pd.DataFrame(np.random.randn(20,2)/[50,50]+ [37.76, -122.4],columns = ['lat', 'lon'])

st.map(map_data)

