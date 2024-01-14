import streamlit as st

st.header('Lanzamiento de monedas')

# Dibujamos el Slider
number_of_trials = st.slider("¿Cuantos intentos quieres realizar?", 1,1000,10)

# Dibujamos el botón
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso')
    
st.write('Esta aplicación aún no es funcional. En construcción.')
