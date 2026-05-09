import random

import streamlit as st


def gothic_rain():
    symbols = ["☕", "☕", "☕", "🧋", "🍵"]

    elements = ""

    for _ in range(20):
        symbol = random.choice(symbols)
        left = random.randint(0, 95)
        size = random.randint(22, 36)
        duration = random.uniform(3.0, 5.8)
        delay = random.uniform(0, 1.5)

        elements += (
            f'<span class="goth-symbol" '
            f'style="left:{left}vw; font-size:{size}px; '
            f'animation-duration:{duration}s; animation-delay:{delay}s;">'
            f'{symbol}</span>'
        )

    st.markdown(elements, unsafe_allow_html=True)


def spider_rain():
    spiders = ["🕷️", "🕸️"]

    elements = ""

    for _ in range(35):
        spider = random.choice(spiders)
        left = random.randint(0, 95)
        size = random.randint(22, 36)
        duration = random.uniform(3.0, 5.8)
        delay = random.uniform(0, 1.6)

        elements += (
            f'<span class="white-spider" '
            f'style="left:{left}vw; '
            f'font-size:{size}px; '
            f'animation-duration:{duration}s; '
            f'animation-delay:{delay}s;">'
            f'{spider}</span>'
        )

    st.markdown(elements, unsafe_allow_html=True)

def ambient_dark_rain():
    symbols = ["💔", "🩸"]

    elements = ""

    for _ in range(16):
        symbol = random.choice(symbols)
        left = random.randint(0, 95)
        size = random.randint(18, 30)

        if symbol == "💔":
            css_class = "ambient-heart"
            direction = random.choice(["left", "right"])
            duration = random.uniform(13, 24)
            delay = random.uniform(0, 38)
        else:
            css_class = "ambient-blood"
            direction = "down"
            duration = random.uniform(9, 18)
            delay = random.uniform(0, 38)

        elements += (
            f'<span class="{css_class} {direction}" '
            f'style="left:{left}vw; font-size:{size}px; '
            f'animation-duration:{duration}s; animation-delay:{delay}s;">'
            f'{symbol}</span>'
        )

    st.markdown(elements, unsafe_allow_html=True)


def lanzar_efecto_segun_energia(df):
    if df.empty:
        st.session_state.efecto_pendiente = "gothic"
        return

    promedio = df["Energia"].mean()

    if promedio >= 40:
        st.session_state.efecto_pendiente = "balloons"
    else:
        st.session_state.efecto_pendiente = "gothic"


def mostrar_efecto_pendiente():
    efecto = st.session_state.get("efecto_pendiente")

    if efecto == "balloons":
        st.balloons()

    elif efecto == "gothic":
        gothic_rain()

    st.session_state.efecto_pendiente = None