import streamlit as st
import pandas as pd
import plotly_express as px

# Colocar un titulo al encabezado de la aplicacion que vamos a lanzar. 

st.header("Datos de vehiculos -- Concencionario base de datos")
datos_autos = pd.read_csv("vehicles_us.csv")

#opciones de los usuarios

grafico_histograma = st.checkbox("Generar histograma")
grafico_dispersion = st.checkbox("Generar grafico de dispersion")

# Crear el boton que genera el histograma. 

if grafico_histograma:
    fig = px.histogram(datos_autos, x='odometer', title='Distribución del kilometraje')
    fig.update_layout(bargap = 0.2) 
    st.plotly_chart(fig)   
    
    
if grafico_dispersion:
    
    fig = px.scatter(datos_autos, x='odometer', title='Distribucion del kilometraje')       
    fig.update_layout(bargap = 0.2)         
    st.plotly_chart(fig)                                                                                            
    
                                                                                           
    
    