import streamlit as st
import pandas as pd
import os

# --- 0. 세션 상태 초기화 (필수) ---
# 앱을 처음 로드할 때 오류가 나지 않도록 변수를 미리 정의
if 'login' not in st.session_state:
    st.session_state['login'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''
if 'is_authenticated' not in st.session_state:
    st.session_state['is_authenticated'] = False

st.title(' 스마트 모빌리티 프로젝트: AI와 교통을 디자인하다. ')

# --- 1. 메인 앱 콘텐츠 (로그인 성공 시) ---
# 조건문을 is_authenticated로 변경하여 더 명확하게 관리하는 것을 권장
if st.session_state['is_authenticated']:
    st.info(f'Welcome, 어서오세요 {st.session_state["login"]}님.....',)
    st.markdown('---')
    
    # 로그오프 버튼을 메인 콘텐츠 영역이나 사이드바에 명확히 위치시킵니다.
    if st.sidebar.button('로그오프', key='main_logoff'):
        st.session_state['login'] = ''
        st.session_state['password'] = ''
        st.session_state['is_authenticated'] = False
        st.rerun()

    col1, col2 = st.columns((4,1))
    with col1:
        with st.expander('개인정보 등록..'):
            # 학생 등록 정보를 입력해서 받는 부분
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input('이름: ', key='name')
                school = st.text_input('학교명: ', key='school')
                age = st.number_input('나이: ', min_value=1, max_value=120, step=1)
            with c2:
                address = st.text_input('주소: ', key='address')
                # 콤마 대신 리스트를 사용하는 것이 더 깔끔합니다.
                grade = st.selectbox('학년: ', [f'{x}학년' for x in range(1,7)], key='grade') 
                birthday = st.date_input('생년월일: ', value=None, key='birthday')

            if st.button('제출하기'):
                # age는 number_input이므로 0이 아닌 1로 min_value 설정하여 True/False 대신 값 자체를 확인합니다.
                # birthday가 None이 아닌지 확인합니다.
                if all([name, school, age, address, grade, birthday is not None]):
                    st.success('제출되었습니다.')
                else:
                    st.error('모두 필수 입력입니다.')

# --- 2. 로그인/등록 페이지 (로그아웃 상태) ---
else:
    # data.csv 파일이 없으면 생성 (헤더 포함)
    if not os.path.exists('./data.csv'):
        with open('./data.csv', 'w') as f:
            f.write('login,password,email\n')

    cc1, cc2 = st.columns(2)
    with cc1:
        # 이미지 파일이 현재 경로에 있는지 확인하세요.
        try:
            st.image('./login_background_image.jpg')
        except FileNotFoundError:
             st.info("로그인 이미지를 찾을 수 없습니다. (./login_background_image.jpg)")

    with cc2: 
        t1, t2 = st.tabs(('Login', 'Register'))
        
        # 2.1. 로그인 탭
        with t1: 
            # 폼 사용으로 버튼 클릭 시 전체 재실행 방지 (선택 사항)
            with st.form('Login_Form'):
                login_id = st.text_input('User ID', key='login_id')
                login_pw = st.text_input('Password', type='password', key='login_pw')
                
                if st.form_submit_button('로그인'):
                    if all([login_id, login_pw]):
                        try:
                            df = pd.read_csv('./data.csv')
                        except pd.errors.EmptyDataError:
                             st.error('등록된 사용자가 없습니다. Register 탭에서 등록해주세요.')
                             st.stop()
                        
                        # 사용자 ID로 필터링
                        user_row = df[df['login'] == login_id]

                        if not user_row.empty:
                            # --- 핵심 수정: 비밀번호 확인 로직 추가 ---
                            stored_password = user_row.iloc[0]['password']
                            if stored_password == login_pw:
                                st.session_state['login'] = login_id
                                # st.session_state['password'] 저장은 불필요하지만 기존 코드 유지를 위해 남김
                                st.session_state['password'] = login_pw 
                                st.session_state['is_authenticated'] = True # 인증 상태 플래그
                                
                                st.success('로그인이 되었습니다.')
                                # --- 핵심 수정: 로그인 성공 후 즉시 페이지 갱신 ---
                                st.rerun() 
                            else:
                                st.error('비밀번호가 일치하지 않습니다.')
                        else:
                            st.error('등록된 사용자 ID가 아닙니다.')
                    else:
                        st.error('아이디와 패스코드는 필수입력입니다.')
        
        # 2.2. 등록 탭
        with t2:
            with st.form('Register_Form'):
                reg_login = st.text_input('User ID: ', key='reg_userid_input')
                reg_password = st.text_input('Password: ', type='password', key='reg_password_input')
                reg_email = st.text_input('Email : ', key='reg_email_input')
                
                if st.form_submit_button('저장하기'):
                    if all([reg_login, reg_password, reg_email]):
                        if '@' in reg_email and '.' in reg_email: # 이메일 유효성 간단 검사 추가
                            try:
                                df = pd.read_csv('./data.csv')
                                if reg_login in list(df['login']):
                                    st.error("이미 존재하는 사용자 ID입니다.")
                                    st.stop()
                            except pd.errors.EmptyDataError:
                                # 파일이 비어 있어도 등록은 가능하므로 통과
                                pass
                                
                            # 파일을 'a'(추가 모드)로 열어 데이터 저장
                            with open('./data.csv', 'a') as f:
                                # CSV 형식에 맞게 데이터 저장
                                inputtxt = f'{reg_login},{reg_password},{reg_email}\n' 
                                f.write(inputtxt)

                            st.success('회원 정보가 저장되었습니다. 자동으로 로그인됩니다.')
                            
                            # 등록 성공 후 바로 로그인 상태로 전환
                            st.session_state['login'] = reg_login
                            st.session_state['password'] = reg_password 
                            st.session_state['is_authenticated'] = True
                            st.rerun()
                        else:
                            st.error('유효한 이메일 주소가 아닙니다.')
                    else:
                        st.error('모든 입력 필드는 필수입니다.')
st.markdown('---')
st.write('copyright ....... since 2025')