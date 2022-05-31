import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

def run_study():
    
   df_study = pd.read_csv('data/대검찰청_소년범죄자 교육정도_20191231.csv',encoding='cp949')

   df_study.index = df_study['범죄분류']    
   df_study['총범죄건수'] = df_study.sum(axis=1)
   df_study = df_study.drop('범죄분류',axis=1)
   df_study.head()
   df_study = df_study.drop(['불취학','초등학교_재중', '초등학교_중퇴', '초등학교_졸업','전문대학_재중', '전문대학_중퇴', '전문대학_졸업',
      '일반대학_재중', '일반대학_중퇴', '일반대학_졸업', '대학원', '기타', '미상','총범죄건수'],axis=1)
    
   df_study_sum = df_study.sum().to_frame()
   plt.figure(figsize=(30,12))

   st.dataframe(df_study_sum)

   fig1 = px.pie(df_study_sum,names=['중학교_재중', '중학교_중퇴', '중학교_졸업', '고등학교_재중', '고등학교_중퇴', '고등학교_졸업'],
         values=[13286, 1395, 1748, 23084, 9492, 4232],
         title='소년범죄 교육정도')
   st.plotly_chart(fig1)


   print(df_study_sum.shape)

   plt.rc('font', family='NanumBarunGothic')

   fig2 = plt.figure()
   plt.pie(np.array(df_study_sum.values).ravel(),autopct='%.2f',labels=df_study_sum.index,
      startangle=90,shadow=True,colors=['silver','lightgray','silver','firebrick','gray','darkgray','lightgray'],textprops={'size':12})

   plt.title('소년범죄 교육정도')
   plt.legend()
   st.pyplot(fig2)
