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



def run_result2():
    df_result2 = pd.read_csv('data/대검찰청_소년범죄자 처분결과_20171231.csv',encoding='cp949')
    
    df_result2.head()
    df_result2.index = df_result2['범죄분류']
    df_result2 = df_result2.drop('범죄분류',axis=1)

    df_re2_6 = df_result2[['구공판_구속',	'구공판_불구속',	'구약식',	'소년보호송치', '기소유예',	'혐의없음']]
    df_re2_6_sum = df_re2_6.sum().to_frame()
    

    fig1 = px.pie(df_re2_6_sum,names=['구공판_구속', '구공판_불구속', '구약식', '소년보호송치', '기소유예','혐의없음'],
        values=[728, 2721, 2384, 20578, 20108, 4636],
        title='소년범죄 처분결과 상황')
    st.plotly_chart(fig1)

    fig2 = plt.figure()
    plt.pie(np.array(df_re2_6_sum).ravel(),autopct='%.2f',labels=df_re2_6_sum.index,
    startangle=90,shadow=True,colors=['silver','lightgray','silver','brown','gray','darkgray','lightgray'],
    wedgeprops={'width':0.7}, textprops={'size':12})

    plt.title('소년범죄 처분결과 상황')
    plt.legend()
    st.pyplot(fig2)
