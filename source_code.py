import homepage
import avaliar_teste
import historico
import indicadores
import streamlit as st
from globais import *
from configparser import ConfigParser
from PIL import Image

config = ConfigParser()
config.read("parametros.ini")


PAGES = {"Página inicial": homepage,
         "Teste de qualidade da imagem": avaliar_teste,
         "Indicadores adicionais": indicadores,
         "Histórico dos testes": historico,         
         }

criar_pasta_raiz()
verifica_pastas()
pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens, pasta_raiz = carrega_ini()

#Centralizando as imagens
col1, col2, col3 = st.sidebar.columns([1,2,1])

with col1:
    st.write("")

with col2:
    logo = Image.open(pasta_raiz +'Logo.png')
    st.image(logo, width = 100)

with col3:
    st.write("")

st.sidebar.header("Navegação")

selection = st.sidebar.radio("", list(PAGES.keys()))
st.sidebar.write("---")


c1, c2 = st.sidebar.columns(2)
with c1:
    hcpa = Image.open(pasta_raiz +'HCPA.png')
    st.image(hcpa, width = 150)
with c2:
    ufcspa = Image.open(pasta_raiz +'UFCSPA.png')
    st.image(ufcspa, width = 150)


page = PAGES[selection]
page.app()
