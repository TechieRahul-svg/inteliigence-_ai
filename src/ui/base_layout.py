import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: 
                    radial-gradient(ellipse at 10% 10%, rgba(124,58,237,0.18) 0%, transparent 50%),
                    radial-gradient(ellipse at 90% 90%, rgba(99,102,241,0.15) 0%, transparent 50%),
                    radial-gradient(ellipse at 50% 50%, rgba(6,182,212,0.06) 0%, transparent 60%),
                    #0B1120 !important;
                min-height: 100vh;
            }

            /* Home page role selection cards */
            .stApp div[data-testid="stColumn"] {
                background: rgba(17,24,39,0.55) !important;
                backdrop-filter: blur(24px) saturate(1.3) !important;
                -webkit-backdrop-filter: blur(24px) saturate(1.3) !important;
                border: 1px solid rgba(255,255,255,0.06) !important;
                padding: 2.5rem 2rem !important;
                border-radius: 20px !important;
                box-shadow:
                    0 8px 32px rgba(0,0,0,0.4),
                    inset 0 1px 0 rgba(255,255,255,0.04) !important;
                transition: all 0.4s cubic-bezier(0.16,1,0.3,1) !important;
                text-align: center !important;
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                position: relative !important;
                overflow: hidden !important;
            }

            .stApp div[data-testid="stColumn"]::before {
                content: '';
                position: absolute;
                top: 0; left: 0; right: 0;
                height: 3px;
                background: linear-gradient(90deg, #7C3AED, #06B6D4, #7C3AED);
                opacity: 0;
                transition: opacity 0.4s ease;
            }

            .stApp div[data-testid="stColumn"]:hover {
                transform: translateY(-8px) !important;
                border-color: rgba(124,58,237,0.35) !important;
                box-shadow:
                    0 20px 60px rgba(124,58,237,0.15),
                    0 8px 32px rgba(0,0,0,0.4),
                    inset 0 1px 0 rgba(255,255,255,0.06) !important;
            }

            .stApp div[data-testid="stColumn"]:hover::before {
                opacity: 1;
            }

            .stApp div[data-testid="stColumn"] img {
                margin-top: 8px !important;
                margin-bottom: 20px !important;
                filter: drop-shadow(0 12px 28px rgba(124,58,237,0.25)) !important;
                transition: transform 0.4s cubic-bezier(0.16,1,0.3,1) !important;
            }

            .stApp div[data-testid="stColumn"]:hover img {
                transform: scale(1.08) translateY(-4px) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background:
                    radial-gradient(ellipse at 0% 0%, rgba(124,58,237,0.08) 0%, transparent 50%),
                    radial-gradient(ellipse at 100% 100%, rgba(6,182,212,0.08) 0%, transparent 50%),
                    #0B1120 !important;
                min-height: 100vh;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        /* ═══════════════════════════════════════
           HIDE STREAMLIT CHROME
           ═══════════════════════════════════════ */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding-top: 1.5rem !important; }

        /* ═══════════════════════════════════════
           TYPOGRAPHY
           ═══════════════════════════════════════ */
        h1 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 800 !important;
            letter-spacing: -0.04em !important;
            background: linear-gradient(135deg, #FFFFFF 0%, #E5E7EB 60%, #8B5CF6 100%) !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            font-size: 2.6rem !important;
            line-height: 1.15 !important;
            margin-bottom: 0.25rem !important;
        }

        h2 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 700 !important;
            letter-spacing: -0.03em !important;
            color: #F9FAFB !important;
            font-size: 1.75rem !important;
            line-height: 1.25 !important;
            margin-bottom: 0.25rem !important;
        }

        h3 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            color: #E5E7EB !important;
            font-size: 1.25rem !important;
        }

        h4, h5, h6 {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            color: #D1D5DB !important;
        }

        p, label, li, span, small, div {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }

        p, span, small {
            color: #9CA3AF !important;
        }

        label {
            color: #D1D5DB !important;
            font-weight: 500 !important;
            font-size: 0.875rem !important;
        }

        /* ═══════════════════════════════════════
           SCROLLBAR
           ═══════════════════════════════════════ */
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: rgba(255,255,255,0.08);
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(124,58,237,0.4);
        }

        /* ═══════════════════════════════════════
           INPUT FIELDS
           ═══════════════════════════════════════ */
        div[data-testid="stTextInput"] input,
        div[data-testid="stNumberInput"] input {
            background-color: rgba(17,24,39,0.6) !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            border-radius: 10px !important;
            color: #F9FAFB !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            padding: 12px 16px !important;
            font-size: 0.95rem !important;
            transition: all 0.25s ease !important;
        }

        div[data-testid="stTextInput"] input:focus,
        div[data-testid="stNumberInput"] input:focus {
            border-color: #7C3AED !important;
            box-shadow: 0 0 0 3px rgba(124,58,237,0.15), 0 0 20px rgba(124,58,237,0.1) !important;
            background-color: rgba(17,24,39,0.8) !important;
        }

        div[data-testid="stTextInput"] input::placeholder {
            color: #6B7280 !important;
        }

        /* ═══════════════════════════════════════
           SELECT BOX
           ═══════════════════════════════════════ */
        div[data-testid="stSelectbox"] div[role="button"] {
            background-color: rgba(17,24,39,0.6) !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            border-radius: 10px !important;
            color: #F9FAFB !important;
        }

        /* ═══════════════════════════════════════
           BUTTONS
           ═══════════════════════════════════════ */
        button {
            border-radius: 10px !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            padding: 10px 24px !important;
            border: none !important;
            transition: all 0.25s cubic-bezier(0.16,1,0.3,1) !important;
            letter-spacing: -0.01em !important;
        }

        button[kind="primary"] {
            background: linear-gradient(135deg, #7C3AED 0%, #6366F1 100%) !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 14px rgba(124,58,237,0.3) !important;
        }
        button[kind="primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(124,58,237,0.5) !important;
        }

        button[kind="secondary"] {
            background: linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%) !important;
            color: #FFFFFF !important;
            box-shadow: 0 4px 14px rgba(6,182,212,0.25) !important;
        }
        button[kind="secondary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 25px rgba(6,182,212,0.45) !important;
        }

        button[kind="tertiary"] {
            background: rgba(31,41,55,0.5) !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            color: #D1D5DB !important;
        }
        button[kind="tertiary"]:hover {
            transform: translateY(-1px) !important;
            background: rgba(31,41,55,0.8) !important;
            border-color: rgba(255,255,255,0.15) !important;
            color: #F9FAFB !important;
        }

        /* ═══════════════════════════════════════
           DIVIDER
           ═══════════════════════════════════════ */
        hr {
            border-color: rgba(255,255,255,0.06) !important;
            margin: 1rem 0 !important;
        }

        /* ═══════════════════════════════════════
           STREAMLIT CONTAINERS
           ═══════════════════════════════════════ */
        div[data-testid="stAlert"] {
            background-color: rgba(17,24,39,0.4) !important;
            border: 1px solid rgba(255,255,255,0.06) !important;
            border-radius: 12px !important;
            backdrop-filter: blur(8px) !important;
        }

        /* Container with border */
        div[data-testid="stVerticalBlock"] > div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: rgba(17,24,39,0.4) !important;
            border: 1px solid rgba(255,255,255,0.06) !important;
            border-radius: 16px !important;
            backdrop-filter: blur(8px) !important;
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid rgba(255,255,255,0.06) !important;
            border-radius: 12px !important;
            overflow: hidden !important;
        }

        /* ═══════════════════════════════════════
           DIALOG
           ═══════════════════════════════════════ */
        div[role="dialog"] {
            background-color: #111827 !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            border-radius: 16px !important;
            box-shadow: 0 25px 50px rgba(0,0,0,0.5) !important;
        }

        /* ═══════════════════════════════════════
           FILE UPLOADER
           ═══════════════════════════════════════ */
        div[data-testid="stFileUploader"] {
            background-color: rgba(17,24,39,0.3) !important;
            border: 2px dashed rgba(255,255,255,0.08) !important;
            border-radius: 12px !important;
            padding: 20px !important;
            transition: all 0.3s ease !important;
        }
        div[data-testid="stFileUploader"]:hover {
            border-color: rgba(124,58,237,0.4) !important;
            background-color: rgba(124,58,237,0.03) !important;
        }

        /* ═══════════════════════════════════════
           CAMERA INPUT
           ═══════════════════════════════════════ */
        div[data-testid="stCameraInput"] {
            border-radius: 16px !important;
            overflow: hidden !important;
        }
        div[data-testid="stCameraInput"] video {
            border-radius: 12px !important;
        }

        /* ═══════════════════════════════════════
           TOAST / NOTIFICATION
           ═══════════════════════════════════════ */
        div[data-testid="stToast"] {
            background-color: #1F2937 !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 12px !important;
            color: #E5E7EB !important;
        }

        /* ═══════════════════════════════════════
           SPINNER
           ═══════════════════════════════════════ */
        div[data-testid="stSpinner"] > div {
            border-top-color: #7C3AED !important;
        }

        /* ═══════════════════════════════════════
           TABS (using columns as tabs)
           ═══════════════════════════════════════ */
        div[data-testid="stHorizontalBlock"] {
            gap: 0.75rem !important;
        }

        </style>
    """, unsafe_allow_html=True)