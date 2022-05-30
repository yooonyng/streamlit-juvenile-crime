import streamlit as st
import joblib
import numpy as np
import pandas as pd
import altair as alt
import plotly.express as px

df_crime = pd.read_csv('data/대검찰청_소년범죄자 범행동기_20171231.csv',encoding='cp949')

def run_top5():
    top5 = df_crime['총범죄건수'].sort_values(ascending=False).head()
    top5 = top5.to_frame()
    top5_chart = px.bar(top5,x='lang',y='Sum')
    st.plotly_chart(top5_chart)

    # df4_sorted = df4.sort_values('Sum',ascending=False)
    # fig2 = px.bar(df4_sorted,x='lang',y='Sum')
    # st.plotly_chart(fig2)

if __name__ == '__main__':
    main()