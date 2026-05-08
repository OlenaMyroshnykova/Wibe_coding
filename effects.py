import random
import streamlit as st


# -------------------------------
# Efecto visual personalizado: lluvia gótica
# -------------------------------
def gothic_rain():
    symbols = ["🦇", "🕯️", "🌙", "🖤", "🥀", "☕"]
    elements = ""

    for _ in range(45):
        symbol = random.choice(symbols)
        left = random.randint(0, 95)
        size = random.randint(24, 44)
        duration = random.uniform(2.0, 4.2)
        delay = random.uniform(0, 1.2)

        elements += f"""
        <span class="goth-symbol"
              style="
                  left: {left}vw;
                  font-size: {size}px;
                  animation-duration: {duration}s;
                  animation-delay: {delay}s;
              ">
            {symbol}
        </span>
        """

    st.markdown(elements, unsafe_allow_html=True)


# -------------------------------
# Efecto visual: lluvia de arañas blancas al cargar la página
# -------------------------------
def spider_rain():
    spiders = ["🕷️", "🕸️"]
    elements = ""

    for _ in range(35):
        spider = random.choice(spiders)
        left = random.randint(0, 95)
        size = random.randint(22, 38)
        duration = random.uniform(3.0, 5.5)
        delay = random.uniform(0, 1.5)

        elements += f"""
        <span class="white-spider"
              style="
                  left: {left}vw;
                  font-size: {size}px;
                  animation-duration: {duration}s;
                  animation-delay: {delay}s;
              ">
            {spider}
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