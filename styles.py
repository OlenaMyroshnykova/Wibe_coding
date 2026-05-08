import base64
from pathlib import Path
import streamlit as st


def image_to_base64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode("utf-8")


def aplicar_estilos():
    slime_b64 = image_to_base64("assets/slime_transparent_2048x682.webp")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                radial-gradient(circle at top left, rgba(120, 0, 90, 0.35), transparent 35%),
                radial-gradient(circle at bottom right, rgba(70, 0, 120, 0.45), transparent 35%),
                linear-gradient(135deg, #07020d 0%, #16001f 50%, #050008 100%);
            color: #f2e6ff;
        }}

        .slime-background {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: clamp(150px, 28vw, 340px);
            z-index: 0;
            pointer-events: none;

            background-image: url("data:image/webp;base64,{slime_b64}");
            background-repeat: no-repeat;
            background-position: top center;
            background-size: 100% auto;

            opacity: 0.85;
            animation: slimeMove 12s ease-in-out infinite alternate;
            will-change: transform;
        }}

        @keyframes slimeMove {{
            from {{
                transform: translate3d(-8px, -4px, 0) scaleY(0.98);
            }}
            to {{
                transform: translate3d(8px, 8px, 0) scaleY(1.03);
            }}
        }}

        .stApp .block-container {{
            position: relative;
            z-index: 2;
            background: rgba(10, 0, 18, 0.78);
            border-radius: 24px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }}

        section[data-testid="stSidebar"] {{
            position: relative;
            z-index: 3;
            background: rgba(9, 0, 18, 0.92);
        }}

        @media (max-width: 768px) {{
            .slime-background {{
                height: 170px;
                background-size: 145% auto;
                opacity: 0.6;
            }}
        }}
        </style>

        <div class="slime-background"></div>
        """,
        unsafe_allow_html=True,
    )