import streamlit as st
import joblib
import numpy as np
import pandas as pd
import seaborn as sb
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

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



def run_result():
    df_result1 = pd.read_csv('data/대검찰청_소년범죄자 전회처분 상황_20171231.csv',encoding='cp949')

    df_result1.head()
    df_result1.index = df_result1['범죄분류']
    df_result1 = df_result1.drop('범죄분류',axis=1)

    df_re1_5 = df_result1[['초범','기소유예','선도유예','보호처분','형(재산형포함)집행종료']]
    df_re1_5_sum = df_re1_5.sum().to_frame()

    df_result2 = pd.read_csv('data/대검찰청_소년범죄자 처분결과_20171231.csv',encoding='cp949')
    
    df_result2.head()
    df_result2.index = df_result2['범죄분류']
    df_result2 = df_result2.drop('범죄분류',axis=1)

    df_re2_6 = df_result2[['구공판_구속',	'구공판_불구속',	'구약식',	'소년보호송치', '기소유예',	'혐의없음']]
    df_re2_6_sum = df_re2_6.sum().to_frame()

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


    st.title('➡️ 전회처분과 처분결과 상황')
    st.text('\n')
    st.info("1. 소년범의 종류\n2. 전회처분 상황\n3. 처분결과 상황\n4. 동종재범 기간\n5. 이종재범 기간")
    st.text('\n')
    st.text('\n')


    st.subheader('1. 소년범의 종류')
    image = Image.open('data/img02.jpg')
    st.image(image)
    st.text('\n')
    st.text('🟥 범죄소년 : 범행 당시 형사책임연령(만 14세 이상 ~ 만 19세 미만)이었던 소년\n형사처벌을 할 수 있으며, 가정법원의 심리에 따라 형사처벌이 아닌 보호처분을 할 수 있다.')
    st.text('🟥 촉법소년 : 범행 당시 형사책임연령이 아니었던 소년 중 만 10세 이상 ~ 만 14세 미만\n범행 당시 형사책임연령이 아니어서 형사처벌을 할 수 없으나, 소년법에 따라 보호처분을 할 수 있다.')
    st.text('🟥 범법소년 : 범행 당시 만 10세 미만의 소년\n범행 당시 형사책임연령이 아니어서 형사처벌을 할 수 없고, 소년법에 따른 보호처분도 할 수 없다.')
    st.caption('출처: 위키피디아')
    st.text('\n')
    st.text('\n')
    

    # values = [100, 200, 300,500]
    # labels = ['A', 'B', 'C', 'D']
    
    # # fig = px.pie(values=values, names=labels, width=400, height=400, hover_name=labels, title='plotly pie Chart', color=labels,color_discrete_map={'A':'green',
    #                              'B':'cyan',
    #                              'C':'yellow',
    #                              'D':'darkblue'})
    # fig.show()
        
    st.subheader('2. 전회처분 상황')

    fig1 = px.pie(df_re1_5_sum,names=['초범', '기소유예', '선도유예', '보호처분', '형(재산형포함)집행종료'],
        values=[35477, 7632, 1389, 12016, 2885], 
        color_discrete_map={'A':'green','B':'cyan','C':'yellow','D':'darkblue'})
    st.plotly_chart(fig1)

    st.subheader('3. 처분결과 상황')

    fig2 = px.pie(df_re2_6_sum,names=['구공판_구속', '구공판_불구속', '구약식', '소년보호송치', '기소유예','혐의없음'],
        values=[728, 2721, 2384, 20578, 20108, 4636])
    st.plotly_chart(fig2)

    st.subheader('4. 동종재범 기간')
    fig1 = px.bar(df_again_1_T, x=df_again_1_T.columns, y=df_again_1_T.index, orientation='h')
    st.plotly_chart(fig1)

    df_again_2_T = df_again_2.T
    df_again_2_T = df_again_2_T.drop(['장물','강도','횡령','방화','살인'],axis=1)

    st.subheader('5. 이종재범 기간')
    fig2 = px.bar(df_again_2_T, x=df_again_2_T.columns, y=df_again_2_T.index, orientation='h')
    st.plotly_chart(fig2)
    st.text('\n')
    st.text('\n')
    st.text('\n')
    st.text('\n')
   

    st.header('⚖️')
    st.subheader('잘못을 깨달을 수 있는 처벌은 적절하게 내려져야 하지만, 그 처벌마저 가르침의 역할이 있어야 의미가 있다.')
    st.subheader('왜냐하면 소년범은 ‘그 이후’를 또 한참 살아가기 때문에. 어느 섬이나 다른 나라에 치워지는 것이 아니라, 우리 사회에서 함께 말이다.')
    st.subheader('피해자를 최우선으로 보호하면서, 가해자에게 기회를 줌으로써 또 다른 가해의 연쇄를 끊는 것이 얼마나 중요한지')
    st.caption('출처: 경향신문 플랫 https://www.khan.co.kr/culture/culture-general/article/202203071450001')
    




