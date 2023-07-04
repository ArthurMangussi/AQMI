import homepage
import avaliar_teste
import historico
import indicadores
import streamlit as st
from globais import *
from configparser import ConfigParser

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
    logo_image = "https://github.com/ArthurMangussi/AQMI/blob/main/AQMI.png?raw=true"
    st.image(logo_image, width = 100)

with col3:
    st.write("")

st.sidebar.header("Navegação")

selection = st.sidebar.radio("", list(PAGES.keys()))
st.sidebar.write("---")


c1, c2 = st.sidebar.columns(2)
with c1:
    logo_hcpa = "https://github.com/ArthurMangussi/AQIM/blob/main/HCPA.png?raw=true"
    st.image(logo_hcpa, width = 150)
with c2:
    logo_ufcspa = "https://github.com/ArthurMangussi/AQIM/blob/main/ufcspa.png?raw=true"
    st.image(logo_ufcspa, width = 150)


page = PAGES[selection]
page.app()
