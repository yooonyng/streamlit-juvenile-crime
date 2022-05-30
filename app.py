import streamlit as st
from app_crime import run_crime
from app_top5 import run_top5


def main():
    st.title('소년범죄')
    st.subheader('This is a subheader')

    menu = ['소년범죄','상위 범죄순위','부모관계','교육정도','정신상태','전회처분 상황','처분결과 상황','재범기간']
    choice = st.sidebar.selectbox('메뉴 선택',menu)

    if choice == menu[0]:
        run_crime()
    elif choice == menu[1]:
        run_top5
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
    elif choice == menu[7]:
        pass

if __name__ == '__main__':
    main()