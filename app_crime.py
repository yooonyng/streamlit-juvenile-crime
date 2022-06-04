import streamlit as st
import joblib
import numpy as np
import sklearn
from PIL import Image
import os
import base64

def run_crime():
    st.title('🚔소년범죄와 주변환경의 관계')
    st.text('\n')

    image = Image.open('data/img01.jpg')
    st.image(image)
    st.text('\n')

#     st.info("목차\n1. 소년 범죄의 개념\n2. 소년 범죄의 유형\n3. 소년 범죄의 특징\n4. 소년 범죄의 원인")
#     st.text('\n')
#     st.text('\n')

#     st.subheader('1. 소년범죄의 개념')
#     image = Image.open('data/img04.png')
#     st.image(image)
#     st.text('법적으로 미성년에 해당하는 자의 범죄 행위.\n한국에서는 19세 미만 소년의 범죄 행위를 말한다.')
#     st.text('\n')
#     st.text('\n')

#     st.subheader('2. 소년범죄의 유형')
#     st.text('소년 범죄는 그 내용에 따라 폭력범죄, 재산범죄, 강력범죄, 교통사범 등으로 구분된다.')
#     st.text('\n')
#     st.text('\n')

#     st.subheader('3. 소년범죄의 특징')
#     st.text('첫째, 범죄 청소년 평균 연령의 저하이다.\n대중 매체를 통해 청소년 문화 형성의 중심이 저연령화하고 있기 때문이다.')
#     st.text('둘째, 2인 이상의 다수가 공모하여 범죄를 저지르는 집단화 경향의 추세를 보인다.')
#     st.text('셋째, 여성 청소년 범죄가 증가하고 있다.')
#     st.text('넷째, 소년 재범자가 증가하는 추세이다.')
#     st.text('다섯째, 소년 범죄에서 살인, 강도, 강간, 방화와 같은 죄질이 나쁘고\n상대방에게 미치는 피해가 큰 강력범죄가 늘어나고 있다.')
#     st.text('\n')
#     st.text('\n')

#     st.subheader('4. 소년범죄의 원인')
#     st.text('청소년 범죄자의 개인적 특성 및 소질을 중요시하는 개인적 요인')
#     st.text('범죄자를 둘러싼 가정, 학교, 교우관계, 사회의 문화 또는 가치 체계에 의한\n영향을 중요시하는 사회·환경적 요인')
#     st.caption('출처: 네이버 심리학용어사전')



    # @st.cache(allow_output_mutation=True)
    # def get_base64_of_bin_file(bin_file):
    #     with open(bin_file, 'rb') as f:
    #         data = f.read()
    #     return base64.b64encode(data).decode()

    # @st.cache(allow_output_mutation=True)
    # def get_img_with_href(local_img_path, target_url):
    #     img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    #     bin_str = get_base64_of_bin_file(local_img_path)
    #     html_code = f'''
    #         <a href="{target_url}">
    #             <img src="data:image/{img_format};base64,{bin_str}" />
    #         </a>'''
    #     return html_code

    # gif_html = get_img_with_href('data/sum01.png', 'https://www.youtube.com/watch?v=h-WmvzCtRh0')
    # st.markdown(gif_html, unsafe_allow_html=True)

    
   
    # col1,col2 = st.columns(2)
    # with col1:
    #     pass
    # with col2:
    #     pass





    # st.subheader('소년범의 종류')
    # st.text('🔸범죄소년 : 범행 당시 형사책임연령(만 14세 이상 ~ 만 19세 미만)이었던 소년\n형사처벌을 할 수 있으며, 가정법원의 심리에 따라 형사처벌이 아닌 보호처분을 할 수 있다.')
    # st.text('🔸촉법소년 : 범행 당시 형사책임연령이 아니었던 소년 중 만 10세 이상 ~ 만 14세 미만\n범행 당시 형사책임연령이 아니어서 형사처벌을 할 수 없으나, 소년법에 따라 보호처분을 할 수 있다.')
    # st.text('🔸범법소년[3] : 범행 당시 만 10세 미만의 소년\n범행 당시 형사책임연령이 아니어서 형사처벌을 할 수 없고, 소년법에 따른 보호처분도 할 수 없다.')
    # st.text('\n')
    # image = Image.open('data/img02.png')
    # st.image(image)