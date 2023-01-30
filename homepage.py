import pandas as pd
from scipy.stats import skew, kurtosis
import streamlit as st
import tkinter as tk
from tkinter import filedialog
import time


from globais import *

#Layout
st.set_page_config(layout="wide")

def form_callback():
    pass    
    
def muda_caminho_app(dirname):
        atualiza_ini("path", "pasta_raiz", dirname + "/")
        pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens, pasta_raiz = carrega_ini()
        verifica_pastas()
        verifica_csv(pasta_csv)
        return pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens,  pasta_raiz

def app():

    verifica_pastas()
    pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens, pasta_raiz = carrega_ini()
    verifica_csv(pasta_csv)

    #st.title('Software QCQIM')
    st.markdown("<h1 style='text-align: center; color: bold;'> Software AQIM </h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: bold;'> Avaliação da Qualidade de Imagens Mamográficas </h2>", unsafe_allow_html=True)
    
    st.write("*Desenvolvido por Arthur Dantas Mangussi* ")
    st.write("*Orientado por Professora Doutora Viviane Rodrigues Botelho e Professora Doutora Thatiane Alves Pianoschi*")
    st.markdown('### Orientações para aquisição e armazenamento da imagem')
    st.write('''
                
                1) Posicione o objeto simulador no mamógrafo, de forma que fique centralizado no detector;
                2) Abaixe a bandeja de compressão para que ela apenas toque a parte superior do *phantom*;
                3) Verifique se o sensor do Controle Automático de Exposição (CAE) está abaixo do centro do *phantom* e no mesmo posicionamento de aquisição anteriores;
                4) Faça uma exposição usando os parâmetros clinicamente utilizados para uma mama comprimidade de 4,5 cm com densidade média;
                5) Exportar a imagem para uma *workstation* com o AQIM instalado;
                6) Selecionar o diretório de armazenamento;
                7) Verificar se o ID correspondente ao equipamento avaliado está cadastrado. Caso não esteja, realizar a inclusão do equipamento;
                8) Fazer *upload* da imagem no módulo "Teste de qualidade da imagem".
                

                ''')
    
    st.write('---')
    
    # Set up tkinter
    root = tk.Tk()
    root.withdraw()

    # Make folder picker dialog appear on top of other windows
    root.wm_attributes('-topmost', 1)

    # Folder picker button
    st.write(" Diretório de armazenamento: " + pasta_raiz )
    clicked = st.button('Alterar diretório de armazenamento')
    
    if clicked:
        dirname = st.text_input('Diretório selecionado:', filedialog.askdirectory(master=root))
        if arruma_path(dirname) != pasta_raiz:
            pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens, pasta_raiz = muda_caminho_app(dirname)            
        

    df_equipamentos = pd.read_csv(pasta_csv + '/Header.csv', sep=';')
    
    list_df_equipamentos = list(df_equipamentos.id)
    
    equipamentos = st.selectbox('Visualizar equipamentos cadastrados:',list_df_equipamentos )
  
    #cadastro_equipamento = st.selectbox('',['Clique aqui para cadastrar novo equipamento','Cadastrar novo'])
    cadastro_equipamento = st.checkbox('Selecione para cadastrar novos equipamentos')
    
    if cadastro_equipamento:
        form = st.form(key='my_form')
        list_respostas = []
        a = form.number_input('Quantos equipamentos deseja cadastrar?', min_value = 0, max_value = 10, step=1)
        a = int(a)
        submit_button = form.form_submit_button(label = 'Avançar', on_click = form_callback)

        st.markdown("### ID dos equipamentos") 
    
        df = pd.read_csv(pasta_csv + '/Header.csv', sep=';')

        for i in range(a):
            respota = st.text_input(f'Digite o identificador do equipamento {i+1}: ')
            df.loc[len(df.index)] = [respota]
            list_respostas.append(respota)

        button_save = st.button('Salvar dados de cadastro')
        if button_save:
            #df_dados_salvos = pd.DataFrame({"id":list_respostas})
            df.to_csv(pasta_csv+'/Header.csv', sep=';',index=False)
            with st.spinner('Carregando...'):
                time.sleep(1.2)
            st.success('Informações preenchidas e salvas com sucesso!')


       
              
        