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

st.title("# EPR | DCD | CEF CRÉDITO ")


# BANCO DE DADOS ACESSO ================================================================================

ID_BD = "fe96xe"
Key_name = "fe96xe"
Key = "fe96xe"
token = "a02oy5av_rKazvmd4H16MgHLaz1Y3uKa34sXg4uZ7"

deta = Deta(token)
db = deta.Base(Key)

ID_BD1 = "tbwokc"
Key_name = "tbwokc"
Key1 = "tbwokc"
token1 = "e0voh46t_NP78oPva2ngqY7ro5yJ8h4SN1uVmwRyx"

deta1 = Deta(token1)
db1 = deta1.Base(Key1)

dic_col = ['JUROS_AGL25_MOD1','JUROS_AGL25_MOD2','JUROS_AGL23','JUROS_F003', 'JUROS_F005', 'JUROS_AGL27', 'JUROS_DF001', 'JUROS_FSA006', 'JUROS_FSA007', 'JUROS_AGL28_MOD1', 'JUROS_AGL28_MOD2', 'key']


def salvar_bd(dic_emp, bd):
    n=0
    for i in range(0,len(dic_emp)):
        bd.put(dic_emp[n])
        n+=1
    return print("Script Finalizado")


colunas = ["key",'CONTRATO',
 'NOME MUTUARIO',
 'COD',
 'DT.ASSIN',
 'TIPO UND',
 'GAR.AUT',
 'DT.INC.CTR',
 'DT.INC.REG',
 'VR RETIDO',
 'VR AMORTIZ',
 'AMO',
 'MES_REG',
 'ANO_REG',
 'MES_ASSINATURA',
 'ANO_ASSINATURA',
 'EMPREENDIMENTO']

AGL23 = 'AGL 23 - Vila do Sol'
AGL25_1 = 'AGL 25 - Vila das Águas'
AGL25_2 = 'AGL 25 - Vila das Águas'
AGL27 = 'AGL 27 - Vila Azaleia - 7LM'
AGL28 = 'AGL28 - Vila do Cerrado'
F5 = "FSA 05 - Vila das Orquídeas - 7LM"
F6 = "FSA 06 - Vila das Tulipas - 7LM"
F3 = "FSA 03 - Aurium Home"
HAUS = "DF 01 - Haus By Novka"


def ABRIR_TABELA():  
    #Abrir pickle 
    tabela_ = open("df_tabela.pickle","rb")
    #Baixar pickle 
    tabela = pickle.load(tabela_)
    return tabela


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

def conversor_moeda_brasil(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def baixa_bd(Banco_Dados, COL):
    res = Banco_Dados.fetch()
    all_items = res.items
    while res.last:
        res = Banco_Dados.fetch(last=res.last)
        all_items += res.items
    banco_de_dados = pd.DataFrame([all_items][0])
    banco_de_dados = banco_de_dados.loc[:, COL]
    return banco_de_dados

def delete_user(key):
    db.delete(key)
    return st.success("Dados Deletado")

def get_user(key):
    user = db.get(key)
    return user

def ATUALIZAR_BANCO_DADOS_PANDAS(Coluna, value, key):
    df1 = get_user(key)
    df1[Coluna] = value
    user = db.put(df1, key)
    return user

def INDICADOR(meta,text):
    fig = go.Figure()
    fig.add_trace(go.Indicator(
    mode = "number",
    title = {"text": text},
    value = meta,
    domain = {'row': 0, 'column': 1}))
    fig.update_layout(height=150, width=250,margin=dict(l=0, r=0, t=0 , b=0 ))
    fig.update_layout(showlegend=False, paper_bgcolor = 'rgba(0, 0, 0, 0)', plot_bgcolor = 'rgba(0, 0, 0, 0)')
    return fig

espaco = st.container()

def ABRIR_REPASSE():  
    #Abrir pickle
    repasse_ = open("df_repasse.pickle","rb") 
    #Baixar pickle
    repasse = pickle.load(repasse_)
    return repasse    
 
def ABRIR_VENDAS():  
    #Abrir pickle 
    vendas_ = open("df_vendas.pickle","rb")
    #Baixar pickle 
    vendas = pickle.load(vendas_)
    return vendas


with st.sidebar.expander("ATUALIZAR BANCO DE DADOS"):
    with st.form(key="form001"):
        # incluir elementos
        bt_001 = st.form_submit_button("BAIXAR_ARQUIVO")
    if bt_001:
        with espaco:
            df = baixa_bd(db,colunas)
            df = df.loc[df["NOME MUTUARIO"]!='7 LM EMPREENDIMENTOS IMO ']               

            df.sort_values(by=["EMPREENDIMENTO"], inplace=True)
            df["MES_REG"] = df["DT.INC.REG"].str.slice(3,5) 
            df["ANO_REG"] = df["DT.INC.REG"].str.slice(6,8) 

            df["MES_ASSINATURA"] = df["DT.INC.CTR"].str.slice(3,5) 
            df["ANO_ASSINATURA"] = df["DT.INC.CTR"].str.slice(6,8) 

            df["MES_REG"] = df["MES_REG"].astype(int)
            df["ANO_REG"] = df["ANO_REG"].astype(int)

            df["MES_ASSINATURA"] = df["MES_ASSINATURA"].astype(int)
            df["ANO_ASSINATURA"] = df["ANO_ASSINATURA"].astype(int)
            
            df["Assinado_Caixa"] = 1
            df.loc[df["MES_REG"]==0,"Registrado"] = 0
            df.loc[df["MES_REG"]!=0,"Registrado"] = 1      
            
            dindin = []
            dindin1 = []
            for i in df["VR RETIDO"]:
                try:
                    dindin.append(conversor_moeda_brasil(i))
                except:
                    dindin.append(i)
            for i in dindin:
                a = i.replace(".", "")
                b = a.replace(",", ".")
                dindin1.append(b)
            
            df["VR RETIDO"] = dindin1
            df["VR RETIDO"] = df["VR RETIDO"].astype(float)

            dindin = []
            dindin1 = []
            for i in df["VR AMORTIZ"]:
                try:
                    dindin.append(conversor_moeda_brasil(i))
                except:
                    dindin.append(i)
            for i in dindin:
                a = i.replace(".", "")
                b = a.replace(",", ".")
                dindin1.append(b)
            df["VR AMORTIZ"] = dindin1
            df["VR AMORTIZ"] = df["VR AMORTIZ"].astype(float)      
                        
            df = df.loc[df["NOME MUTUARIO"]!='7 LM EMPREENDIMENTOS IMO ']               
            resumo = pd.DataFrame(df.groupby(["EMPREENDIMENTO"])["Assinado_Caixa","Registrado","VR RETIDO"].sum()).reset_index()
            total_unidade = [138, 144,58,112,58, 144,184, 144 ]
            resumo["Total_Unid"] = total_unidade
            resumo["Quitado"] = 0

            #st.write(resumo)
            
            vendas = ABRIR_VENDAS()
            repasse = ABRIR_REPASSE()
            filtro_repasse = repasse[["reserva","situacao","empreendimento","etapa","valor_previsto"]]

            list_restricao = ["7.2 Distrato","9.1 Distrato","9.2 Cancelado"] 
            list_quitado = ["7.4 - Venda a vista", '8.1 - Venda a vista','7.5 - Venda a vista' ]

            filtro_repasse_001 = filtro_repasse.loc[~filtro_repasse["situacao"].isin(list_restricao)]
            filtro_repasse_002 = filtro_repasse_001.sort_values(by=["situacao","empreendimento","etapa"], ascending=True)
            #st.write(filtro_repasse_002)
            filtro_repasse_002["valor_previsto"] = filtro_repasse_002["valor_previsto"].astype(float)
            repasse_valor_medio = filtro_repasse_002.loc[filtro_repasse_002["valor_previsto"]>0]


            FIL = filtro_repasse_002.loc[filtro_repasse_002["situacao"].isin(list_quitado)]
            VENDAS_TRAT = vendas.loc[vendas["empreendimento"].isin([AGL23, AGL25_1, AGL27, AGL28, F5, F6, F3, HAUS])]
            VENDAS_TRAT = VENDAS_TRAT.loc[VENDAS_TRAT["situacao_atual"].isin(["Venda finalizada"])]
            
            AGL23_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([AGL23])])
            AGL25_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([AGL25_1])])
            AGL27_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([AGL27])])
            AGL28_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([AGL28])])
            F5_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([F5])])
            F6_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([F6])])
            F3_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([F3])])
            HAUS_QUITADO = len(FIL.loc[FIL["empreendimento"].isin([HAUS])])
            
            AGL23_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([AGL23])])
            AGL25_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([AGL25_1])])
            AGL27_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([AGL27])])
            AGL28_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([AGL28])])
            F5_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([F5])])
            F6_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([F6])])
            F3_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([F3])])
            HAUS_VENDIDO = len(VENDAS_TRAT.loc[VENDAS_TRAT["empreendimento"].isin([HAUS])])

            PM_EMP = pd.DataFrame(repasse_valor_medio.groupby(["empreendimento"])["valor_previsto"].median()).reset_index()
            PM_AGL23 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([AGL23])]["valor_previsto"])[0]
            PM_AGL25 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([AGL25_1])]["valor_previsto"])[0]
            PM_AGL27 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([AGL27])]["valor_previsto"])[0]
            PM_AGL28 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([AGL28])]["valor_previsto"])[0]
            PM_F5 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([F5])]["valor_previsto"])[0]
            PM_F6 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([F6])]["valor_previsto"])[0]
            PM_F3 = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([F3])]["valor_previsto"])
            PM_HAUS = list(PM_EMP.loc[PM_EMP["empreendimento"].isin([HAUS])]["valor_previsto"])[0]
            
            tab = ABRIR_TABELA()
            
            status_unidades = tab.copy()
            status_unidades = status_unidades[["empreendimento","etapa","bloco","unidade","metragem","situacao"]]
            EMP = ['AGL 25 - Vila das Águas','FSA 03 -  Aurium Home', "FSA07 - Vila Das Hortênsias 7LM", 'FSA 06 - Vila das Tulipas - 7LM','AGL 25 - Vila das Águas',
                'AGL 23 - Vila do Sol', 'FSA 05 - Vila das Orquídeas - 7LM','AGL 27 - Vila Azaleia - 7LM',  'AGL28 - Vila do Cerrado','DF 01 - Haus By Novka' ]
            status_unidades_001 = status_unidades.loc[status_unidades["empreendimento"].isin(EMP)]
            status_unidades_001 = status_unidades_001.loc[status_unidades_001["situacao"] == "Vendida"]
            status_unidades_001["Vendidas"] = 1
            status_unidades_002 = pd.DataFrame(status_unidades_001.groupby(["empreendimento","etapa"])["Vendidas"].sum()).reset_index().sort_values(by=["empreendimento","etapa"], ascending=True)

            NOV_F3 = status_unidades_002.loc[status_unidades_002["empreendimento"] == 'FSA 03 -  Aurium Home']["Vendidas"].values[0]
            SETE_AGL27 = status_unidades_002.loc[status_unidades_002["empreendimento"] == 'AGL 27 - Vila Azaleia - 7LM']["Vendidas"].values[0]
            SETE_F5 = status_unidades_002.loc[status_unidades_002["empreendimento"] == 'FSA 05 - Vila das Orquídeas - 7LM']["Vendidas"].values[0]
            SETE_F6 = status_unidades_002.loc[status_unidades_002["empreendimento"] == 'FSA 05 - Vila das Orquídeas - 7LM']["Vendidas"].values[0]
            SETE_AGL28 = status_unidades_002.loc[status_unidades_002["empreendimento"] == 'AGL28 - Vila do Cerrado']["Vendidas"].values[0]
            SETE_AGL23 = status_unidades_002.loc[status_unidades_002["empreendimento"] == 'AGL 23 - Vila do Sol']["Vendidas"].values[0]
            NOV_DF001 = status_unidades_002.loc[status_unidades_002["empreendimento"] == "DF 01 - Haus By Novka"]["Vendidas"].values[0]
            ETQ = [138,144,NOV_F3,SETE_AGL27, NOV_DF001, SETE_F5, SETE_AGL23, SETE_F6 ]
            
            
            #st.write(resumo)
            resumo["POC"] = [1.0,0.975, 0, 0.40, 0.20, 0.60, 0.61, 0.29 ]
            list_final_financ_medio = [PM_AGL25, PM_AGL25, 0, PM_AGL27, PM_HAUS, PM_F5, PM_AGL23, PM_F6]          
            list_final_vendidos =  [138, AGL25_VENDIDO-138, F3_VENDIDO, AGL27_VENDIDO, HAUS_VENDIDO, F5_VENDIDO,  AGL23_VENDIDO,F6_VENDIDO]
            list_final_quitados =  [AGL25_QUITADO, AGL25_QUITADO, F3_QUITADO, AGL27_QUITADO, HAUS_QUITADO, F5_QUITADO,  AGL23_QUITADO,F6_QUITADO]
            resumo["Quitado"] = list_final_quitados
            resumo["Vendidos"] = ETQ
            resumo["MP_Assinatura"] = (resumo["Assinado_Caixa"] + resumo["Quitado"]) - resumo["Vendidos"]
            resumo["MP_Registro"] = resumo["Registrado"] - resumo["Assinado_Caixa"]
            resumo["Financ_Médio"] = list_final_financ_medio
            resumo["Previsão_Receb_PF"] = resumo["VR RETIDO"]
            #resumo["Previsão_Receb_PF"] = df["VR RETIDO"].sum()#np.round(resumo["Financ_Médio"] * (-resumo["MP_Registro"])  * resumo["POC"]) 
            resumo_001 = resumo.loc[:,["EMPREENDIMENTO","Total_Unid","Vendidos","Assinado_Caixa","Quitado","Registrado","MP_Assinatura","MP_Registro","Financ_Médio","POC","Previsão_Receb_PF"]]
            #st.write(resumo.columns)
            #st.plotly_chart(INDICADOR(resumo_001["MP_Assinatura"].sum(), "MP | ASSINATURA CEF"))
            #st.plotly_chart(INDICADOR(resumo_001["MP_Registro"].sum(), "MP | REGISTRO"))
            #st.plotly_chart(INDICADOR(resumo_001["Previsão_Receb_PF"].sum(), "PF | REC"))
            
            #JUROS = baixa_bd(db1, dic_col)
            #st.write(JUROS)
            
            
            with espaco:
                JUROS = baixa_bd(db1,dic_col)
                JUROS_AGL25_MOD1 = str(JUROS.iloc[0,0]).replace(".", "")
                JUROS_AGL25_MOD1 = JUROS_AGL25_MOD1.replace(",", ".")

                JUROS_AGL25_MOD2 = str(JUROS.iloc[0,1]).replace(".", "")
                JUROS_AGL25_MOD2 = JUROS_AGL25_MOD2.replace(",", ".")

                JUROS_AGL23 = str(JUROS.iloc[0,2]).replace(".", "")
                JUROS_AGL23 = JUROS_AGL23.replace(",", ".")

                JUROS_F003 = str(JUROS.iloc[0,3]).replace(".", "")
                JUROS_F003 = JUROS_F003.replace(",", ".")

                JUROS_F005 = str(JUROS.iloc[0,4]).replace(".", "")
                JUROS_F005 = JUROS_F005.replace(",", ".")

                JUROS_AGL27 = str(JUROS.iloc[0,5]).replace(".", "")
                JUROS_AGL27 = JUROS_AGL27.replace(",", ".")

                JUROS_DF001 = str(JUROS.iloc[0,6]).replace(".", "")
                JUROS_DF001 = JUROS_DF001.replace(",", ".")

                JUROS_FSA006 = str(JUROS.iloc[0,7]).replace(".", "")
                JUROS_FSA006 = JUROS_FSA006.replace(",", ".")
                c1, c2, c3 = st.columns((3,3,3))
                
                PJ_ = [float(JUROS_AGL25_MOD1), float(JUROS_AGL25_MOD2), float(JUROS_F003), float(JUROS_AGL27), float(JUROS_DF001), float(JUROS_F005),float(JUROS_AGL23), float(JUROS_FSA006)]
                
                with c1:
                    st.plotly_chart(INDICADOR(float(JUROS_AGL23), "PJ | AGL23"))  
                with c2: 
                    st.plotly_chart(INDICADOR(float(JUROS_F003), "PJ | F003"))   
                with c3: 
                    st.plotly_chart(INDICADOR(float(JUROS_F005), "PJ | F005"))  
                    
                c1, c2, c3 = st.columns((3,3,3))                       
                with c1: 
                    st.plotly_chart(INDICADOR(float(JUROS_AGL27), "PJ | AGL27"))
                with c2: 
                    st.plotly_chart(INDICADOR(float(JUROS_DF001), "PJ | DF001"))            
                with c3: 
                    st.plotly_chart(INDICADOR(float(JUROS_FSA006), "PJ | F006"))       
        
                c1, c2, c3 = st.columns((3,3,3))
                st.subheader("INDICADORES OPERACIONAIS")
                with c1:
                    st.plotly_chart(INDICADOR(resumo_001["MP_Assinatura"].sum(), "MP | ASSINATURA CEF"))                    
                with c2:
                    st.plotly_chart(INDICADOR(resumo_001["MP_Registro"].sum(), "MP | REGISTRO"))
                with c3:
                    st.plotly_chart(INDICADOR(resumo_001["Previsão_Receb_PF"].sum(), "PF | REC"))
            resumo_001["PJ_utilizado"] = PJ_
            resumo_001["Juros_estimado"] = resumo_001["PJ_utilizado"]*0.009 
            a = []
            b = []
            c = []
            d = []
            for e, f, g, h in zip(resumo["Financ_Médio"], resumo["Previsão_Receb_PF"], PJ_,resumo_001["Juros_estimado"]):
                a.append(conversor_moeda_brasil(e))
                b.append(conversor_moeda_brasil(f))
                c.append(conversor_moeda_brasil(g))
                d.append(conversor_moeda_brasil(h))
            resumo_001["Financ_Médio"] = a
            resumo_001["Previsão_Receb_PF"] = b   
            resumo_001["PJ_utilizado"] = c  
            resumo_001["Juros_estimado"] = d
            grid_dataframe_top(resumo_001, 300)
            st.subheader("Base | EPR")
            grid_dataframe_top(df, 800)