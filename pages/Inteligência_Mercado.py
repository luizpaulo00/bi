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

st.title("# INTELIGÊNCIA NEGOCIO | VENDAS | MKT | CRÉDITO")





with st.sidebar.expander("ATUALIZAR BANCO DE DADOS"):
    with st.form(key="form001"):
        # incluir elementos
        bt_001 = st.form_submit_button("BAIXAR_ARQUIVO")
    if bt_001:
        st.sucess("ok")
    

Relatorio_Aguas_Lindas, Relatorio_Aguas_Formosa = st.tabs(["Relatorio_Aguas_Lindas", "Relatorio_Aguas_Formosa"])

n=0
m=4
k = f"Pág_{n+1}"
i = f"t{n+1}"
j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"

with st.expander("RELATÓRIOS_DE_INTELIGÊNCIA"):
    SENHA = st.text_input("SENHA_ACESSO",type="password",placeholder="Preencha a senha", value=0 )
    if SENHA == 0:
        st.warning("Favor preencher a senha!")
    if SENHA != "7lm2022":
        st.error("Senha errada!")
    else: 
        with Relatorio_Aguas_Lindas:
            st.header(k)
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)
            #====================================================================
            n+=1
            m+=1
            k = f"Pág_{n+1}"
            i = f"t{n+1}"
            j = f"assets/relatorio/64c293ff5e4bff2998a45ab1c7baa0cd-{m+1}.png"
            st.image(j, width=1500)
            st.write(j)



            





