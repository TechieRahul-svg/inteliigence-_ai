import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin-bottom: 48px;
            margin-top: 24px;
        ">
            <div style="
                background: rgba(124,58,237,0.08);
                padding: 24px;
                border-radius: 24px;
                border: 1px solid rgba(124,58,237,0.2);
                box-shadow: 0 16px 48px rgba(124,58,237,0.12);
                margin-bottom: 24px;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <img src='{logo_url}' style='height: 80px;' />
            </div>
            <h1 style='
                text-align: center;
                margin: 0 0 8px 0;
                font-weight: 800;
                font-size: 3rem;
                letter-spacing: -0.06em;
                background: linear-gradient(135deg, #FFFFFF 0%, #D1D5DB 50%, #8B5CF6 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Plus Jakarta Sans", sans-serif;
            '>SNAPCLASS</h1>
            <p style='
                color: #6B7280;
                font-size: 1rem;
                text-align: center;
                margin: 0;
                font-weight: 400;
                font-family: "Plus Jakarta Sans", sans-serif;
                letter-spacing: 0.05em;
                text-transform: uppercase;
            '>AI-Powered Attendance</p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"

    st.markdown(f"""
        <div style="
            display: flex;
            align-items: center;
            gap: 16px;
            padding-bottom: 8px;
        ">
            <div style="
                background: rgba(124,58,237,0.08);
                padding: 10px;
                border-radius: 12px;
                border: 1px solid rgba(124,58,237,0.15);
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 4px 16px rgba(0,0,0,0.2);
            ">
                <img src='{logo_url}' style='height: 40px;' />
            </div>
            <div>
                <h2 style='
                    margin: 0;
                    font-weight: 800;
                    font-size: 1.5rem;
                    letter-spacing: -0.04em;
                    color: #F9FAFB;
                    font-family: "Plus Jakarta Sans", sans-serif;
                '>SnapClass</h2>
                <p style='
                    margin: 0;
                    color: #6B7280;
                    font-size: 0.75rem;
                    font-weight: 500;
                    letter-spacing: 0.06em;
                    text-transform: uppercase;
                    font-family: "Plus Jakarta Sans", sans-serif;
                '>AI Attendance</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
