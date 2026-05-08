import os
import random
import streamlit as st
import pandas as pd

# -------------------------------
# Configuración de la página
# -------------------------------
st.set_page_config(page_title="Team Vibe", page_icon="🌈")

# Archivo donde se guardan los datos
DATA_FILE = "historial_vibe.csv"


# -------------------------------
# Funciones para guardar y cargar datos
# -------------------------------
def cargar_datos():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)

        columnas_necesarias = ["Nombre", "Humor", "Energia"]
        for columna in columnas_necesarias:
            if columna not in df.columns:
                df[columna] = ""

        return df[columnas_necesarias]

    return pd.DataFrame(columns=["Nombre", "Humor", "Energia"])


def guardar_datos(df):
    df.to_csv(DATA_FILE, index=False)


# -------------------------------
# Efecto personalizado: lluvia de cafés
# -------------------------------
def coffee_rain():
    coffees = ["☕", "☕", "☕", "🧋", "🍵"]
    coffee_elements = ""

    for i in range(45):
        coffee = random.choice(coffees)
        left = random.randint(0, 95)
        size = random.randint(24, 42)
        duration = random.uniform(2.0, 4.0)
        delay = random.uniform(0, 1.2)

        coffee_elements += f"""
        <span class="coffee"
              style="
                  left: {left}vw;
                  font-size: {size}px;
                  animation-duration: {duration}s;
                  animation-delay: {delay}s;
              ">
            {coffee}
        </span>
        """

    st.markdown(
        f"""
        <style>
        .coffee {{
            position: fixed;
            top: -60px;
            z-index: 999999;
            pointer-events: none;
            animation-name: coffee-fall;
            animation-timing-function: linear;
            animation-fill-mode: forwards;
        }}

        @keyframes coffee-fall {{
            0% {{
                transform: translateY(0) rotate(0deg);
                opacity: 1;
            }}
            80% {{
                opacity: 1;
            }}
            100% {{
                transform: translateY(110vh) rotate(360deg);
                opacity: 0;
            }}
        }}
        </style>

        <div class="coffee-rain">
            {coffee_elements}
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------
# Elegir efecto según energía media
# -------------------------------
def lanzar_efecto_segun_energia(df):
    if df.empty:
        st.session_state.efecto_pendiente = "coffee"
        return

    promedio = df["Energia"].mean()

    if promedio >= 40:
        st.session_state.efecto_pendiente = "balloons"
    else:
        st.session_state.efecto_pendiente = "coffee"


def mostrar_efecto_pendiente():
    efecto = st.session_state.get("efecto_pendiente")

    if efecto == "balloons":
        st.balloons()
    elif efecto == "coffee":
        coffee_rain()

    st.session_state.efecto_pendiente = None


# -------------------------------
# Eliminar un registro
# -------------------------------
def eliminar_registro(indice):
    st.session_state.historial_vibe = st.session_state.historial_vibe.drop(
        index=indice
    ).reset_index(drop=True)

    guardar_datos(st.session_state.historial_vibe)

    lanzar_efecto_segun_energia(st.session_state.historial_vibe)

    st.rerun()


# -------------------------------
# Cargar datos al iniciar la app
# -------------------------------
if "historial_vibe" not in st.session_state:
    st.session_state.historial_vibe = cargar_datos()

if "efecto_pendiente" not in st.session_state:
    st.session_state.efecto_pendiente = None


# -------------------------------
# Título principal
# -------------------------------
st.title("🌈 Team Vibe Dashboard")
st.markdown("### ¿Cómo está el pulso del equipo hoy?")

# Mostrar efecto después de añadir, eliminar o borrar datos
mostrar_efecto_pendiente()


# -------------------------------
# Sidebar / Formulario de registro
# -------------------------------
with st.sidebar:
    st.header("Tu Registro")

    nombre = st.text_input("Tu nombre", placeholder="Ej. Ana")

    humor = st.selectbox(
        "Humor",
        [
            "🤩 Increíble",
            "😴 Sueño",
            "☕ Café urgente",
            "🤯 Al límite",
        ],
    )

    energia = st.slider("Nivel de batería (%)", 0, 100, 50)

    boton_registrar = st.button("Registrar mi Vibe 🚀")


# -------------------------------
# Procesamiento del registro
# -------------------------------
if boton_registrar:
    if nombre.strip() == "":
        st.warning("Por favor, escribe tu nombre antes de registrar.")
    else:
        nuevo_registro = pd.DataFrame(
            [
                {
                    "Nombre": nombre.strip(),
                    "Humor": humor,
                    "Energia": energia,
                }
            ]
        )

        st.session_state.historial_vibe = pd.concat(
            [st.session_state.historial_vibe, nuevo_registro],
            ignore_index=True,
        )

        guardar_datos(st.session_state.historial_vibe)

        lanzar_efecto_segun_energia(st.session_state.historial_vibe)

        st.success("Registro guardado correctamente ☕")

        st.rerun()


# -------------------------------
# Visualización de datos
# -------------------------------
df = st.session_state.historial_vibe

if not df.empty:
    promedio = df["Energia"].mean()

    col1, col2 = st.columns(2)

    col1.metric("Energía Promedio", f"{int(promedio)}%")
    col2.metric("Registros Totales", len(df))

    if promedio > 80:
        st.success(
            f"💥 ¡Vibe Altísima! El promedio es {promedio:.1f}%. "
            "¡A comerse el mundo!"
        )
    elif promedio < 40:
        st.error(
            f"🪫 Batería baja ({promedio:.1f}%). "
            "Es hora de un break de 15 min."
        )
    else:
        st.info(
            f"⚖️ Vibe estable en {promedio:.1f}%. "
            "¡Buen ritmo, equipo!"
        )

    st.subheader("Historial de Energía")
    st.bar_chart(df.set_index("Nombre")["Energia"])

    # -------------------------------
    # Historial con eliminación individual
    # -------------------------------
    st.subheader("Registros guardados")

    for indice, fila in df.iterrows():
        col_nombre, col_humor, col_energia, col_boton = st.columns([3, 3, 2, 2])

        col_nombre.write(f"**{fila['Nombre']}**")
        col_humor.write(fila["Humor"])
        col_energia.write(f"{fila['Energia']}%")

        if col_boton.button("🗑️ Eliminar", key=f"delete_{indice}"):
            eliminar_registro(indice)

    # -------------------------------
    # Tabla completa
    # -------------------------------
    with st.expander("Ver tabla completa"):
        st.dataframe(df, use_container_width=True)

    # -------------------------------
    # Borrar todo el historial
    # -------------------------------
    st.divider()

    if st.button("🗑️ Borrar todo el historial"):
        st.session_state.historial_vibe = pd.DataFrame(
            columns=["Nombre", "Humor", "Energia"]
        )

        guardar_datos(st.session_state.historial_vibe)

        st.session_state.efecto_pendiente = "coffee"

        st.rerun()

else:
    st.info("Aún no hay registros. ¡Sé la primera en compartir tu vibe!")