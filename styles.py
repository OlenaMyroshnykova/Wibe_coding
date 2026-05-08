import streamlit as st


def aplicar_estilos():
    st.markdown(
        """
        <style>
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

        .slime-layer {
            position: fixed;
            inset: 0;
            z-index: 0;
            pointer-events: none;
            overflow: hidden;
        }

        .slime-svg {
            position: absolute;
            top: 0;
            left: 0;
            width: 100vw;
            height: 310px;
            animation: slimeMove 8s ease-in-out infinite alternate;
        }

        .slime-strip {
            animation: slimeBreath 6s ease-in-out infinite alternate;
            transform-origin: top center;
        }

        .drip-a {
            animation: dripA 7s ease-in-out infinite alternate;
            transform-origin: top center;
        }

        .drip-b {
            animation: dripB 9s ease-in-out infinite alternate;
            transform-origin: top center;
        }

        .drip-c {
            animation: dripC 8s ease-in-out infinite alternate;
            transform-origin: top center;
        }

        @keyframes slimeMove {
            from {
                transform: translateX(-8px);
            }
            to {
                transform: translateX(8px);
            }
        }

        @keyframes slimeBreath {
            from {
                transform: scaleY(0.98);
            }
            to {
                transform: scaleY(1.04);
            }
        }

        @keyframes dripA {
            from {
                transform: scaleY(0.92);
            }
            to {
                transform: scaleY(1.18);
            }
        }

        @keyframes dripB {
            from {
                transform: scaleY(1.05);
            }
            to {
                transform: scaleY(0.88);
            }
        }

        @keyframes dripC {
            from {
                transform: scaleY(0.96);
            }
            to {
                transform: scaleY(1.25);
            }
        }

        .stApp .block-container {
            position: relative;
            z-index: 2;
            background: rgba(10, 0, 18, 0.74);
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

        <div class="slime-layer">
            <svg class="slime-svg" viewBox="0 0 1200 310" preserveAspectRatio="none">
                <defs>
                    <linearGradient id="slimeGradient" x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stop-color="#75ff35"/>
                        <stop offset="38%" stop-color="#26df0d"/>
                        <stop offset="100%" stop-color="#056800"/>
                    </linearGradient>

                    <linearGradient id="slimeDark" x1="0" y1="0" x2="1" y2="1">
                        <stop offset="0%" stop-color="#66ff30"/>
                        <stop offset="55%" stop-color="#16b807"/>
                        <stop offset="100%" stop-color="#034900"/>
                    </linearGradient>

                    <filter id="slimeShadow">
                        <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#001900" flood-opacity="0.65"/>
                    </filter>

                    <filter id="softGlow">
                        <feGaussianBlur stdDeviation="2.5" result="blur"/>
                        <feMerge>
                            <feMergeNode in="blur"/>
                            <feMergeNode in="SourceGraphic"/>
                        </feMerge>
                    </filter>
                </defs>

                <!-- Основная верхняя масса -->
                <path class="slime-strip"
                    d="
                    M 0 0
                    H 1200
                    V 62

                    C 1180 58, 1168 75, 1160 98
                    C 1152 125, 1135 122, 1130 96
                    C 1124 64, 1094 64, 1065 78

                    C 1038 91, 1008 89, 982 76
                    C 960 65, 928 65, 918 92
                    C 906 124, 878 121, 870 91
                    C 862 63, 835 59, 810 73

                    C 780 91, 744 91, 720 70
                    C 700 53, 670 58, 662 83
                    C 655 105, 633 105, 628 81
                    C 622 50, 580 50, 560 73

                    C 538 99, 506 99, 482 75
                    C 460 54, 430 58, 424 90
                    C 417 126, 390 127, 382 91
                    C 375 60, 345 58, 320 76

                    C 292 96, 255 96, 230 78
                    C 207 61, 178 63, 166 91
                    C 154 120, 126 121, 116 91
                    C 104 55, 62 63, 48 90
                    C 37 113, 17 116, 12 88

                    C 7 66, 0 62, 0 62
                    Z"
                    fill="url(#slimeGradient)"
                    filter="url(#slimeShadow)"
                    opacity="0.92"
                />

                <!-- Длинные потёки, они теперь НЕ круглые -->
                <path class="drip-a"
                    d="M 370 70 C 395 65, 418 72, 412 110 C 407 144, 412 178, 390 188 C 366 177, 375 143, 366 110 C 358 87, 355 76, 370 70 Z"
                    fill="url(#slimeDark)"
                    filter="url(#slimeShadow)"
                    opacity="0.94"
                />

                <path class="drip-b"
                    d="M 665 72 C 690 70, 710 78, 706 112 C 701 154, 708 206, 682 221 C 653 205, 665 157, 656 115 C 651 92, 649 78, 665 72 Z"
                    fill="url(#slimeDark)"
                    filter="url(#slimeShadow)"
                    opacity="0.94"
                />

                <path class="drip-c"
                    d="M 1015 77 C 1044 69, 1070 82, 1064 124 C 1058 171, 1063 232, 1034 250 C 1003 230, 1016 174, 1006 126 C 1000 99, 999 83, 1015 77 Z"
                    fill="url(#slimeDark)"
                    filter="url(#slimeShadow)"
                    opacity="0.94"
                />

                <path class="drip-a"
                    d="M 60 78 C 82 72, 101 80, 96 112 C 91 143, 94 169, 75 181 C 52 168, 61 143, 55 113 C 50 92, 47 82, 60 78 Z"
                    fill="url(#slimeDark)"
                    filter="url(#slimeShadow)"
                    opacity="0.9"
                />

                <path class="drip-b"
                    d="M 1160 64 C 1184 59, 1204 70, 1196 102 C 1191 126, 1192 151, 1174 162 C 1152 148, 1161 126, 1154 102 C 1148 80, 1148 68, 1160 64 Z"
                    fill="url(#slimeDark)"
                    filter="url(#slimeShadow)"
                    opacity="0.9"
                />

                <!-- Блики -->
                <path d="M 40 32 C 90 22, 145 24, 196 30" stroke="rgba(255,255,255,0.42)" stroke-width="5" stroke-linecap="round" fill="none" filter="url(#softGlow)" />
                <path d="M 520 36 C 555 25, 600 25, 636 33" stroke="rgba(255,255,255,0.38)" stroke-width="5" stroke-linecap="round" fill="none" filter="url(#softGlow)" />
                <path d="M 930 35 C 970 25, 1010 26, 1050 34" stroke="rgba(255,255,255,0.36)" stroke-width="5" stroke-linecap="round" fill="none" filter="url(#softGlow)" />

                <!-- Нижние отдельные куски, как на референсе -->
                <g opacity="0.62">
                    <path
                        d="M 55 185 H 360 C 350 215, 315 205, 298 222 C 276 244, 245 236, 235 207 C 220 218, 198 217, 184 200 C 160 213, 126 210, 112 190 C 92 199, 70 197, 55 185 Z"
                        fill="url(#slimeGradient)"
                        filter="url(#slimeShadow)"
                    />

                    <path
                        d="M 510 195 H 760 C 748 226, 714 214, 696 235 C 676 258, 642 248, 632 218 C 606 225, 577 218, 566 199 C 544 205, 524 204, 510 195 Z"
                        fill="url(#slimeGradient)"
                        filter="url(#slimeShadow)"
                    />

                    <path
                        d="M 905 205 H 1130 C 1118 233, 1092 230, 1078 248 C 1056 276, 1018 264, 1010 232 C 986 239, 954 229, 944 209 C 928 214, 915 212, 905 205 Z"
                        fill="url(#slimeGradient)"
                        filter="url(#slimeShadow)"
                    />
                </g>
            </svg>
        </div>
        """,
        unsafe_allow_html=True,
    )