import streamlit as st
from app_crime import run_crime
from app_top10 import run_top10
from app_parents import run_parents
from app_result import run_result



def main():

    menu = ['소년범죄','사회적 시선','주변 환경','전회처분과 처분결과 상황']
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0]:
        run_crime()
    elif choice == menu[1]:
        run_top10()
    elif choice == menu[2]:
        run_parents()
    elif choice == menu[3]:
        run_result()
    
    

if __name__ == '__main__':
    main()