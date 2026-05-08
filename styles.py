import streamlit as st


# -------------------------------
# Aplicar estilos CSS de la aplicación
# -------------------------------
def aplicar_estilos():
    st.markdown(
        """
        <style>
        /* Fondo principal gótico */
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(120, 0, 60, 0.35), transparent 35%),
                radial-gradient(circle at bottom right, rgba(40, 0, 80, 0.45), transparent 35%),
                linear-gradient(135deg, #07020d 0%, #130015 45%, #050008 100%);
            color: #f2e6ff;
            overflow: hidden;
        }

        /* Capa de slime verde que baja lentamente */
        .stApp::before {
            content: "";
            position: fixed;
            top: -120%;
            left: 0;
            width: 100%;
            height: 220%;
            pointer-events: none;
            z-index: 0;

            background:
                radial-gradient(circle at 8% 12%, rgba(72, 255, 0, 0.55) 0 2%, transparent 6%),
                radial-gradient(circle at 20% 5%, rgba(120, 255, 40, 0.45) 0 3%, transparent 8%),
                radial-gradient(circle at 35% 15%, rgba(60, 255, 0, 0.40) 0 2%, transparent 7%),
                radial-gradient(circle at 52% 8%, rgba(150, 255, 30, 0.50) 0 3%, transparent 9%),
                radial-gradient(circle at 68% 14%, rgba(70, 255, 0, 0.45) 0 2%, transparent 7%),
                radial-gradient(circle at 84% 7%, rgba(130, 255, 40, 0.55) 0 3%, transparent 8%),
                radial-gradient(circle at 95% 18%, rgba(80, 255, 0, 0.45) 0 2%, transparent 7%),

                linear-gradient(
                    180deg,
                    transparent 0%,
                    rgba(77, 255, 0, 0.12) 18%,
                    rgba(77, 255, 0, 0.05) 32%,
                    transparent 55%
                );

            filter: blur(1px);
            opacity: 0.75;
            animation: greenSlimeFall 18s linear infinite;
        }

        /* Segunda capa: gotas más largas */
        .stApp::after {
            content: "";
            position: fixed;
            top: -100%;
            left: 0;
            width: 100%;
            height: 200%;
            pointer-events: none;
            z-index: 0;

            background:
                linear-gradient(180deg, rgba(100, 255, 20, 0.45), transparent 45%) 10% 0 / 8px 180px,
                linear-gradient(180deg, rgba(80, 255, 0, 0.35), transparent 50%) 28% 0 / 6px 240px,
                linear-gradient(180deg, rgba(150, 255, 30, 0.40), transparent 50%) 47% 0 / 10px 210px,
                linear-gradient(180deg, rgba(90, 255, 0, 0.35), transparent 55%) 66% 0 / 7px 260px,
                linear-gradient(180deg, rgba(130, 255, 20, 0.45), transparent 50%) 88% 0 / 9px 200px;

            background-repeat: repeat-y;
            opacity: 0.55;
            filter: blur(0.5px);
            animation: greenSlimeDrops 25s linear infinite;
        }

        @keyframes greenSlimeFall {
            0% {
                transform: translateY(-20%);
            }
            100% {
                transform: translateY(55%);
            }
        }

        @keyframes greenSlimeDrops {
            0% {
                transform: translateY(-25%);
            }
            100% {
                transform: translateY(65%);
            }
        }

        /* Чтобы контент был поверх слизи */
        .stApp > header,
        .stApp [data-testid="stToolbar"],
        .stApp [data-testid="stSidebar"],
        .stApp .block-container {
            position: relative;
            z-index: 2;
        }

        /* Header Streamlit */
        header[data-testid="stHeader"] {
            background: rgba(7, 2, 13, 0.65) !important;
            backdrop-filter: blur(4px);
        }

        /* Основной контейнер */
        .block-container {
            background: rgba(10, 0, 18, 0.58);
            border-radius: 22px;
            padding-top: 2rem;
            box-shadow: 0 0 35px rgba(120, 0, 160, 0.25);
        }

        h1, h2, h3 {
            color: #e9d5ff;
            text-shadow: 0 0 12px rgba(170, 60, 255, 0.8);
        }

        p, label, span, div {
            color: #f2e6ff;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )