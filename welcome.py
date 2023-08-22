import streamlit as st

def bienvenida(nombre):
    mymensaje = 'Bienvenide ' + nombre
    return mymensaje

myname = st.text_input('Escribe tu nombre:')

if myname:
    mensaje = bienvenida(myname)
    st.write(mensaje)