import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



def carrega_dados(caminho):
    dados = pd.read_csv(caminho)
    return dados

def grafico_comparativo(dados_2019, dados_2020, causa, estado='BRASIL'):

    if estado == "BRASIL":
        total_2019 = dados_2019.groupby('tipo_doenca').sum()
        total_2020 = dados_2020.groupby('tipo_doenca').sum()
        lista = [int(total_2019.loc[causa]), int(total_2020.loc[causa])]
    else:
        total_2019 = dados_2019.groupby(['uf','tipo_doenca']).sum()
        total_2020 = dados_2020.groupby(['uf','tipo_doenca']).sum()
        lista = [int(total_2019.loc[estado,causa]), int(total_2020.loc[estado,causa])]
    
    dados = pd.DataFrame({'Total': lista,
                           'Ano': [2019, 2020]})
    fig, ax = plt.subplots()
    ax = sns.barplot(x='Ano', y='Total', data=dados)
    ax.set_title(f'Óbitos por {causa} - {estado}', fontsize=20)
    return fig

def main():
    obitos_2019 = carrega_dados('./dados/obitos-2019.csv')
    obitos_2020 = carrega_dados('./dados/obitos-2020.csv')
    tipo_doenca = obitos_2020['tipo_doenca'].unique()
    estado = np.append(obitos_2020['uf'].unique(), 'BRASIL')

    
    st.title('ANÁLISE DE ÓBITOS 2019-2020')
    st.subheader('Aplicação feita durante o Bootcamp da Alura')
    opcao_1 = st.sidebar.selectbox('Selecione o tipo da doença', tipo_doenca)
    opcao_2 = st.sidebar.selectbox('Selecione o Estado', estado)
    figura = grafico_comparativo(obitos_2019, obitos_2020, opcao_1, opcao_2)
    st.pyplot(figura)

    if st.checkbox('Mostre os Dados que originaram o gráfico'):
        st. subheader('Estes foram os dados usados na análise')
        st.markdown('2019')
        st.dataframe(obitos_2019)
        st.markdown('2020')
        st.dataframe(obitos_2020)
    




if __name__ == '__main__':
    main()