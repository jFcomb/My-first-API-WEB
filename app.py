import pandas as pd
import streamlit as st
import scipy.stats
import time

# Variables de estado al ejecutar streamlit
if 'experiment_no' not in st.session_state:
    st.session_state['experiment_no'] = 0
    
if 'df_experiment_results' not in st.session_state:
    st.session_state['df_experiment_results'] = pd.DataFrame(columns = ['no', 'iteraciones', 'media'])

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
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)
        
    return mean

        
# Dibujamos el Slider
number_of_trials = st.slider("¿Cuantos intentos quieres realizar?", 1,1000,10)

# Dibujamos el botón
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso')
    st.session_state['experiment_no'] += 1
    mean = toss_coin(number_of_trials)
    st.session_state['df_experiment_results'] = pd.concat([st.session_state['df_experiment_results'], 
                                                           pd.DataFrame(data=[[st.session_state['experiment_no'],
                                                                               number_of_trials,
                                                                               mean]],
                                                                        columns=['no', 'iterations', 'mean'])
                                                           ],
                                                          axis=0)
    st.session_state['df_experiment_results'] = st.session_state['df_experiment_results'].reset_index(drop=True)

st.write(st.session_state['df_experiment_results'])
