import streamlit.components.v1 as components
import streamlit as st
import time
import numpy as np
from datetime import datetime
import pandas as pd
import seaborn as sns
from openpyxl import Workbook
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder, JsCode
from tqdm import tqdm
import matplotlib.pyplot as plt
import sqlalchemy   
from datetime import date
from scipy import stats
import mysql.connector
import plotly.express as px
from plotly import graph_objects as go
import psycopg2
import warnings
import pickle
from deta import Deta
import json
st.set_page_config(page_icon="https://7lm.com.br/wp-content/themes/7lm/build/img/icons/assinatura_7lm.png", layout="wide", page_title="GRUPO IMERGE | FERRAMENTA")


# Acesso do Banco de Dados
#====================================================================
KEY = "2e4p4f"
TOKEN = "e0vhjypu_T5B1mUZN1r13YLVWqeuLK8tz6tyLPNaE"
deta = Deta(TOKEN)
BD = deta.Base(KEY)
#====================================================================




st.title("Cadastro de Insumos")




# Funções de acesso
#====================================================================
def grid_dataframe_top(df, tamanho):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(groupable=True, enableValue=True, enableRowGroup=True,aggFunc="sum",editable=True)
    gb.update_mode=GridUpdateMode.MANUAL
    gb.configure_selection(selection_mode="multiple", use_checkbox=True)
    gb.configure_side_bar()
    gridoptions = gb.build()
    response = AgGrid(
        df,
        height=tamanho,
        gridOptions=gridoptions,
        enable_enterprise_modules=True,
        header_checkbox_selection_filtered_only=True,
        use_checkbox=True, theme="blue")
    return response

def baixa_bd(Banco_Dados, COL):
    res = Banco_Dados.fetch()
    all_items = res.items
    while res.last:
        res = Banco_Dados.fetch(last=res.last)
        all_items += res.items
    banco_de_dados = pd.DataFrame([all_items][0])
    banco_de_dados = banco_de_dados.loc[:, COL]
    return banco_de_dados


def SALVAR_BANCO_DE_DADOS(dic_emp, bd):
    user = bd.put(dic_emp)
    return user

def salvar_bd(dic_emp, bd):
    n=0
    pbar = tqdm(total = len(dic_emp), position=0, leave = True)
    for i in range(0,len(dic_emp)):
        pbar.update()
        bd.put(dic_emp[n])
        n+=1
    return print("Script Finalizado")
#====================================================================


df = pd.read_excel("Cadastro_Geral.xlsx")
df = df.iloc[4:,:]

col_df = []
for i in df.iloc[0,:]:
    col_df.append(i)


df_001 = pd.DataFrame(data=df, columns=col_df, index=range(0, 500))

for i in range(0, 8):
    df_001[col_df[i]] = df.iloc[:,i]


df_final = df_001.iloc[5:,0:8]
espaco = st.container()
#grid_dataframe_top(df_final, 400)


#grid_dataframe_top(df,800)

with st.sidebar.expander("ANEXAR DOC"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        dataframe = pd.read_excel(uploaded_file)
        



dic_emp = {25:"AGL25", "25":"AGL25","23":"AGL23", "27":"AGL27"}
      
def envio():
    try:
        df_solicitacao = pd.DataFrame(index=range(0,len(dataframe)-1))
        df_solicitacao["NOME"] = dataframe.iloc[2,1]
        df_solicitacao["Email"] = dataframe.iloc[3,1]

        try:
            df_solicitacao["Obra"] = dic_emp[dataframe.iloc[2,9]]
        except:
            df_solicitacao["Obra"] = dataframe.iloc[2,9]
            
        df_solicitacao["DATA"] = pd.to_datetime(dataframe.iloc[3,9], errors="coerce").strftime("%d-%m-%y")
        df_solicitacao["Descrição"] = 0
        df_solicitacao["Unidade"] = 0
        df_solicitacao["Cod.item"] = 0
        
        n=6
        limite = len(dataframe.iloc[6:,1])
 

        for i in range(0,limite):
            df_solicitacao.iloc[i,4] = dataframe.iloc[n,1]
            df_solicitacao.iloc[i,5] = dataframe.iloc[n,9]
            df_solicitacao.iloc[i,6] = dataframe.iloc[n,11]
            n+=1

        Arquivo_final = df_solicitacao.iloc[0:limite, :]
        Arquivo_final["Item"] = range(0, limite)
        Arquivo_final["Finalidade"] = "Solicitação"
        
        st.title("Planilha de Envio::")
        grid_dataframe_top(Arquivo_final,300)
    except:
        st.error("IMPORTAR BASE")
    return Arquivo_final
try:
    envio()
except:
    pass

with st.sidebar.expander("ENVIAR AO BD"):
    BT_001 = st.button("ENVIAR AO BD")    

if BT_001:
    df = df_final.astype(str)
    BASE1 = json.loads(json.dumps(list(df.T.to_dict().values())))
    salvar_bd(BASE1, BD)
    st.success("DADOS ENVIADOS")
    
    
with st.sidebar.expander("ENVIAR SOLICITAÇÃO"):
    BT_002 = st.button("ENVIAR AO BANCO DE DADOS")    
    
    

if BT_002:  
    df = envio() 
    df = df.astype(str)
    BASE1 = json.loads(json.dumps(list(df.T.to_dict().values())))
    salvar_bd(BASE1, BD)
    st.success("DADOS ENVIADOS")
try:   
    df = envio()    
    coluna = list(df.columns)   
    data_ = baixa_bd(BD, coluna)
    with espaco:
        grid_dataframe_top(data_, 500)
except:
    pass