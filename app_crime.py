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
