import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

def run_parents():
    df_crime = pd.read_csv('data/대검찰청_소년범죄자 범행동기_20171231.csv',encoding='cp949')
    df_parents = pd.read_csv('data/대검찰청_소년범죄자 부모관계_20171231.csv',encoding='cp949')

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

    df_parents.head()
    df_parents.index = df_parents['범죄분류']
    df_parents = df_parents.drop('범죄분류',axis=1)
    df_parents['미혼자부모관계'] = df_parents.iloc[:,1:8].sum(axis=1)
    df_parents = df_parents.drop(['계부모',	'실부계모',	'실부무모',	'실모계부',	'실모무부',	'계부무모',	'계모무부'],axis=1)
    df_parents = df_parents[['실(양)부모', '무부모','기혼', '미상', '미혼자부모관계','미혼자부모관계_미상']]
    df_parents['미혼자부모관계'] = df_parents.iloc[:,4:6].sum(axis=1)
    df_parents = df_parents.drop(['미혼자부모관계_미상'],axis=1)
    df_parents = df_parents[['실(양)부모', '미혼자부모관계','무부모','기혼', '미상']]

    df_connect = pd.merge(df_crime,df_parents,on='범죄분류')
    df_connect = df_connect.sort_values('총범죄건수',ascending=False)

    st.subheader('소년범과 부모관계')

    language = ['실(양)부모','미혼자부모관계','무부모','기혼','미상']
    my_choice = st.selectbox(language)
    
    if my_choice == language[0]:
        alt_chart = alt.Chart(df_connect).mark_circle().encode(
        x = '실(양)부모',
        y = '총범죄건수',
        size = '실(양)부모')
        st.altair_chart(alt_chart)

    elif my_choice == language[1]:
        alt_chart = alt.Chart(df_connect).mark_circle().encode(
        x = '미혼자부모관계',
        y = '총범죄건수',
        size = '미혼자부모관계')
        st.altair_chart(alt_chart)

    elif my_choice == language[2]:
        alt_chart = alt.Chart(df_connect).mark_circle().encode(
        x = '무부모',
        y = '총범죄건수',
        size = '무부모')
        st.altair_chart(alt_chart)

    elif my_choice == language[3]:
        alt_chart = alt.Chart(df_connect).mark_circle().encode(
        x = '기혼',
        y = '총범죄건수',
        size = '기혼')
        st.altair_chart(alt_chart)
    
    elif my_choice == language[4]:
        alt_chart = alt.Chart(df_connect).mark_circle().encode(
        x = '미상',
        y = '총범죄건수',
        size = '미상')
        st.altair_chart(alt_chart)
        