import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

def run_result1():
    df_result1 = pd.read_csv('data/대검찰청_소년범죄자 전회처분 상황_20171231.csv',encoding='cp949')

    df_result1.head()
    df_result1.index = df_result1['범죄분류']
    df_result1 = df_result1.drop('범죄분류',axis=1)

    df_re1_5 = df_result1[['초범','기소유예','선도유예','보호처분','형(재산형포함)집행종료']]
    df_re1_5_sum = df_re1_5.sum().to_frame()
    
    st.dataframe(df_re1_5_sum)

    fig1 = px.pie(df_mental_sum,names=['정상_남', '정상_여', '주취_남', '주취_여', '정신이상_남', '정신이상_여'],
        values=[45394, 8974, 4544, 729, 419, 40],
        title='소년범죄 정신상태')
    st.plotly_chart(fig1)


'초범', '기소유예', '선도유예', '보호처분', '형(재산형포함)집행종료'


