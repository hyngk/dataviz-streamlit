import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(
    page_title="streamlit app",
    layout="wide"
)
st.title("K팝 데몬 헌터스(c321022 김하영)")
df=pd.read_csv("naver_news.csv",encoding='utf-8')
df['pubDatd'] = pd.to_datetime(df['pubDatd']) 
df['date'] = df['pubDatd'].dt.date
st.subheader("시간 흐름에 따른 뉴스량")

count = df['date'].value_counts().sort_index()
x = count.index.astype(str)
y = count.values

fig, ax = plt.subplots()
ax.plot(x, y) 
plt.xticks(rotation=45)

st.pyplot(fig) 

st.line_chart(count)
st.image("cloud.png",caption="wordcloud",use_container_width=True)
button1=st.button('snow')
if button1:
    st.snow()
#==========ai 참고==================
start_date = date(2025, 11, 20)
end_date = date(2025, 12, 15)
slider=st.slider('기간선택',start_date,end_date)
#===================================
