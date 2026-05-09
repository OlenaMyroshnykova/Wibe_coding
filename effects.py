import random

import streamlit as st


# -------------------------------
# Efecto visual personalizado: lluvia gótica
# Se lanza cuando la energía media del equipo es baja
# -------------------------------
def gothic_rain():
    symbols = ["💔", "💔", "🩸", "🩸", "🥀", "🕷️", "🕸️", "🦇"]

    elements = ""

    for _ in range(28):
        symbol = random.choice(symbols)
        left = random.randint(0, 95)
        size = random.randint(22, 38)
        duration = random.uniform(3.0, 6.0)
        delay = random.uniform(0, 1.8)

        elements += f"""
        <span
            class="goth-symbol"
            style="
                left: {left}vw;
                font-size: {size}px;
                animation-duration: {duration}s;
                animation-delay: {delay}s;
            "
        >
            {symbol}
        </span>
        """

    st.markdown(elements, unsafe_allow_html=True)


# -------------------------------
# Efecto visual: arañas blancas al cargar la página
# -------------------------------
def spider_rain():
    spiders = ["🕷️"]

    elements = ""

    for _ in range(14):
        spider = random.choice(spiders)
        left = random.randint(0, 95)
        size = random.randint(22, 36)
        duration = random.uniform(3.0, 5.8)
        delay = random.uniform(0, 1.6)

        elements += f"""
        <span
            class="white-spider"
            style="
                left: {left}vw;
                font-size: {size}px;
                animation-duration: {duration}s;
                animation-delay: {delay}s;
            "
        >
            {spider}
        </span>
        """

    st.markdown(elements, unsafe_allow_html=True)


# -------------------------------
# Efecto ambiental constante:
# corazones rotos y gotas de sangre
# -------------------------------
def ambient_dark_rain():
    symbols = ["💔", "🩸"]

    elements = ""

    for _ in range(20):
        symbol = random.choice(symbols)
        left = random.randint(0, 95)
        size = random.randint(18, 32)

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

        elements += f"""
        <span
            class="{css_class} {direction}"
            style="
                left: {left}vw;
                font-size: {size}px;
                animation-duration: {duration}s;
                animation-delay: {delay}s;
            "
        >
            {symbol}
        </span>
        """

    st.markdown(elements, unsafe_allow_html=True)


# -------------------------------
# Decidir qué efecto mostrar según la energía media
# -------------------------------
def lanzar_efecto_segun_energia(df):
    if df.empty:
        st.session_state.efecto_pendiente = "gothic"
        return

    promedio = df["Energia"].mean()

    if promedio >= 40:
        st.session_state.efecto_pendiente = "balloons"
    else:
        st.session_state.efecto_pendiente = "gothic"


# -------------------------------
# Mostrar el efecto pendiente
# -------------------------------
def mostrar_efecto_pendiente():
    efecto = st.session_state.get("efecto_pendiente")

    if efecto == "balloons":
        st.balloons()

    elif efecto == "gothic":
        gothic_rain()

    st.session_state.efecto_pendiente = None