import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title('DSAI M5 Reto')
st.header('Josue Isaac Rios Muñoz')

DATA_URL = 'Employees.csv'

@st.cache
def data_default(nrows):
    data = pd.read_csv(DATA_URL, nrows = nrows)
    return data
def data_total():
    data = pd.read_csv(DATA_URL)
    return data

def filter_data_by_ID(ID):
    en_data = data[data['Employee_ID'].str.upper().str.contains(ID)]
    return en_data

def filter_data_by_Ht(Ciudad):
    en_data = data[data['Hometown'].str.upper() == Ciudad.upper()]
    return en_data

def filter_data_by_Area(Area):
    en_data = data[data['Unit'].str.upper() == Area.upper()]
    return en_data

def filter_data_by_El(Nivel_educativo):
    en_data = data[data['Education_Level'] == Nivel_educativo]
    return en_data

def filter_data_by_ciudad(Ciudad):
    en_data = data[data['Hometown'] == Ciudad]
    return en_data

def filter_data_by_unidad(unidad):
    en_data = data[data['Unit'] == unidad]
    return en_data

st.sidebar.title('Barra lateral')

data = data_default(500)

if st.sidebar.checkbox('Mostrar toda la información'):
    data = data_total()
    

st.dataframe(data)

#Se crea la sección de filtros y los respectivos cajas de texto/botones
st.sidebar.header('Filtros')
st.sidebar.subheader('Cajas de texto')

Employee_ID = st.sidebar.text_input('Buscar ID')
boton_filtro_ID = st.sidebar.button('Filtrar por ID')

Ciudad = st.sidebar.text_input('Buscar Ciudad')
boton_filtro_HT = st.sidebar.button('Filtrar por ciudad')

Area = st.sidebar.text_input('Buscar area')
boton_filtro_Un = st.sidebar.button('Filtrar por área')

if (boton_filtro_ID):
    data_ID = filter_data_by_ID(Employee_ID)
    countrows = data_ID.shape[0]
    st.write(f'El el número de empleados con ese ID es: {countrows}')
    st.dataframe(data_ID)

if (boton_filtro_HT):
    data_Ht = filter_data_by_Ht(Ciudad)
    countrows = data_Ht.shape[0]
    st.write(f'El numero de empleados de {Ciudad} es de {countrows}')
    st.dataframe(data_Ht)

if (boton_filtro_Un):
    data_Un = filter_data_by_Area(Area)
    countrows = data_Un.shape[0]
    st.write(f'El numero de empleados en {Area} es de {countrows}')
    st.dataframe(data_Un)

st.sidebar.subheader('Listas desplegables')

#Selectbox para filtrar por nivel educativo

E_level = st.sidebar.selectbox('Elige nivel educativo', sorted(data['Education_Level'].unique()))

data_El = filter_data_by_El(E_level)
countrows = data_El.shape[0]
st.write (f'Los empleados con nivel educativo {E_level} son {countrows}')
st.dataframe(data_El)

#Selectbox para filtrar por ciudad que participó en el estudio

ciudad_sel = st.sidebar.selectbox('Seleccione la ciudad', data['Hometown'].unique())

data_ciudad = filter_data_by_ciudad(ciudad_sel)
countrows = data_ciudad.shape[0]
st.write (f'Los empleados de {ciudad_sel} son {countrows}')
st.dataframe(data_ciudad)

#Selectbox por unit
Unidad_sel = st.selectbox('Seleccione la ciudad', data['Unit'].unique())

data_unidad = filter_data_by_unidad(Unidad_sel)
countrows = data_unidad.shape[0]
st.write (f'Los empleados de {Unidad_sel} son {countrows}')
st.dataframe(data_unidad)

#Histograma de empleados por edad

st.subheader('Histograma por edades')
fig, ax = plt.subplots()

ax.hist(data['Age'])
ax.set_xlabel('Edad')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

#Frecuencias por area
st.subheader('Grafica de frecuencias por area')

fig2, ax2 = plt.subplots()
data_by_unit = data[['Unit', 'Employee_ID']].groupby('Unit').count()
#st.dataframe(data_by_unit) linea para corroborar el df resumen
ax2 = st.bar_chart(data_by_unit)

st.pyplot(fig2)

#Ciudades con mayor indice de deserción
st.title('Indice de deserción por ciudad')
fig3, ax3 = plt.subplots()

ar_hometown = data[['Hometown','Attrition_rate']].groupby('Hometown').mean()
ax3 = st.line_chart(ar_hometown)

st.pyplot(fig3)

#Indice de desercion por edad
st.title('Indice de desercion por edad')
fig4, ax4 = plt.subplots()
ax4.scatter(np.log(data['Age']), data['Attrition_rate'])
st.pyplot(fig4)

#Indice de desercion por tiempo de servicio
st.title('Indice de desercion por tiempo de servicio')
fig5, ax5 = plt.subplots()
ax5.scatter(data['Time_of_service'],data['Attrition_rate'])
st.pyplot(fig5)