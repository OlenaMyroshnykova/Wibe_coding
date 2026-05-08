import base64
from pathlib import Path

import streamlit as st


def image_to_base64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode("utf-8")


def aplicar_estilos():
    slime_b64 = image_to_base64("assets/slime_top_clean_2048x370.webp")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                radial-gradient(circle at top left, rgba(140, 0, 110, 0.35), transparent 34%),
                radial-gradient(circle at bottom right, rgba(70, 0, 130, 0.45), transparent 36%),
                linear-gradient(135deg, #07020d 0%, #16001f 50%, #050008 100%);
            color: #f2e6ff;
        }}

        header[data-testid="stHeader"] {{
            background: rgba(7, 2, 13, 0.85) !important;
        }}

        .slime-background {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: clamp(95px, 18vw, 230px);
            z-index: 0;
            pointer-events: none;

            background-image: url("data:image/webp;base64,{slime_b64}");
            background-repeat: no-repeat;
            background-position: top center;
            background-size: 100% auto;

            opacity: 0.78;
            animation: slimeMove 14s ease-in-out infinite alternate;
            will-change: transform;
        }}

        @keyframes slimeMove {{
            from {{
                transform: translate3d(-6px, -8px, 0) scaleY(0.96);
            }}
            to {{
                transform: translate3d(6px, 2px, 0) scaleY(1.02);
            }}
        }}

        .stApp .block-container {{
            position: relative;
            z-index: 2;
            margin-top: 120px;
            background: rgba(10, 0, 18, 0.82);
            border-radius: 24px;
            padding-top: 2rem;
            padding-bottom: 2rem;
            box-shadow: 0 0 35px rgba(120, 0, 160, 0.25);
        }}

        section[data-testid="stSidebar"] {{
            position: relative;
            z-index: 3;
            background: rgba(9, 0, 18, 0.94);
        }}

        h1, h2, h3 {{
            color: #e9d5ff;
            text-shadow: 0 0 12px rgba(170, 60, 255, 0.75);
        }}

        p, label, span, div {{
            color: #f2e6ff;
        }}

        .stButton > button {{
            border-radius: 14px;
            border: 1px solid rgba(190, 120, 255, 0.45);
            background: rgba(50, 0, 75, 0.78);
            color: #f2e6ff;
            box-shadow: 0 0 14px rgba(140, 40, 200, 0.25);
        }}

        .stButton > button:hover {{
            border-color: rgba(130, 255, 70, 0.65);
            box-shadow: 0 0 18px rgba(110, 255, 50, 0.22);
        }}

        @media (max-width: 768px) {{
            .slime-background {{
                height: 120px;
                background-size: 150% auto;
                opacity: 0.58;
            }}

            .stApp .block-container {{
                margin-top: 80px;
                border-radius: 16px;
                background: rgba(10, 0, 18, 0.88);
            }}
        }}

        @media (prefers-reduced-motion: reduce) {{
            .slime-background {{
                animation: none;
            }}
        }}
        </style>

        <div class="slime-background"></div>
        """,
        unsafe_allow_html=True,
    )