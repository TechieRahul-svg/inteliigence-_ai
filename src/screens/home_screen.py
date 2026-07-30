import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    style_background_home()
    style_base_layout()
    header_home()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="text-align:center;">
                <p style="
                    color: #7C3AED !important;
                    font-weight: 600;
                    font-size: 0.75rem;
                    letter-spacing: 0.1em;
                    text-transform: uppercase;
                    margin-bottom: 4px;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                ">FOR STUDENTS</p>
            </div>
        """, unsafe_allow_html=True)
        st.header("I'm Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        st.markdown('<p style="color:#6B7280 !important; text-align:center; font-size:0.85rem; font-family: Plus Jakarta Sans, sans-serif;">Login with Face ID to mark your attendance instantly</p>', unsafe_allow_html=True)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='home_student_btn'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="text-align:center;">
                <p style="
                    color: #06B6D4 !important;
                    font-weight: 600;
                    font-size: 0.75rem;
                    letter-spacing: 0.1em;
                    text-transform: uppercase;
                    margin-bottom: 4px;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                ">FOR TEACHERS</p>
            </div>
        """, unsafe_allow_html=True)
        st.header("I'm Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        st.markdown('<p style="color:#6B7280 !important; text-align:center; font-size:0.85rem; font-family: Plus Jakarta Sans, sans-serif;">Manage classes, take attendance with AI</p>', unsafe_allow_html=True)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='home_teacher_btn'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()