import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

def run_study():
    
    df_study = pd.read_csv('data/�����û_�ҳ������ ��������_20191231.csv',encoding='cp949')

    df_study.index = df_study['���˺з�']
    df_study['�ѹ��˰Ǽ�'] = df_study.sum(axis=1)
    df_study = df_study.drop('���˺з�',axis=1)
    df_study.head()
    df_study = df_study.drop(['������','�ʵ��б�_����', '�ʵ��б�_����', '�ʵ��б�_����','��������_����', '��������_����', '��������_����',
       '�Ϲݴ���_����', '�Ϲݴ���_����', '�Ϲݴ���_����', '���п�', '��Ÿ', '�̻�','�ѹ��˰Ǽ�'],axis=1)
    
    df_study_sum = df_study.sum().to_frame()
    plt.figure(figsize=(30,12))

    st.dataframe(df_study_sum)

    fig1 = px.pie(df_study_sum,names=['���б�_����', '���б�_����', '���б�_����', '�����б�_����	', '�����б�_����', '�����б�_����'],
            values=[13286, 1395, 1748, 23084, 9492, 4232],
            title='�ҳ� ���� ���� ���� ��Ȳ')
    st.plotly_chart(fig1)


    print(df_study_sum.shape)

    fig2 = plt.figure()
    plt.pie(np.array(df_study_sum.values).ravel(),autopct='%.2f',labels=df_study_sum.index,
       startangle=90,shadow=True,colors=['silver','lightgray','silver','firebrick','gray','darkgray','lightgray'],textprops={'size':12})

    plt.title('�ҳ���� ��������')
    plt.legend()
    st.pyplot(fig2)

