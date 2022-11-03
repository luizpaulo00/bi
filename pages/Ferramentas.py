import streamlit as st
import time
import pandas as pd
import numpy as np
from datetime import datetime
import pandas as pd
import seaborn as sns
import plotly.express as px
from openpyxl import Workbook
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder, JsCode
from tqdm import tqdm
import matplotlib.pyplot as plt
import mysql.connector 
import sqlalchemy   
from datetime import date
from scipy import stats
import mysql.connector
import pandas as pd
import plotly.express as px
from plotly import graph_objects as go
import psycopg2
import warnings
import pickle
from deta import Deta
import json
Data_Hoje = pd.to_datetime(date.today(),errors="coerce")
import streamlit.components.v1 as components
st.set_page_config(page_icon="https://7lm.com.br/wp-content/themes/7lm/build/img/icons/assinatura_7lm.png", layout="wide", page_title="GRUPO IMERGE | FERRAMENTA")

img = "assets/logo7lm.png"
st.sidebar.image(image=img, use_column_width=True,caption="Dashboard-Comercial")

img = "assets/logo7lm.png"
img1 = "assets/login.png"
img2 = "assets/Resultado.png"
img3 = "assets/novos_negocios.png"
img4 = "assets/Imagem_001.png"

st.title("# FERRAMENTAS | DIVERSAS | MELHORIA ")
tab1, tab2, tab3, tab4 = st.tabs(["Resumo_de_Texto", "Viabilidade_Economica", "Extração_Texto_PDF", "Pergunte para o Jarvi"])

with tab1:
    import transformers
    from transformers import pipeline
    import spacy
    import re
    import nltk
    import string
    import numpy as np
    import networkx as nx
    from goose3 import Goose
    #pln = spacy.load('pt_core_news_sm')
    
    nltk.download('punkt')
    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('portuguese')
    print(stopwords)
    
    
    
    
    
    
    
    
    def sumarizar_lematizacao(texto, quantidade_sentencas):
        texto_original = texto
        # Chamada para a outra função de pré-processamento
        texto_formatado = preprocessamento_lematizacao(texto_original)

        frequencia_palavras = nltk.FreqDist(nltk.word_tokenize(texto_formatado))
        frequencia_maxima = max(frequencia_palavras.values())
        for palavra in frequencia_palavras.keys():
            frequencia_palavras[palavra] = (frequencia_palavras[palavra] / frequencia_maxima)
        lista_sentencas = nltk.sent_tokenize(texto_original)
        
        nota_sentencas = {}
        for sentenca in lista_sentencas:
            for palavra in nltk.word_tokenize(sentenca):
                if palavra in frequencia_palavras.keys():
                    if sentenca not in nota_sentencas.keys():
                        nota_sentencas[sentenca] = frequencia_palavras[palavra]
                    else:
                        nota_sentencas[sentenca] += frequencia_palavras[palavra]

        import heapq
        melhores_sentencas = heapq.nlargest(quantidade_sentencas, nota_sentencas, key=nota_sentencas.get)

        return lista_sentencas, melhores_sentencas, frequencia_palavras, nota_sentencas    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def visualiza_resumo(titulo, lista_sentencas, melhores_sentencas):
        texto = ''
        st.markdown(HTML(f'<h1>Resumo do texto - {titulo}</h1>'),unsafe_allow_html=True)
        for i in lista_sentencas:
            if i in melhores_sentencas:
                texto += str(i).replace(i, f"<mark>{i}</mark>")
            else:
                texto += i
        st.markdown(HTML(f""" {texto} """),unsafe_allow_html=True)
        
        
    def preprocessamento_lematizacao(texto):
        texto = texto.lower()
        texto = re.sub(r" +", ' ', texto)

        documento = pln(texto)
        tokens = []
        for token in documento:
            tokens.append(token.lemma_)
        
        tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation]
        texto_formatado = ' '.join([str(elemento) for elemento in tokens if not elemento.isdigit()])
    
        return texto_formatado

    def preprocessamento(texto):
        texto_formatado = texto.lower()
        tokens = []
        for token in nltk.word_tokenize(texto_formatado):
            tokens.append(token)

        tokens = [palavra for palavra in tokens if palavra not in stopwords and palavra not in string.punctuation]
        texto_formatado = ' '.join([str(elemento) for elemento in tokens if not elemento.isdigit()])

        return texto_formatado

    espaco = st.container()


    with st.sidebar.expander("LINK PARA SCRAPING:"):
        with st.form(key="90oooa"):
            LINk = st.text_input("link", value="https://www.clickhabitacao.com.br/artigos/programa-casa-verde-e-amarela-pcva/")
            bt_001 = st.form_submit_button("BUSCAR_TEXTO")
        if bt_001:
            st.success("BUSCA FINALIZADA")
            with espaco:
                try:
                    g = Goose()
                    url = LINk
                    artigo = g.extract(url)
                    text = artigo.cleaned_text
                    texto_original = re.sub(r'\s+', ' ', text)
                    c1, c2 = st.columns((3,3))
                    c1.subheader("TEXTO_ORIGINAL:")
                    c1.text_area(label="Texto Original",value=texto_original, height=800)
                    c2.subheader("TEXTO_RESUMIDO:")
                    texto_formatado = preprocessamento(texto_original)
                    frequencia_palavras = nltk.FreqDist(nltk.word_tokenize(texto_formatado))    
                    frequencia_maxima = max(frequencia_palavras.values())
                    for palavra in frequencia_palavras.keys():
                        frequencia_palavras[palavra] = (frequencia_palavras[palavra] / frequencia_maxima)
                    lista_sentencas = nltk.sent_tokenize(texto_original)
                    nota_sentencas = {}
                    for sentenca in lista_sentencas:
                    #print(sentenca)
                        for palavra in nltk.word_tokenize(sentenca.lower()):
                            #print(palavra)
                            if palavra in frequencia_palavras.keys():
                                if sentenca not in nota_sentencas.keys():
                                    nota_sentencas[sentenca] = frequencia_palavras[palavra]
                                else:
                                    nota_sentencas[sentenca] += frequencia_palavras[palavra]                
                    import heapq
                    melhores_sentencas = heapq.nlargest(3, nota_sentencas, key=nota_sentencas.get)
                    resumo = ' '.join(melhores_sentencas)
                    c2.text_area(label="Texto Resumido",value=resumo, height=800)
                except:
                    st.error("Favor verificar erro na conexão.")
                

with tab4:
    import os
    import openai

    def gpt3(stext):
        openai.api_key = "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"
        response = openai.Completion.create(
        engine="text-davinci-002", #"davinci-instruct-beta",
        prompt=stext,
            temperature=0.1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )
        content = response.choices[0].text.split(".")
        print(content)
        return response.choices[0].text

    c1, c2 = st.columns((2,2))
    with st.form(key="8lm"):
        c1.write("Olá, meu nome é Jarvis! O que você deseja?")
        query = c1.text_input("Pergunta?")
        bt_111 = st.form_submit_button("GERAR INFORMAÇÕES")
    if bt_111:
        try:
            response = gpt3(query)
            st.write(response)
        except:
            st.write("IA com preguiça. Tente mais tarde!")
        











