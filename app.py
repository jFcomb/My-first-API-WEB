import streamlit as st
import scipy.stats
import time

st.header('Lanzamiento de monedas')

# Agregamos un chart
chart = st.line_chart([0.5])

#Función de emulación de lanzamiento de moneda
def toss_coin(n):
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0
    
    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_nochart.add_rows([mean])
        chart.add_rows([mean])
        time_sleep(0.05)
        
    return mean

        
# Dibujamos el Slider
number_of_trials = st.slider("¿Cuantos intentos quieres realizar?", 1,1000,10)

# Dibujamos el botón
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso')
    mean = toss_coin(number_of_trials)
