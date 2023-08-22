import streamlit as st
import pandas as pd

data = pd.read_csv('titanic.csv')
selected_sex = st.selectbox('Select sex', data['Sex'].unique())

st.write (f'Selected option:  {selected_sex!r}')