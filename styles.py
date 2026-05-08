import streamlit as st


def aplicar_estilos():
    st.markdown(
        """
        <style>
        /* -------------------------------
           Fondo gótico principal
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
           Slime layer
        -------------------------------- */
        .slime-scene {
            position: fixed;
            inset: 0;
            pointer-events: none;
            overflow: hidden;
            z-index: 0;
        }

        .slime-wrapper {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 260px;
            filter: url("#gooey-slime");
            animation: slimeSway 7s ease-in-out infinite alternate;
        }

        /* Верхняя большая масса слизи */
        .slime-main {
            position: absolute;
            top: -18px;
            left: -3%;
            width: 106%;
            height: 95px;
            border-radius: 0 0 42% 38%;
            background:
                radial-gradient(circle at 12% 35%, rgba(255,255,255,0.85) 0 1.2%, transparent 3%),
                radial-gradient(circle at 38% 22%, rgba(255,255,255,0.65) 0 1%, transparent 3%),
                radial-gradient(circle at 65% 30%, rgba(255,255,255,0.75) 0 1.2%, transparent 3%),
                radial-gradient(circle at 89% 25%, rgba(255,255,255,0.6) 0 1%, transparent 3%),
                linear-gradient(180deg, #54ff1f 0%, #21cf0c 45%, #087b05 100%);
            box-shadow:
                inset 0 8px 12px rgba(210, 255, 180, 0.45),
                inset 0 -14px 24px rgba(0, 65, 0, 0.55),
                0 0 25px rgba(70, 255, 30, 0.35);
            opacity: 0.92;
        }

        /* Волнистая нижняя кромка */
        .slime-main::after {
            content: "";
            position: absolute;
            left: 0;
            bottom: -26px;
            width: 100%;
            height: 55px;
            background:
                radial-gradient(ellipse at 5% 0%, #23d90d 0 38%, transparent 40%),
                radial-gradient(ellipse at 14% 0%, #20c80c 0 34%, transparent 36%),
                radial-gradient(ellipse at 24% 0%, #28df10 0 42%, transparent 44%),
                radial-gradient(ellipse at 36% 0%, #1fc40b 0 36%, transparent 38%),
                radial-gradient(ellipse at 49% 0%, #2ee915 0 43%, transparent 45%),
                radial-gradient(ellipse at 63% 0%, #1fc90b 0 35%, transparent 37%),
                radial-gradient(ellipse at 76% 0%, #2be512 0 44%, transparent 46%),
                radial-gradient(ellipse at 90% 0%, #20c80c 0 37%, transparent 39%);
            filter: blur(0.4px);
        }

        /* Общий стиль потёков */
        .slime-drip {
            position: absolute;
            top: 42px;
            width: 38px;
            border-radius: 0 0 999px 999px;
            background:
                radial-gradient(circle at 40% 12%, rgba(255,255,255,0.65) 0 5%, transparent 13%),
                linear-gradient(90deg,
                    rgba(0, 85, 0, 0.45) 0%,
                    rgba(73, 255, 26, 0.95) 32%,
                    rgba(39, 210, 11, 1) 55%,
                    rgba(0, 90, 0, 0.6) 100%
                );
            box-shadow:
                inset 7px 0 10px rgba(170, 255, 130, 0.28),
                inset -8px 0 12px rgba(0, 55, 0, 0.45),
                0 0 16px rgba(70, 255, 30, 0.28);
            transform-origin: top center;
            animation-name: dripStretch;
            animation-timing-function: ease-in-out;
            animation-iteration-count: infinite;
            opacity: 0.95;
        }

        .slime-drip::after {
            content: "";
            position: absolute;
            left: 50%;
            bottom: -2px;
            transform: translateX(-50%);
            width: 48px;
            height: 38px;
            border-radius: 50%;
            background:
                radial-gradient(circle at 35% 25%, rgba(255,255,255,0.55) 0 8%, transparent 18%),
                linear-gradient(180deg, #4cff1f, #139b07);
            box-shadow:
                inset 5px 5px 9px rgba(220, 255, 190, 0.35),
                inset -8px -8px 12px rgba(0, 65, 0, 0.5);
        }

        /* Разные потёки, как на картинке */
        .drip-1 {
            left: 4%;
            height: 88px;
            width: 30px;
            animation-duration: 8s;
            animation-delay: -1s;
        }

        .drip-2 {
            left: 28%;
            height: 135px;
            width: 36px;
            animation-duration: 11s;
            animation-delay: -4s;
        }

        .drip-3 {
            left: 44%;
            height: 62px;
            width: 25px;
            animation-duration: 9s;
            animation-delay: -2s;
        }

        .drip-4 {
            left: 56%;
            height: 122px;
            width: 38px;
            animation-duration: 12s;
            animation-delay: -5s;
        }

        .drip-5 {
            left: 73%;
            height: 75px;
            width: 32px;
            animation-duration: 10s;
            animation-delay: -3s;
        }

        .drip-6 {
            left: 86%;
            height: 170px;
            width: 42px;
            animation-duration: 13s;
            animation-delay: -7s;
        }

        .drip-7 {
            left: 97%;
            height: 90px;
            width: 27px;
            animation-duration: 8.5s;
            animation-delay: -2.5s;
        }

        /* Дополнительные отдельные полосы слизи */
        .slime-strip {
            position: absolute;
            height: 52px;
            border-radius: 18px 18px 35px 35px;
            background:
                radial-gradient(circle at 18% 25%, rgba(255,255,255,0.6) 0 2%, transparent 5%),
                radial-gradient(circle at 72% 30%, rgba(255,255,255,0.5) 0 2%, transparent 5%),
                linear-gradient(180deg, #5aff22 0%, #20c80c 55%, #087004 100%);
            box-shadow:
                inset 0 7px 10px rgba(220,255,190,0.35),
                inset 0 -12px 18px rgba(0,70,0,0.55),
                0 0 18px rgba(70,255,30,0.25);
            opacity: 0.72;
            filter: url("#gooey-slime");
        }

        .strip-1 {
            top: 150px;
            left: 4%;
            width: 250px;
            animation: stripFloat 14s ease-in-out infinite alternate;
        }

        .strip-2 {
            top: 165px;
            left: 43%;
            width: 310px;
            animation: stripFloat 17s ease-in-out infinite alternate-reverse;
        }

        .strip-3 {
            top: 230px;
            right: 7%;
            width: 170px;
            animation: stripFloat 13s ease-in-out infinite alternate;
        }

        .strip-1::after,
        .strip-2::after,
        .strip-3::after {
            content: "";
            position: absolute;
            left: 12%;
            bottom: -36px;
            width: 28px;
            height: 60px;
            border-radius: 0 0 999px 999px;
            background: linear-gradient(180deg, #25d20d, #087004);
        }

        .strip-2::after {
            left: 55%;
            height: 92px;
            width: 35px;
        }

        .strip-3::after {
            left: 78%;
            height: 76px;
            width: 25px;
        }

        @keyframes dripStretch {
            0% {
                transform: scaleY(0.85) translateX(0);
            }
            50% {
                transform: scaleY(1.18) translateX(4px);
            }
            100% {
                transform: scaleY(0.92) translateX(-2px);
            }
        }

        @keyframes slimeSway {
            0% {
                transform: translateX(-8px);
            }
            100% {
                transform: translateX(8px);
            }
        }

        @keyframes stripFloat {
            0% {
                transform: translateY(0) translateX(0);
            }
            100% {
                transform: translateY(18px) translateX(10px);
            }
        }

        /* -------------------------------
           Контент поверх слизи
        -------------------------------- */
        .stApp .block-container {
            position: relative;
            z-index: 2;
            background: rgba(10, 0, 18, 0.72);
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

        <svg width="0" height="0">
            <defs>
                <filter id="gooey-slime">
                    <feGaussianBlur in="SourceGraphic" stdDeviation="7" result="blur" />
                    <feColorMatrix
                        in="blur"
                        mode="matrix"
                        values="
                            1 0 0 0 0
                            0 1 0 0 0
                            0 0 1 0 0
                            0 0 0 22 -9"
                        result="gooey"
                    />
                    <feComposite in="SourceGraphic" in2="gooey" operator="atop" />
                </filter>
            </defs>
        </svg>

        <div class="slime-scene">
            <div class="slime-wrapper">
                <div class="slime-main"></div>

                <div class="slime-drip drip-1"></div>
                <div class="slime-drip drip-2"></div>
                <div class="slime-drip drip-3"></div>
                <div class="slime-drip drip-4"></div>
                <div class="slime-drip drip-5"></div>
                <div class="slime-drip drip-6"></div>
                <div class="slime-drip drip-7"></div>
            </div>

            <div class="slime-strip strip-1"></div>
            <div class="slime-strip strip-2"></div>
            <div class="slime-strip strip-3"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )