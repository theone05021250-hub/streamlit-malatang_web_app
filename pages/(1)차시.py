import streamlit as st

# 쿠키변수 login, password 초기화 
if 'login' not in st.session_state:
    st.session_state['login'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''


st.title(' 1차시 : 스마트모빌리티 이론학습, 자율주행자동차 개념적 이론, 윤리적 문제와 해결방안 구상 ')

st.markdown('---')
with st.expander(' (1) 스마트시티란? '):
    st.write('세종에 구현할 스마트시티를 보다 통합적인 관점에서 정의하면,')
    st.write('도시에서 벌어지는 모든 현상과 움직임, 시민들의 행동들을 전부 데이터화해서, 이를 인공지능으로 분석해 도시인들의 삶의 질과 행복, 도시의 지속가능성을 높이는 맞춤형 예측 서비스를 제공하는 플랫폼으로서의 도시')
    url = 'https://youtu.be/Be5RPxrokMo?list=PLkE78JTeduuy-Hm9Zdty7S4Uu7Wr2tpPa'
    st.video(url)
    url = 'https://youtu.be/Vb7LBpGc-Xg?list=PLkE78JTeduuy-Hm9Zdty7S4Uu7Wr2tpPa'
    st.video(url)
with st.expander(' (2) 스마트 모빌리티란? '):
    st.write(' 스마트 모빌리티(Smart Mobility)는 첨단 정보통신기술(ICT)을 활용하여 기존 교통 시스템의 효율성과 안전성을 높이고, 사람들의 이동을 더욱 편리하고 지속 가능하게 만드는 새로운 이동 방식 및 관련 기술, 서비스를 포괄하는 개념 ')
    st.write(' 주요 개념 및 특징 ' )
    st.write(' 첨단 기술 융합: 전자 제어, 통신, 인공지능(AI), 빅데이터 등 다양한 첨단 기술이 이동 수단 및 교통 인프라에 접목됩니다.')
    st.write(' 효율성 및 안전성 향상: 실시간 교통 정보 분석, 자율 주행 등을 통해 교통 혼잡을 줄이고 사고율을 낮추는 것을 목표로 합니다.')
    st.write(' 지속 가능성 추구: 친환경 동력원(전기, 수소 등)을 사용하고 차량 공유 등을 통해 에너지 효율을 높이고 환경 오염을 줄입니다.')
    st.write(' 서비스 통합 (MaaS, Mobility as a Service): 다양한 교통 수단을 하나의 플랫폼에서 예약, 이용, 결제할 수 있는 통합 서비스도 포함됩니다.')
    c1, c2 = st.columns(2)
    with c1:
        st.image('./1ch_smart_M.png', use_container_width=True)
    with c2:
        st.image('./1ch_smart_M2.png', use_container_width=True)
    st.write(' _________________________________')
    st.write(' [세종시의 모빌리티 서비스 운영 계획]')
    st.write('  [1] 무인 자율주행 셔틀 서비스 -버스노선 BRT 구간 자율주행 셔틀 도입')
    st.image('./1ch_brt.png', width=550)
    st.write(' (세종 교통 버스노선 자율주행버스 확대와 관련한 뉴스 자료)')
    col1, col2, col3 = st.columns([1, 3, 1])  # 가운데 컬럼이 넓음
    with col2:
        url = 'https://youtu.be/wKb9p8Ui39w'
        st.video(url)
    st.write(' _________________________________')
    st.write('  [2] 자율주행 기반 대중교통시스템 실증연구를 기반으로 하여 전체 생활권 확대 (C-ITS 구축)')
    st.write(' C-ITS란? 협력 지능형 교통 체계(Cooperative-Intelligent Transport Systems)의 약자로, 차량과 도로가 서로 통신하며 교통 정보를 실시간으로 공유하여 교통사고를 예방하고 이동성을 향상하는 차세대 지능형 교통 시스템입니다.')
    st.image('./1ch_c-its.png', width=550)
    st.write(' (C-ITS 시스템 소개 영상)')
    url = 'https://youtu.be/u5SaMRLeMFk'
    st.video(url)
    st.write(' _________________________________')
    st.write('  [3] 보행안전 서비스 제공으로 안전하고 쾌적한 보행환경 구축')
    st.write(' 스마트 횡단보도 서비스 : 횡단보도 부근 교통사고 방지와 안전한 보행을 지원하기 위해 보행자 감지, 자동차 정지 감지 시스템 등으로 사전에 교통사고를 예방하며, 보행자의 안전하고 쾌적한 보행을 지원')
    st.write(' 스쿨존 안전 서비스 : 스쿨존 지역내 CCTV 영상분석 처리 및 검지센서를 통한 횡단보도 보행자 안전 강화 및 교통사고 예방 서비스')
    st.image('./1ch_safety_survice.png', width=550)
    st.write(' (세종스마트시티 스마트 횡단보도 실제 적용 횡단보도 소개, 이용자 인터뷰 영상)')
    url = 'https://youtu.be/SrJ87JlM0jI'
    st.video(url)
with st.expander(' (3) 인공지능의 개념과 특성 학습 '):
    st.write('---')
    st.write(' _________________________________')
with st.expander(' (4) 스마트 모빌리티에서의 AI 활용 사례 찾기 '):
    st.write('---')
    st.write(' _________________________________')
with st.expander(' (5) 스마트 모빌리티와 관련된 공정성 · 형평성 문제, 프라이버시 및 데이터 윤리 문제 '):
    st.write('---')
    st.write(' _________________________________')
