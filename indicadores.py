import matplotlib.pyplot as plt
import os
import pandas as pd
from scipy.stats import skew, kurtosis
import streamlit as st
from PIL import Image
from globais import *


# Função para plotar a imagem
def plot_image(img, nome):
    fig, ax = plt.subplots()
    ax.imshow(img,cmap='gray')
    ax.set_title(f'{nome}', fontsize=8)
    return fig


def app():
   
    pasta_csv, pasta_indicadores, pasta_sala_equipamento, pasta_sala_imagens, pasta_raiz = carrega_ini()
    st.title("Indicadores adicionais")
    st.write("Indicadores de qualidade da imagem não exigidos pela IN N° 92 da RDC 611 ANVISA.")
    referencias = st.expander('Descrição')
    with referencias:
        st.write('''
        Segundo Borg (2012), as métricas mais utilizadas para avaliar a qualidade da imagem são a Razão Sinal Ruído e a Razão Contraste Ruído. Ademais, a Figura de Mérito também é utilizada como um indicador de qualidade. Logo, nessa aba do ambiente virtual será possível analisar esses indicadores de qualidade da imagem não exigidos pela IN N° 92. 
        
         - Histograma comparativo: é uma comparação de um histograma de uma imagem adequada a avaliação do teste com a imagem que está sendo avaliada;
        - Razão Sinal Ruído (*Signal to Noise Ratio - SNR*) é obtida pela razão do sinal em uma região de interesse pelo ruído associado¹;''')
        st.latex(r'''
                    SNR = \frac{\bar{X}_{BG}}{\sigma_{BG}}
                    ''') 
        st.write('''
        - Razão Contraste Ruído (*Contrast to Noise Ratio - CNR*): permite identificar a sensibilidade na detecção de estruturas, além de descrever a amplitude do sinal em relação ao ruído de fundo em uma imagem ²;''')
        st.latex(r'''
                    CNR = \frac{\bar{X}_{ROI} - \bar{X}_{BG}}{\sigma_{BG}}
                    ''')
        st.write('''- Figura de Mérito: é um indicador de qualidade, que relaciona a qualidade da imagem com a dose necessária para produzir a mesma³. ''')
        st.latex(r'''
                    FOM = \frac{CNR^2}{DGM}
                ''')
        st.markdown(r" em que $\bar{X}_{BG}$ é o valor médio do fundo (BG), $\sigma_{BG}$ é o desvio padrão do fundo, $\bar{X}_{ROI}$ é o valor médio da ROI, DGM é a Dose Glandular média, retirada da tag DICOM (0040, 0316) Organ Dose (mGy) e CNR é a razão contraste-ruído.")     
        st.write(''' --- ''')
        st.write( '''
        BORG, M.; BADR, I.; ROYLE, G. The use of a figure-of-merit (fom) for optimisation in digital mammography: a literature review. Radiation Protection Dosimetry, v. 151, n. 1, p.81–88, 2012. \n
        1 - Martí Villarreal, Oscar Ariel. Otimização da mamografia digital variando a glandularidade. Dissertação (Mestrado) - Ilhéus, BA: UESC, 2019.\n 
        2 - GUZMÁN, V. C.; RESTREPO, H. D. B.; HURTADO, E. S. Natural scene statistics of mammography accreditation phantom images. XXII Symposium on Image, Signal Processing and Artificial Vision, 2019. \n
        3 - XAVIER, A. C. da S. Dosimetria e qualidade da imagem em mamografia digital. Dissertação (Mestrado) — Universidade Federal de Pernambuco, 2015.
        
        ''')
    st.info(f'Diretório de armazenamento do teste: {pasta_indicadores}')
    #st.write(st.session_state.path_sala_imagens)
    list_respostas_diretorio = os.listdir(pasta_sala_equipamento)
    
    
    list_respostas = []
    for i in list_respostas_diretorio:
        i = i[:-4]
        list_respostas.append(i)
      
    list_respostas.insert(0,'')
    
    #st.markdown('### Mamografia')
    escolha_imagem = st.selectbox('Selecione o ID que deseja analisar os indicadores adicionais', list_respostas,
                                      format_func = lambda x: 'Selecione uma opção' if x == '' else x)
    
    if escolha_imagem == '':
        st.empty()
    else:
        imagens_diretorio = os.listdir(pasta_sala_imagens+f'\{escolha_imagem}')
            
        list_respostas = []
        for i in imagens_diretorio:
            i = i[:-4]
            list_respostas.append(i)

        list_respostas.insert(0,'')

        option = st.selectbox('Selecione a imagem', list_respostas,
                                      format_func = lambda x: 'Selecione uma opção' if x == '' else x)
        
        if option == '':
            st.empty()
        else:
            st.write(f'### Indicadores adicionais da imagem {option}')
            
            st.markdown("### Imagem")
                                
            aa =f'{pasta_sala_imagens}\{escolha_imagem}\{option}.png'
                
            image = Image.open(aa)
            st.image(image, caption = f'Imagem: {option}')
                
            caminho_sala_escolhida = pasta_sala_equipamento + f'\{escolha_imagem}.csv'
            dados = pd.read_csv(caminho_sala_escolhida, sep = ';' )
            # Buscando os dados 
            for i in range(0, len(list_respostas) - 1):
                if dados.iloc[i]["Nome da Imagem"] == option+'.dcm':
                    linha = dados.iloc[i]
                    break
            
            
            st.markdown("### Razão Sinal Ruído (SNR), Razão Contraste Ruído (CNR) e Figura de Mérito (FOM)")
            path_indicadores_cnr = pasta_indicadores+ f'\ CNR {option}'+ '.dcm' + '.png'
            file_cnr = Image.open(path_indicadores_cnr)
            
            #Indicadores adicionais
            coluna_hist, coluna_indicadores = st.columns([2,1])
            with coluna_hist:
                st.image(file_cnr, caption = f'ROIs para CNR da imagem {option}')
            with coluna_indicadores:
                #st.markdown("##### Razão Sinal Ruído")
                st.markdown(f'**SNR** = {float(linha.SNR):.7f}')
                #st.markdown("##### Razão Contraste Ruído")
                st.markdown(f'**CNR** = {float(linha.CNR):.7f}')
                a = linha['Dose (dGy)'][1:-1] 
                aa = linha.CNR ** 2
                aaa = float(a) * 100
                FOM = aa /  aaa
                #st.markdown("##### Figura de Mérito")
                st.markdown(f'**FOM** = {float(FOM):.7f}')   
                calc1 = f'{linha.X_BG:.5f}'
                calc2 = f'{linha.X_ROI:.5f}'
                calc3 = f'{linha.Sigma:.5f}'
                st.write(r'$\bar{X}_{BG}$ =', calc1) 
                st.write(r'$\bar{X}_{ROI}$ =', calc2) 
                st.write(r'$\sigma_{BG}$ =', calc3)
            
            # Buscando as métricas do histograma    
            col1, col2 = st.columns([2,1])
            with col1:
                st.markdown("### Histograma")
                iuug = Image.open(pasta_indicadores + f'\ {option}'+'.dcm'+ '.png')
                st.image(iuug, caption = f'Histograma da imagem {option}')
            with col2:
                st.markdown('### Métricas estatísiticas')
                st.write(f"Média: {float(linha.Media):.4f}")  
                st.write(f"Variância: {float(linha.Variancia):.4f}")
                st.write(f"Assimetria: {float(linha.Assimetria):.4f}")
                st.write(f"Curtose: {float(linha.Curtose):.4f}")         
            
            espaco_vazio = st.empty()
            espaco_vazio.write('')
            
            
            
            
            
                
            
            
            
                
                