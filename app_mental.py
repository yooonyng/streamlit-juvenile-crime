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


def run_mental():
    df_mental = pd.read_csv('data/대검찰청_소년범죄자 성별 범행시 정신상태_20171231.csv',encoding='cp949')

    df_mental.index = df_mental['범죄분류']
    df_mental['총범죄건수'] = df_mental.sum(axis=1)
    df_mental = df_mental.drop('범죄분류',axis=1)
    df_mental.head()
    df_mental = df_mental[['정상_남', '정상_여', '정신이상_남', '정신박약_남', '정신이상_여', '정신박약_여', '기타정신장애_남',
       '기타정신장애_여', '주취_남', '주취_여', '월경시이상', '미상', '총범죄건수']]
    df_mental['정신이상_남'] = df_mental.iloc[:,2:4].sum(axis=1)
    df_mental['정신이상_여'] = df_mental.iloc[:,4:6].sum(axis=1)
    df_mental = df_mental[['정상_남', '정상_여', '정신이상_남', '기타정신장애_남', '정신이상_여', '기타정신장애_여', '주취_남',
       '주취_여']]
    df_mental['정신이상_남'] = df_mental.iloc[:,2:4].sum(axis=1)
    df_mental['정신이상_여'] = df_mental.iloc[:,4:6].sum(axis=1)
    df_mental = df_mental.drop(['기타정신장애_남','기타정신장애_여'],axis=1)

    df_mental = df_mental[['정상_남',	'정신이상_남',	'주취_남', '주취_여', '정상_여', '정신이상_여']]
    df_mental_sum = df_mental.sum().to_frame()


    st.subheader('소년범죄 정신건강 상태')

    fig1 = px.pie(df_mental_sum,names=['정상_남', '정상_여', '주취_남', '주취_여', '정신이상_남', '정신이상_여'],
            values=[45394, 8974, 4544, 729, 419, 40])
    st.plotly_chart(fig1)






