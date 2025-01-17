import streamlit as st
import os
# Configuración inicial
st.set poge config(layout="wide")
# Página de inicio st. title("Proyecto Final")
st.markdown("""
## Bienvenido
Este proyecto incluye las siguientes páginas:
""")
# Sección de páginas con título y imagenes 
col1, col2 = st.columns([2, 2])
with col1:
st.markdown("<div class="column">", unsafe_allow_html=True)
st.image("utils/1.png", width=250)
st.markdown("</div>", unsafe_allow_html=True)
with col2:
st.subheader ("EDA: Análisis exploratorio de datos")
st.markdown("Examina los datos y descubre patrones interesantes.")
col3, col4 = st. columns([2, 2])
with col3:
st.markdown("«div class="column">", unsafe_allow_html=True)
st.image("utils/2.png", width=250)
st.markdown("</div>", unsafe_allow_html=True)
with col4:
st.subheader ("Hipótesis: Visualización de hipótesis propuestas")
st.markdown("Evalúa diferentes hipótesis mediante gráficos interactivos.")
col5, col6 = st.columns([2, 2])
with col5:
st.markdown("«div class="column">", unsafe_allow_html=True)
st.image("utils/3.png", width=250)
st.markdown("</div>", unsafe_allow_html=True)
with col6:
st.subheader ("Modelo: Predicciones con diferntes tipos de modelos")
st.markdown("Genera predicciones y evalúa el desempeño del modelo")
