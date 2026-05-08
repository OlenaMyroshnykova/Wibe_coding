import base64
from pathlib import Path
import streamlit as st

BASE_DIR = Path(__file__).parent

def image_to_base64(relative_path: str) -> str:
    full_path = BASE_DIR / relative_path
    return base64.b64encode(full_path.read_bytes()).decode("utf-8")

def aplicar_estilos():
    slime_b64 = image_to_base64("assets/slime_top_clean_2048x370.webp")

    st.markdown(
        f"""
        <style>

        /* Фон — таргетируем и body и stApp */
        body, .stApp {{
            background: 
                radial-gradient(circle at top left, rgba(140, 0, 110, 0.35), transparent 34%),
                radial-gradient(circle at bottom right, rgba(70, 0, 130, 0.45), transparent 36%),
                linear-gradient(135deg, #07020d 0%, #16001f 50%, #050008 100%) !important;
            color: #f2e6ff;
        }}

        /* Убираем белый фон у основного контейнера */
        .stApp > div:first-child {{
            background: transparent !important;
        }}

        /* Streamlit main wrapper */
        [data-testid="stAppViewContainer"] {{
            background: transparent !important;
        }}

        [data-testid="stMain"] {{
            background: transparent !important;
        }}

        /* Слизь сверху */
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: clamp(115px, 19vw, 245px);
            z-index: 100;
            pointer-events: none;
            background-image: url("data:image/webp;base64,{slime_b64}");
            background-repeat: no-repeat;
            background-position: top center;
            background-size: 100vw auto;
            opacity: 0.92;
            animation: slimeMove 14s ease-in-out infinite alternate;
            will-change: transform;
        }}

        @keyframes slimeMove {{
            from {{ transform: translate3d(-6px, -8px, 0) scaleY(0.96); }}
            to   {{ transform: translate3d(6px, 3px, 0) scaleY(1.02); }}
        }}

        /* Хедер */
        header[data-testid="stHeader"] {{
            background: rgba(7, 2, 13, 0.72) !important;
            z-index: 10;
        }}

        /* Sidebar */
        section[data-testid="stSidebar"] {{
            background: rgba(8, 0, 18, 0.92) !important;
            border-right: 1px solid rgba(190, 120, 255, 0.18);
            z-index: 4;
        }}
        section[data-testid="stSidebar"] * {{
            color: #f2e6ff;
        }}
        section[data-testid="stSidebar"] label {{
            color: #e9d5ff !important;
            font-weight: 600;
        }}

        /* Основной контент — отступ под слизь */
        .stApp .block-container,
        [data-testid="stMainBlockContainer"] {{
            margin-top: clamp(115px, 19vw, 245px) !important;
            background: rgba(10, 0, 18, 0.84);
            border-radius: 24px;
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            box-shadow: 0 0 35px rgba(120, 0, 160, 0.25);
        }}

        /* Тексты */
        h1, h2, h3 {{
            color: #e9d5ff !important;
            text-shadow: 0 0 12px rgba(170, 60, 255, 0.75);
        }}
        p {{ color: #f2e6ff; }}
        label {{ color: #e9d5ff !important; }}

        /* Inputs */
        .stTextInput input,
        .stNumberInput input,
        .stTextArea textarea {{
            background-color: rgba(25, 5, 42, 0.96) !important;
            color: #f2e6ff !important;
            border: 1px solid rgba(230, 200, 255, 0.75) !important;
            border-radius: 12px !important;
        }}
        .stTextInput input::placeholder,
        .stTextArea textarea::placeholder {{
            color: rgba(242, 230, 255, 0.38) !important;
        }}

        /* Selectbox */
        div[data-baseweb="select"] > div {{
            background-color: rgba(25, 5, 42, 0.96) !important;
            color: #f2e6ff !important;
            border: 1px solid rgba(230, 200, 255, 0.75) !important;
            border-radius: 12px !important;
        }}
        div[data-baseweb="select"] span {{ color: #f2e6ff !important; }}
        div[data-baseweb="popover"] {{ z-index: 9999 !important; }}
        div[data-baseweb="popover"] ul {{ background-color: #14001f !important; }}
        div[data-baseweb="popover"] li {{ color: #f2e6ff !important; }}

        /* Кнопки */
        .stButton > button {{
            border-radius: 14px;
            border: 1px solid rgba(190, 120, 255, 0.45);
            background: rgba(50, 0, 75, 0.78);
            color: #f2e6ff !important;
            box-shadow: 0 0 14px rgba(140, 40, 200, 0.25);
            transition: all 0.25s ease;
        }}
        .stButton > button:hover {{
            border-color: rgba(130, 255, 70, 0.65);
            box-shadow: 0 0 18px rgba(110, 255, 50, 0.22);
            transform: translateY(-1px);
        }}

        /* Падающие символы */
        .white-spider {{
            position: fixed;
            top: -70px;
            z-index: 9;
            pointer-events: none;
            color: rgba(255, 255, 255, 0.92);
            text-shadow: 0 0 8px rgba(255,255,255,0.9), 0 0 14px rgba(190,120,255,0.55);
            animation-name: spiderFall;
            animation-timing-function: linear;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
        }}
        @keyframes spiderFall {{
            0%   {{ transform: translateY(-80px) rotate(0deg); opacity: 0; }}
            8%   {{ opacity: 1; }}
            85%  {{ opacity: 0.9; }}
            100% {{ transform: translateY(115vh) rotate(360deg); opacity: 0; }}
        }}

        .goth-symbol {{
            position: fixed;
            top: -70px;
            z-index: 9;
            pointer-events: none;
            color: rgba(235, 220, 255, 0.9);
            text-shadow: 0 0 8px rgba(180,80,255,0.8), 0 0 14px rgba(80,255,40,0.35);
            animation-name: gothicFall;
            animation-timing-function: linear;
            animation-iteration-count: 1;
            animation-fill-mode: forwards;
        }}
        @keyframes gothicFall {{
            0%   {{ transform: translateY(-80px) rotate(0deg); opacity: 0; }}
            10%  {{ opacity: 1; }}
            100% {{ transform: translateY(115vh) rotate(260deg); opacity: 0; }}
        }}

        /* Mobile */
        @media (max-width: 768px) {{
            [data-testid="stAppViewContainer"]::before {{
                height: 135px;
                background-size: 150vw auto;
                opacity: 0.62;
            }}
            .stApp .block-container,
            [data-testid="stMainBlockContainer"] {{
                margin-top: 85px !important;
                border-radius: 16px;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }}
            .white-spider, .goth-symbol {{ font-size: 18px !important; }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            [data-testid="stAppViewContainer"]::before,
            .white-spider, .goth-symbol {{ animation: none !important; }}
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )