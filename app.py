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



def main():

    st.title('🚔소년범죄와 주변환경의 관계')
    st.text('\n')

    image = Image.open('data/img01.jpg')
    st.image(image)
    st.text('\n')



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

    

    st.info("1. 사회적 시선과 의견 대립\n2. 소년범의 주변 환경\n3. 전회처분과 처분결과 상황")
    st.text('\n')
    st.text('\n')
    st.write('---')
    st.title('➡️ 사회적 시선과 의견 대립')
    st.text('\n')
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
   
    st.subheader('3. 소년범죄에 대한 의견 대립')
    image = Image.open('data/img03.jpg')
    st.image(image)
    st.text('\n')



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

    df_study = pd.read_csv('data/대검찰청_소년범죄자 교육정도_20191231.csv',encoding='cp949')

    df_study.index = df_study['범죄분류']    
    df_study['총범죄건수'] = df_study.sum(axis=1)
    df_study = df_study.drop('범죄분류',axis=1)
    df_study.head()
    df_study = df_study.drop(['불취학','초등학교_재중', '초등학교_중퇴', '초등학교_졸업','전문대학_재중', '전문대학_중퇴', '전문대학_졸업',
      '일반대학_재중', '일반대학_중퇴', '일반대학_졸업', '대학원', '기타', '미상','총범죄건수'],axis=1)
    
    df_study_sum = df_study.sum().to_frame()
    plt.figure(figsize=(30,12))

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
    
    
    st.write('---')
    st.title('➡️ 소년범의 주변 환경')
    st.text('\n')
    st.text('\n')
    st.text('\n')

    col1,col2,col3 = st.columns(3)
    with col1:
        gif_html = get_img_with_href('data/img05.png', 'https://www.netflix.com/kr/title/81312802')
        st.markdown(gif_html, unsafe_allow_html=True)
    with col2:
        pass
    with col3:
        st.subheader('범죄를 택한 건 소년이지만')
        st.subheader('그 소년은 결코 홀로 자라지 않는다')
        st.caption('출처: 경향신문 플랫 https://www.khan.co.kr/culture/culture-general/article/202203071450001')
    st.text('\n')
    st.text('\n')
    st.text('\n')
    st.text('\n')

    st.subheader('1. 소년범의 부모 관계')
    language = ['실(양)부모','미혼자부모관계','무부모','기혼','미상']
    my_choice = st.selectbox('부모 관계 선택',language)
    
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
        
    st.subheader('2. 소년범의 교육 정도')
    fig1 = px.pie(df_study_sum,names=['중학교_재중', '중학교_중퇴', '중학교_졸업', '고등학교_재중', '고등학교_중퇴', '고등학교_졸업'],
            values=[13286, 1395, 1748, 23084, 9492, 4232],
            color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig1)

    print(df_study_sum.shape)

    st.subheader('3. 소년범의 정신 건강 상태')
    fig1 = px.pie(df_mental_sum,names=['정상_남', '정상_여', '주취_남', '주취_여', '정신이상_남', '정신이상_여'],
            values=[45394, 8974, 4544, 729, 419, 40],
            color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig1)


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
    

    st.write('---')
    st.title('➡️ 전회처분과 처분결과 상황')
    st.text('\n')
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
        
    st.subheader('2. 전회처분 상황')

    fig1 = px.pie(df_re1_5_sum,names=['초범', '기소유예', '선도유예', '보호처분', '형(재산형포함)집행종료'],
        values=[35477, 7632, 1389, 12016, 2885], 
        color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig1)

    st.subheader('3. 처분결과 상황')

    fig2 = px.pie(df_re2_6_sum,names=['구공판_구속', '구공판_불구속', '구약식', '소년보호송치', '기소유예','혐의없음'],
        values=[728, 2721, 2384, 20578, 20108, 4636],
        color_discrete_sequence=px.colors.sequential.RdBu)
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
   



    
    

if __name__ == '__main__':
    main()