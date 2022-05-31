from inspect import stack
import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

############### 그래프에서 한국어 인식 ###############
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')    
else:
    print('Unknown system')



def run_again():
    
    df_again = pd.read_csv('data/대검찰청_소년범죄자 재범기간 및 종류_20171231.csv',encoding='cp949')

    df_again.head()
    df_again.index = df_again['범죄분류']
    df_again = df_again.drop('범죄분류',axis=1)

    df_again_10 = df_again.head(10)
    df_again_1 = df_again.iloc[:,:7]
    df_again_1 = df_again_1.head(10)
    df_again_2 = df_again.iloc[:,7:]
    df_again_2 = df_again_2.head(10)
    df_again_sum = df_again.sum().to_frame()
    df_again_1_T = df_again_1.T
    df_again_1_T = df_again_1_T.drop(['장물','횡령','손괴','방화','살인'],axis=1)


    st.subheader('소년범죄 동종재범 기간')

    fig1 = px.bar(df_again_1_T, x=df_again_1_T.columns, y=df_again_1_T.index, orientation='h')
    st.plotly_chart(fig1)


    df_again_2_T = df_again_2.T
    df_again_2_T = df_again_2_T.drop(['장물','강도','횡령','방화','살인'],axis=1)


    st.subheader('소년범죄 이종재범 기간')
    
    fig2 = px.bar(df_again_2_T, x=df_again_2_T.columns, y=df_again_2_T.index, orientation='h')
    st.plotly_chart(fig2)
   

