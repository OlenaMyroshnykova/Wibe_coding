import streamlit as st
from config import HUMOR_OPTIONS


# -------------------------------
# Mostrar formulario lateral
# -------------------------------
def mostrar_formulario():
    with st.sidebar:
        st.header("🖤 Tu Registro")

        nombre = st.text_input("Nombre", placeholder="Ej. Morticia")

        humor = st.selectbox(
            "Estado del alma",
            HUMOR_OPTIONS,
        )

        energia = st.slider("Nivel de energía vital (%)", 0, 100, 50)

        boton_registrar = st.button("Registrar mi Vibe 🕯️")

    return nombre, humor, energia, boton_registrar


# -------------------------------
# Mostrar métricas principales
# -------------------------------
def mostrar_metricas(df):
    promedio = df["Energia"].mean()

    col1, col2 = st.columns(2)

    col1.metric("Energía Vital Promedio", f"{int(promedio)}%")
    col2.metric("Registros en el Grimorio", len(df))

    return promedio


# -------------------------------
# Mostrar mensaje según energía media
# -------------------------------
def mostrar_mensaje_energia(promedio):
    if promedio > 80:
        st.success(
            f"🌙 La noche favorece al equipo. Energía promedio: {promedio:.1f}%. "
            "La productividad despierta."
        )
    elif promedio < 40:
        st.error(
            f"☕ Energía crítica: {promedio:.1f}%. "
            "Se recomienda café oscuro y pausa ritual de 15 minutos."
        )
    else:
        st.info(
            f"🕯️ Energía estable: {promedio:.1f}%. "
            "El equipo avanza entre sombras con buen ritmo."
        )


# -------------------------------
# Mostrar lista minimalista de registros
# -------------------------------
def mostrar_registros(df, eliminar_callback):
    st.subheader("📜 Registros guardados")

    for indice, fila in df.iterrows():
        col_nombre, col_humor, col_energia, col_boton = st.columns([3, 4, 2, 1])

        with col_nombre:
            st.markdown(
                f'<div class="record-name">🖤 {fila["Nombre"]}</div>',
                unsafe_allow_html=True,
            )

        with col_humor:
            st.markdown(
                f'<div class="record-text">{fila["Humor"]}</div>',
                unsafe_allow_html=True,
            )

        with col_energia:
            st.markdown(
                f'<div class="record-energy">⚡ {fila["Energia"]}%</div>',
                unsafe_allow_html=True,
            )

        with col_boton:
            if st.button("Eliminar", key=f"delete_{indice}"):
                eliminar_callback(indice)

        st.markdown('<div class="record-separator"></div>', unsafe_allow_html=True)


# -------------------------------
# Mostrar tabla completa en desplegable
# -------------------------------
def mostrar_tabla_completa(df):
    with st.expander("🕯️ Ver tabla completa del grimorio"):
        st.dataframe(df, use_container_width=True)


# -------------------------------
# Mostrar botón para borrar todo
# -------------------------------
def mostrar_boton_borrar_todo():
    st.markdown('<div class="goth-divider"></div>', unsafe_allow_html=True)

    return st.button("🗑️ Borrar todo el grimorio")