import streamlit as st
from app_crime import run_crime
from app_top5 import run_top5
from app_parents import run_parents
from app_study import run_study
from app_mental import run_mental
from app_result1 import run_result1
from app_result2 import run_result2
from app_again import run_again


def main():

    menu = ['소년범죄','상위 범죄순위','부모관계','교육정도','정신상태','전회처분 상황','처분결과 상황','재범기간']
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0]:
        run_crime()
    elif choice == menu[1]:
        run_top5()
    elif choice == menu[2]:
        run_parents()
    elif choice == menu[3]:
        run_study()
    elif choice == menu[4]:
        run_mental()
    elif choice == menu[5]:
        run_result1()
    elif choice == menu[6]:
        run_result2()
    elif choice == menu[7]:
        run_again()

if __name__ == '__main__':
    main()