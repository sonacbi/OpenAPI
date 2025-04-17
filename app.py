import streamlit as st

# 처음에 사이드가 바로 펴 있는 상태가 아니게
# wide : 가로로 넓게

# st.set_page_config(
#   initial_sidebar_state="collapsed", layout="wide", page_icon="🎈",
#   page_title = "나만의 스트링릿 앱"
# )

# with st.sidebar:
#   st.write("안녕~~ 사이드바")
#   st.write("닫을 수도 있습니다")
  
# st.write("이건 메인페이지에 있는 텍스트")

import pandas as pd
import numpy as np
from PIL import Image
from time import sleep

st.set_page_config(
  page_icon="🎆",
  page_title = "인공지능 ~~ 스트림핏 배포하기",
  layout="wide"
  
)

with st.spinner(text="페이지 로딩중....") :
  sleep(3)


st.header("~~~ 페이지에 오신걸 환영합니다~~")
st.subheader("스트림릿 기능 맛보기")

cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "17 °C", "2 °F")
cols[0].metric("10/13", "15 °C", "2")
cols[1].metric("10/14", "17 °C", "2 °F")
cols[1].metric("10/15", "14 °C", "-3 °F")
cols[1].metric("10/16", "13 °C", "-1 °F")

chart_data = pd.DataFrame(
  np.random.randn(20,3),
  columns=['a', 'b', 'c']
)

cols[2].line_chart(chart_data)