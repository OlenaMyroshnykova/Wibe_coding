import streamlit as st


# -------------------------------
# Aplicar estilos CSS de la aplicación
# -------------------------------
def aplicar_estilos():
    st.markdown(
        """
        <style>
        /* -------------------------------
           Fondo principal
        -------------------------------- */
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(120, 0, 90, 0.35), transparent 35%),
                radial-gradient(circle at bottom right, rgba(70, 0, 120, 0.45), transparent 35%),
                linear-gradient(135deg, #07020d 0%, #16001f 50%, #050008 100%);
            color: #f2e6ff;
        }

        header[data-testid="stHeader"] {
            background: rgba(7, 2, 13, 0.75) !important;
        }

        /* -------------------------------
           Capa de slime: detrás del contenido
        -------------------------------- */
        .slime-background {
            position: fixed;
            inset: 0;
            overflow: hidden;
            pointer-events: none;
            z-index: 0;
        }

        /* Mancha superior de donde cae la slime */
        .slime-top {
            position: absolute;
            top: -40px;
            left: 0;
            width: 100%;
            height: 85px;
            background:
                radial-gradient(circle at 8% 70%, rgba(93, 255, 38, 0.45), transparent 8%),
                radial-gradient(circle at 22% 50%, rgba(113, 255, 47, 0.35), transparent 7%),
                radial-gradient(circle at 41% 75%, rgba(76, 255, 20, 0.40), transparent 9%),
                radial-gradient(circle at 63% 60%, rgba(127, 255, 60, 0.35), transparent 8%),
                radial-gradient(circle at 82% 72%, rgba(91, 255, 30, 0.45), transparent 9%),
                linear-gradient(
                    180deg,
                    rgba(88, 255, 30, 0.42),
                    rgba(45, 150, 20, 0.18),
                    transparent
                );
            filter: blur(1px);
            opacity: 0.65;
        }

        /* Cada gota */
        .slime-drop {
            position: absolute;
            top: -420px;
            width: 14px;
            height: 320px;
            border-radius: 999px;
            background:
                linear-gradient(
                    180deg,
                    rgba(130, 255, 70, 0.00) 0%,
                    rgba(130, 255, 70, 0.45) 18%,
                    rgba(72, 220, 25, 0.30) 62%,
                    rgba(72, 220, 25, 0.00) 100%
                );
            filter: blur(0.3px);
            opacity: 0.32;
            animation-name: slimeFall;
            animation-timing-function: linear;
            animation-iteration-count: infinite;
        }

        .slime-drop::after {
            content: "";
            position: absolute;
            bottom: 52px;
            left: 50%;
            transform: translateX(-50%);
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: rgba(130, 255, 70, 0.42);
            box-shadow: 0 0 18px rgba(100, 255, 40, 0.28);
        }

        .drop-1 {
            left: 7%;
            height: 280px;
            animation-duration: 24s;
            animation-delay: -6s;
        }

        .drop-2 {
            left: 18%;
            height: 420px;
            width: 10px;
            animation-duration: 31s;
            animation-delay: -18s;
            opacity: 0.24;
        }

        .drop-3 {
            left: 31%;
            height: 340px;
            width: 16px;
            animation-duration: 27s;
            animation-delay: -12s;
        }

        .drop-4 {
            left: 47%;
            height: 390px;
            width: 12px;
            animation-duration: 34s;
            animation-delay: -22s;
            opacity: 0.26;
        }

        .drop-5 {
            left: 61%;
            height: 300px;
            width: 18px;
            animation-duration: 26s;
            animation-delay: -10s;
        }

        .drop-6 {
            left: 74%;
            height: 450px;
            width: 11px;
            animation-duration: 36s;
            animation-delay: -25s;
            opacity: 0.22;
        }

        .drop-7 {
            left: 89%;
            height: 330px;
            width: 15px;
            animation-duration: 29s;
            animation-delay: -15s;
        }

        @keyframes slimeFall {
            0% {
                transform: translateY(-35vh);
            }

            100% {
                transform: translateY(145vh);
            }
        }

        /* -------------------------------
           Контент поверх анимации
        -------------------------------- */
        .stApp .block-container {
            position: relative;
            z-index: 2;
            background: rgba(10, 0, 18, 0.62);
            border-radius: 24px;
            padding-top: 2rem;
            padding-bottom: 2rem;
            box-shadow: 0 0 35px rgba(120, 0, 160, 0.25);
        }

        section[data-testid="stSidebar"] {
            position: relative;
            z-index: 3;
            background: rgba(9, 0, 18, 0.92);
        }

        h1, h2, h3 {
            color: #e9d5ff;
            text-shadow: 0 0 12px rgba(170, 60, 255, 0.75);
        }

        p, label, span, div {
            color: #f2e6ff;
        }

        /* Кнопки */
        .stButton > button {
            border-radius: 14px;
            border: 1px solid rgba(190, 120, 255, 0.45);
            background: rgba(50, 0, 75, 0.75);
            color: #f2e6ff;
            box-shadow: 0 0 14px rgba(140, 40, 200, 0.25);
        }

        .stButton > button:hover {
            border-color: rgba(130, 255, 70, 0.65);
            box-shadow: 0 0 18px rgba(110, 255, 50, 0.22);
        }
        </style>

        <div class="slime-background">
            <div class="slime-top"></div>
            <div class="slime-drop drop-1"></div>
            <div class="slime-drop drop-2"></div>
            <div class="slime-drop drop-3"></div>
            <div class="slime-drop drop-4"></div>
            <div class="slime-drop drop-5"></div>
            <div class="slime-drop drop-6"></div>
            <div class="slime-drop drop-7"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )