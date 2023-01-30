import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.stats import skew, kurtosis
import streamlit as st
import plotly.express as px

from globais import *


def app():
    pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens, pasta_raiz = carrega_ini()

    st.title("Histórico dos testes")
    st.markdown(
        "### Dados da contagem de estruturas para as avaliações realizadas")
    # st.write(st.session_state.resultados_contagem)

    list_respostas_diretorio = os.listdir(pasta_sala_equipamento)

    list_respostas = []
    for i in list_respostas_diretorio:
        i = i[:-4]
        list_respostas.append(i)

    list_respostas.insert(0, '')

    
    st.info(f'Diretório de armazenamento do teste: {pasta_sala_equipamento}')
    escolha_equipamento = st.selectbox('ID do equipamento', list_respostas,
                                       format_func=lambda x: 'Selecione uma opção' if x == '' else x)

    if escolha_equipamento == '':
        st.empty()
    else:
        escolha_equipamento = escolha_equipamento + '.csv'
        st.markdown(f"## {escolha_equipamento[:-4]}")
        aa = os.path.join(pasta_sala_equipamento, escolha_equipamento)
        id_sala_um = pd.read_csv(aa, sep=";")
        st.write(id_sala_um)
        st.markdown(f'## Gráficos {escolha_equipamento[:-4]}')

        st.write('### Período de visualização das avaliações')
        col1, col2 = st.columns(2)
        with col1:
            data_inicio = st.selectbox(
                'Selecione a data de ínicio do período', id_sala_um['Data da avaliação'])

        with col2:
            data_fim = st.selectbox(
                'Selecione a data de fim do período', id_sala_um['Data da avaliação'])

            #data_fim = st.selectbox('Selecione a data de ínicio do período', [datetime.date.today()])

        with col1:
            st.write('### Fibras')
            linha_base_fibras = []
            for i in range(len(id_sala_um['Fibras'])):
                linha_base_fibras.append(4)

            fig, ax = plt.subplots()
            ax.plot_date(id_sala_um['Data da avaliação'], id_sala_um.Fibras)
            ax.plot(id_sala_um['Data da avaliação'], linha_base_fibras, 'r--')
            ax.grid()
            fig.autofmt_xdate()
            ax.set_ylim(0, 6.5)
            ax.set_xlim([data_inicio, str(data_fim)])
            ax.set_title('Históricos fibras visualizadas')
            plt.tight_layout()
            st.pyplot(fig)

        with col2:
            st.write('### Microcalcifiações')
            linha_base_specks = []
            for i in range(len(id_sala_um['Microcalcificações'])):
                linha_base_specks.append(3)

            fig, ax = plt.subplots()
            ax.plot_date(id_sala_um['Data da avaliação'],
                         id_sala_um['Microcalcificações'])
            ax.plot(id_sala_um['Data da avaliação'], linha_base_specks, 'r--')
            ax.grid()
            fig.autofmt_xdate()
            ax.set_ylim(0, 5.5)
            ax.set_xlim([data_inicio, str(data_fim)])
            ax.set_title('Históricos Microcalcificações visualizadas')
            plt.tight_layout()
            st.pyplot(fig)

        with col1:
            st.write('### Massas')
            fig, ax = plt.subplots()
            ax.plot_date(id_sala_um['Data da avaliação'], id_sala_um['Massas'])
            ax.plot(id_sala_um['Data da avaliação'], linha_base_specks, 'r--')
            ax.grid()
            fig.autofmt_xdate()
            ax.set_ylim(0, 5.5)
            ax.set_xlim([data_inicio, str(data_fim)])
            ax.set_title('Históricos Massas visualizadas')
            plt.tight_layout()
            st.pyplot(fig)

        with col2:
            st.write('### CNR')
            fig, ax = plt.subplots()
            ax.plot_date(id_sala_um['Data da avaliação'], id_sala_um['CNR'])
            ax.grid()
            fig.autofmt_xdate()
            ax.set_xlim([data_inicio, str(data_fim)])
            ax.set_title('Histórico do indicador: CNR')
            plt.tight_layout()
            st.pyplot(fig)

        
        #st.markdown(f'### Gráfico de dispersão')
        #st.write(f'Os valores médios da matriz de pixel de cada imagem *versus* sua variância')
        #col3, col4 = st.columns([2, 1])
        #with col3:
        #    fig1 = px.scatter(id_sala_um, x='Media', y='Variancia',
                             # color='Parecer', hover_data=['Nome da Imagem'])
            #st.plotly_chart(fig1)
