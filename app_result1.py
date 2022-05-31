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



def run_result1():
    df_result1 = pd.read_csv('data/대검찰청_소년범죄자 전회처분 상황_20171231.csv',encoding='cp949')

    df_result1.head()
    df_result1.index = df_result1['범죄분류']
    df_result1 = df_result1.drop('범죄분류',axis=1)

    df_re1_5 = df_result1[['초범','기소유예','선도유예','보호처분','형(재산형포함)집행종료']]
    df_re1_5_sum = df_re1_5.sum().to_frame()
    

    fig1 = px.pie(df_re1_5_sum,names=['초범', '기소유예', '선도유예', '보호처분', '형(재산형포함)집행종료'],
        values=[35477, 7632, 1389, 12016, 2885],
        title='소년범죄 전회처분 상황')
    st.plotly_chart(fig1)




