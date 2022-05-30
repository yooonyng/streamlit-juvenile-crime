import streamlit as st
import joblib
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt



def run_top5():
    df_crime = pd.read_csv('data/대검찰청_소년범죄자 범행동기_20171231.csv',encoding='cp949')

    df_crime.head()
    df_crime.isna().sum()
    df_crime.index = df_crime['범죄분류']
    df_crime = df_crime.drop('범죄분류',axis=1)
    df_crime.iloc[0,:].values.sum()
    df_crime['총범죄건수'] = df_crime.sum(axis=1)
    df_crime['유흥비사치'] = df_crime.iloc[:,1:7].sum(axis=1)
    df_crime = df_crime.drop(['유흥비마련', '도박비마련', '허영사치심','치부',	'이욕_기타',	'사행심'],axis=1)
    df_crime['호기심유혹우발적'] = df_crime.iloc[:,4:7].sum(axis=1)
    df_crime = df_crime.drop(['호기심',	'유혹',	'우발적'],axis=1)
    df_crime['가정불화'] = df_crime.iloc[:,3:5].sum(axis=1)
    df_crime = df_crime.drop(['현실불만'],axis=1)
    df_crime['신고보복'] = df_crime.iloc[:,1:3].sum(axis=1)
    df_crime = df_crime.drop(['신고_고소',	'보복_기타'],axis=1)
    df_crime['기타미상'] = df_crime.iloc[:,1:4].sum(axis=1)
    df_crime = df_crime.drop(['부주의',	'기타',	'미상'],axis=1)
    df_crime = df_crime[['생활비마련','유흥비사치','호기심유혹우발적','가정불화', '신고보복','기타미상','총범죄건수']]

    top5 = df_crime['총범죄건수'].sort_values(ascending=False).head()
    top5 = top5.to_frame()
    top5_chart = top5.reset_index()
    plt.figure(figsize=(10,8))
    
    fig = px.bar(top5_chart, x='범죄분류', y='총범죄건수')
    st.plotly_chart(fig)

    # df4_sorted = df4.sort_values('Sum',ascending=False)
    # fig2 = px.bar(df4_sorted,x='lang',y='Sum')
    # st.plotly_chart(fig2)

