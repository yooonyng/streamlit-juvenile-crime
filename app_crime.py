import streamlit as st
import joblib
import numpy as np
import sklearn
from PIL import Image
import os
import base64

def run_crime():
    st.title('πμλλ²μ£μ μ£Όλ³νκ²½μ κ΄κ³')
    st.text('\n')

    image = Image.open('data/img01.jpg')
    st.image(image)
    st.text('\n')
