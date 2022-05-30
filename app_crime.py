import streamlit as st
import joblib
import numpy as np
import sklearn

def run_crime():
    st.subheader('소년 범죄자의 주변 환경과 범죄 처분 결과 상황을 파악')
    st.text('왼쪽 사이드바에서 원하는 항목을 선택하세요.')

