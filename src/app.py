import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn



def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados



def main():
    st.title('ANÁLISE DE ÓBITOS 2019-2020')
    st.subheader('Aplicação feita durante o Bootcamp da Alura')
    obitos_2019 = carrega_dados('./dados/obitos-2019.csv')
    obitos_2020 = carrega_dados('./dados/obitos-2020.csv')
    st.markdown('Visualizando nossos dados de 2019')
    st.dataframe(obitos_2019)
    st.markdown('Visualizando nossos dados de 2020')
    st.dataframe(obitos_2020)


if __name__ == '__main__':
    main()