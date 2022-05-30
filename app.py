import streamlit as st
import pandas as pd 
import numpy as np 
import random
import seaborn as sb
from fbprophet import Prophet
import matplotlib.pyplot as plt

def main():
    st.title('소년범죄')

    menu = ['상위 범죄순위','부모관계','교육정도','정신상태','전회처분 상황','처분결과 상황','재범기간']
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0]:
        pass
    elif choice == menu[1]:
        pass
    elif choice == menu[2]:
        pass
    elif choice == menu[3]:
        pass
    elif choice == menu[4]:
        pass
    elif choice == menu[5]:
        pass
    elif choice == menu[6]:
        pass

if __name__ == '__main__':
    main()