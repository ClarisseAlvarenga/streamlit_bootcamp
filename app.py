import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('ANÁLISE DE ÓBITOS 2019-2020')
st.subheader('Aplicação feita durante o Bootcamp da Alura')


dados_2019 = pd.read_csv('./dados/obitos-2019.csv')
dados_2020 = pd.read_csv('./dados/obitos-2020.csv')
st.markdown('Visualizando nossos dados de 2019')
st.dataframe(dados_2019)
st.markdown('Visualizando nossos dados de 2020')
st.dataframe(dados_2020)

