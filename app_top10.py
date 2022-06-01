import streamlit as st
import joblib
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image
import os
import base64


def run_top10():
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


    @st.cache(allow_output_mutation=True)
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    @st.cache(allow_output_mutation=True)
    def get_img_with_href(local_img_path, target_url):
        img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
        bin_str = get_base64_of_bin_file(local_img_path)
        html_code = f'''
            <a href="{target_url}">
                <img src="data:image/{img_format};base64,{bin_str}" />
            </a>'''
        return html_code

    st.title('➡️ 사회적 시선과 의견 대립')
    st.text('\n')
    st.info("1. 소년 범죄 순위 Top10\n2. 최근 소년범죄 이슈\n3. 최근 소년범죄 관련 기사\n4. 소년범죄에 대한 의견 대립")
    st.text('\n')
    st.text('\n')

    st.subheader('1. 소년 범죄 순위 Top10')
    top10 = df_crime['총범죄건수'].sort_values(ascending=False).head(10)
    top10 = top10.to_frame()
    top10_chart = top10.reset_index()

    fig2 = px.bar(top10_chart, x='범죄분류', y='총범죄건수')
    st.plotly_chart(fig2)
    st.text('\n')
    st.text('\n')
    st.text('\n')

    st.subheader('2. 최근 소년범죄 이슈')
    col1,col2,col3 = st.columns(3)
    with col1:
        gif_html = get_img_with_href('data/sum01.png', 'https://www.youtube.com/watch?v=h-WmvzCtRh0')
        st.markdown(gif_html, unsafe_allow_html=True)
    with col2:
        pass
    with col3:
        st.subheader('끊임없는 촉법소년 논란 연령하향 해야 vs 처벌이 능사는 아냐')
        st.text('#촉법소년 #소년법 #촉법소년범죄')
    st.text('\n')
    st.text('\n')

    col1,col2,col3 = st.columns(3)
    with col1:
        gif_html = get_img_with_href('data/sum02.png', 'https://www.youtube.com/watch?v=Xq9vYA2sQCk')
        st.markdown(gif_html, unsafe_allow_html=True)
    with col2:
        pass
    with col3:
        st.subheader('빈번히 일어나는 청소년 범죄와 그들의 심리, 촉법 소년법 어떻게 해야 할까?')
        st.text('#청소년범죄 #촉법소년')
    st.text('\n')
    st.text('\n')

    col1,col2,col3 = st.columns(3)
    with col1:
        gif_html = get_img_with_href('data/sum03.png', 'https://www.youtube.com/watch?v=DfOQjgx-owk')
        st.markdown(gif_html, unsafe_allow_html=True)
    with col2:
        pass
    with col3:
        st.subheader('소년법, 이대로 괜찮은거 맞아요?')
        st.text('#촉법소년 #소년법 #소년심판')
    st.text('\n')
    st.text('\n')
    st.text('\n')
    st.text('\n')

    st.subheader('3. 최근 소년범죄 관련 기사')
    st.markdown('<big>[갈수록 흉포해지는 소년범죄, 처벌 연령 낮추는 게 옳다](https://www.mk.co.kr/opinion/editorial/view/2022/03/288888/)',unsafe_allow_html=True)
    st.markdown('<big>[늘어나는 10대 강력범죄‥ 69년 된 촉법소년 논란](https://imnews.imbc.com/replay/2022/nwdesk/article/6337168_35744.html)',unsafe_allow_html=True)
    st.markdown('<big>[촉법소년 범죄자 1만명...연령 하한에 엄벌 VS 신중](https://www.ajunews.com/view/20220520093302711)',unsafe_allow_html=True)
    st.text('\n')
    st.text('\n')
    st.text('\n')
    st.text('\n')

    st.subheader('4. 소년범죄에 대한 의견 대립')
    image = Image.open('data/img03.jpg')
    st.image(image)
    st.text('\n')
