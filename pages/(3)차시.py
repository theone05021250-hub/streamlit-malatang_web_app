import streamlit as st

# 쿠키변수 login, password 초기화 
if 'login' not in st.session_state:
    st.session_state['login'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''


st.title(' 3차시 : 자율주행자동차 개념 학습 및 윤리적 문제 해결')

st.markdown('---')
with st.expander(' (1) 자율주행자동차의 도로 주행 영상'):
    st.write('- 영상을 시청하고 상황별 자율주행자동차의 작동 방식 생각해보자')
    url = 'https://www.youtube.com/watch?v=GXfjAArAuFc'
    st.video(url)
with st.expander(' (2) 자율주행자동차의 상황별 작동 방식을 흐름도로 표현'):
    st.write(' _________________________________')
with st.expander(' (3) 작성한 흐름도를 공유 및 피드백 나눔 '):
    st.write(' _________________________________')
with st.expander(' (4) 자율주행자동차와 관련된 SSI를 기반으로 책임 측면에서 기술 발전의 윤리적 한계와 사회 적용 문제를 다양한 윤리적 관점에서 토론 '):
    st.write(' _________________________________')