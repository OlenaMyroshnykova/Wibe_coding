import streamlit as st


# -------------------------------
# Aplicar estilos CSS de la aplicación
# -------------------------------
def aplicar_estilos():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(120, 0, 60, 0.35), transparent 35%),
                radial-gradient(circle at bottom right, rgba(40, 0, 80, 0.45), transparent 35%),
                linear-gradient(135deg, #07020d 0%, #130015 45%, #050008 100%);
            color: #f2e6ff;
        }

        header[data-testid="stHeader"] {
            background: #07020d !important;
            color: #f2e6ff !important;
        }

        div[data-testid="stDecoration"] {
            background: linear-gradient(90deg, #5c0038, #1f0033) !important;
        }

        div[data-testid="stToolbar"] {
            background: transparent !important;
            color: #f2e6ff !important;
        }

        header button,
        header svg,
        header span {
            color: #f2e6ff !important;
            fill: #f2e6ff !important;
        }

        h1 {
            color: #f5d6ff !important;
            text-shadow: 0 0 12px #9b1d64, 0 0 22px #4b0082;
            font-family: Georgia, serif;
            letter-spacing: 1px;
        }

        h2, h3 {
            color: #e8c3ff !important;
            font-family: Georgia, serif;
        }

        p, div, span, label {
            color: #f1e8ff;
        }

        section[data-testid="stSidebar"] {
            background:
                linear-gradient(180deg, #140018 0%, #07020d 100%);
            border-right: 1px solid #6d214f;
        }

        section[data-testid="stSidebar"] h1,
        section[data-testid="stSidebar"] h2,
        section[data-testid="stSidebar"] h3 {
            color: #ffd6f6 !important;
            text-shadow: 0 0 10px #8e164e;
        }

        .stTextInput input {
            background-color: #16001f !important;
            color: #fff0fb !important;
            border: 1px solid #c84b8c !important;
            border-radius: 12px !important;
        }

        .stTextInput input::placeholder {
            color: #8f7899 !important;
        }

        .stSelectbox div[data-baseweb="select"] > div {
            background-color: #16001f !important;
            color: #fff0fb !important;
            border: 1px solid #c84b8c !important;
            border-radius: 12px !important;
        }

        .stSelectbox div[data-baseweb="select"] span {
            color: #fff0fb !important;
        }

        .stSelectbox svg {
            fill: #c84b8c !important;
            color: #c84b8c !important;
        }

        div[data-baseweb="popover"] {
            background-color: transparent !important;
        }

        ul[role="listbox"] {
            background-color: #16001f !important;
            border: 1px solid #c84b8c !important;
            border-radius: 12px !important;
            box-shadow: 0 0 18px rgba(200, 75, 140, 0.55) !important;
            padding: 6px !important;
        }

        li[role="option"] {
            background-color: #16001f !important;
            color: #fff0fb !important;
            border-radius: 8px !important;
        }

        li[role="option"] div,
        li[role="option"] span {
            color: #fff0fb !important;
        }

        li[role="option"]:hover {
            background-color: #5c0038 !important;
            color: #ffffff !important;
        }

        li[role="option"]:hover div,
        li[role="option"]:hover span {
            color: #ffffff !important;
        }

        li[aria-selected="true"] {
            background-color: #3a003f !important;
            color: #ffffff !important;
        }

        li[aria-selected="true"] div,
        li[aria-selected="true"] span {
            color: #ffffff !important;
        }

        .stButton > button {
            background: linear-gradient(135deg, #5c0038, #1f0033) !important;
            color: #fff0fb !important;
            border: 1px solid #c84b8c !important;
            border-radius: 14px !important;
            padding: 0.55rem 1rem !important;
            font-weight: bold !important;
            box-shadow: 0 0 12px rgba(200, 75, 140, 0.45);
            transition: all 0.2s ease-in-out;
        }

        .stButton > button:hover {
            transform: scale(1.03);
            background: linear-gradient(135deg, #8a0058, #33004d) !important;
            box-shadow: 0 0 20px rgba(255, 120, 190, 0.75);
        }

        div[data-testid="stMetric"] {
            background: rgba(20, 0, 30, 0.78);
            border: 1px solid #7d1b52;
            border-radius: 18px;
            padding: 18px;
            box-shadow: 0 0 18px rgba(80, 0, 120, 0.45);
        }

        div[data-testid="stMetricLabel"] {
            color: #e8c3ff !important;
        }

        div[data-testid="stMetricValue"] {
            color: #ffffff !important;
            text-shadow: 0 0 10px #b5179e;
        }

        div[data-testid="stAlert"] {
            border-radius: 16px;
            border: 1px solid #7d1b52;
            background-color: rgba(20, 0, 30, 0.78);
            box-shadow: 0 0 14px rgba(100, 0, 120, 0.35);
        }

        div[data-testid="stDataFrame"] {
            border: 1px solid #7d1b52;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 0 14px rgba(100, 0, 120, 0.35);
        }

        div[data-testid="stVegaLiteChart"],
        div[data-testid="stArrowVegaLiteChart"] {
            background: rgba(12, 0, 20, 0.65);
            border-radius: 18px;
            padding: 14px;
            border: 1px solid #7d1b52;
            box-shadow: 0 0 14px rgba(110, 0, 90, 0.35);
        }

        details {
            background: rgba(12, 0, 20, 0.75) !important;
            border: 1px solid #7d1b52 !important;
            border-radius: 16px !important;
        }

        summary {
            color: #f5d6ff !important;
            font-weight: bold;
        }

        .goth-divider {
            border-top: 1px solid #7d1b52;
            margin: 18px 0;
        }

        /* Tabla minimalista de registros */
        .record-separator {
            border-bottom: 1px solid rgba(200, 75, 140, 0.20);
            margin: 4px 0 8px 0;
        }

        .record-text {
            font-size: 0.95rem;
            color: #f2e6ff;
        }

        .record-name {
            font-weight: bold;
            color: #fff0fb;
        }

        .record-energy {
            font-weight: bold;
            color: #ffd6f6;
        }

        .goth-symbol {
            position: fixed;
            top: -60px;
            z-index: 999999;
            pointer-events: none;
            animation-name: goth-fall;
            animation-timing-function: linear;
            animation-fill-mode: forwards;
            text-shadow: 0 0 10px #ff4fa3;
        }

        @keyframes goth-fall {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 1;
            }
            80% {
                opacity: 1;
            }
            100% {
                transform: translateY(110vh) rotate(360deg);
                opacity: 0;
            }
        }

        .white-spider {
            position: fixed;
            top: -60px;
            z-index: 999998;
            pointer-events: none;
            animation-name: spider-fall;
            animation-timing-function: linear;
            animation-fill-mode: forwards;
            color: white;
            text-shadow: 0 0 8px #ffffff, 0 0 14px #cfcfff;
        }

        @keyframes spider-fall {
            0% {
                transform: translateY(0) rotate(0deg);
                opacity: 1;
            }
            85% {
                opacity: 1;
            }
            100% {
                transform: translateY(110vh) rotate(25deg);
                opacity: 0;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )