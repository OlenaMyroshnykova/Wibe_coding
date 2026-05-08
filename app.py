import os
import random
import streamlit as st
import pandas as pd
import altair as alt

# -------------------------------
# Configuración de la página
# -------------------------------
st.set_page_config(page_title="Gothic Team Vibe", page_icon="🦇", layout="wide")

# Archivo donde se guardan los datos
DATA_FILE = "historial_vibe.csv"


# -------------------------------
# CSS: diseño gótico
# -------------------------------
st.markdown(
    """
    <style>
    /* Fondo general de la aplicación */
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(120, 0, 60, 0.35), transparent 35%),
            radial-gradient(circle at bottom right, rgba(40, 0, 80, 0.45), transparent 35%),
            linear-gradient(135deg, #07020d 0%, #130015 45%, #050008 100%);
        color: #f2e6ff;
    }

    /* Barra superior de Streamlit */
    header[data-testid="stHeader"] {
        background: #07020d !important;
        color: #f2e6ff !important;
    }

    /* Línea decorativa superior */
    div[data-testid="stDecoration"] {
        background: linear-gradient(90deg, #5c0038, #1f0033) !important;
    }

    /* Barra de herramientas superior */
    div[data-testid="stToolbar"] {
        background: transparent !important;
        color: #f2e6ff !important;
    }

    /* Botones e iconos de la barra superior */
    header button,
    header svg,
    header span {
        color: #f2e6ff !important;
        fill: #f2e6ff !important;
    }

    /* Títulos principales */
    h1 {
        color: #f5d6ff !important;
        text-shadow: 0 0 12px #9b1d64, 0 0 22px #4b0082;
        font-family: Georgia, serif;
        letter-spacing: 1px;
    }

    h2, h3 {
        color: #e8c3ff !important;
        font-family: Georgia, serif;
    }

    /* Texto general */
    p, div, span, label {
        color: #f1e8ff;
    }

    /* Barra lateral */
    section[data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #140018 0%, #07020d 100%);
        border-right: 1px solid #6d214f;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #ffd6f6 !important;
        text-shadow: 0 0 10px #8e164e;
    }

    /* Campos de texto */
    .stTextInput input {
        background-color: #16001f !important;
        color: #fff0fb !important;
        border: 1px solid #c84b8c !important;
        border-radius: 12px !important;
    }

    .stTextInput input::placeholder {
        color: #8f7899 !important;
    }

    /* Selectbox: campo cerrado */
    .stSelectbox div[data-baseweb="select"] > div {
        background-color: #16001f !important;
        color: #fff0fb !important;
        border: 1px solid #c84b8c !important;
        border-radius: 12px !important;
    }

    /* Texto dentro del selectbox cerrado */
    .stSelectbox div[data-baseweb="select"] span {
        color: #fff0fb !important;
    }

    /* Icono de flecha del selectbox */
    .stSelectbox svg {
        fill: #c84b8c !important;
        color: #c84b8c !important;
    }

    /* Popover del menú desplegable */
    div[data-baseweb="popover"] {
        background-color: transparent !important;
    }

    /* Contenedor del menú desplegable */
    ul[role="listbox"] {
        background-color: #16001f !important;
        border: 1px solid #c84b8c !important;
        border-radius: 12px !important;
        box-shadow: 0 0 18px rgba(200, 75, 140, 0.55) !important;
        padding: 6px !important;
    }

    /* Opciones del menú desplegable */
    li[role="option"] {
        background-color: #16001f !important;
        color: #fff0fb !important;
        border-radius: 8px !important;
    }

    /* Texto dentro de cada opción */
    li[role="option"] div,
    li[role="option"] span {
        color: #fff0fb !important;
    }

    /* Opción al pasar el ratón */
    li[role="option"]:hover {
        background-color: #5c0038 !important;
        color: #ffffff !important;
    }

    li[role="option"]:hover div,
    li[role="option"]:hover span {
        color: #ffffff !important;
    }

    /* Opción seleccionada */
    li[aria-selected="true"] {
        background-color: #3a003f !important;
        color: #ffffff !important;
    }

    li[aria-selected="true"] div,
    li[aria-selected="true"] span {
        color: #ffffff !important;
    }

    /* Slider */
    .stSlider {
        color: #f3d6ff !important;
    }

    /* Botones */
    .stButton > button {
        background: linear-gradient(135deg, #5c0038, #1f0033) !important;
        color: #fff0fb !important;
        border: 1px solid #c84b8c !important;
        border-radius: 14px !important;
        padding: 0.55rem 1rem !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px rgba(200, 75, 140, 0.45);
        transition: all 0.2s ease-in-out;
    }

    .stButton > button:hover {
        transform: scale(1.03);
        background: linear-gradient(135deg, #8a0058, #33004d) !important;
        box-shadow: 0 0 20px rgba(255, 120, 190, 0.75);
    }

    /* Tarjetas de métricas */
    div[data-testid="stMetric"] {
        background: rgba(20, 0, 30, 0.78);
        border: 1px solid #7d1b52;
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 0 18px rgba(80, 0, 120, 0.45);
    }

    div[data-testid="stMetricLabel"] {
        color: #e8c3ff !important;
    }

    div[data-testid="stMetricValue"] {
        color: #ffffff !important;
        text-shadow: 0 0 10px #b5179e;
    }

    /* Mensajes de alerta */
    div[data-testid="stAlert"] {
        border-radius: 16px;
        border: 1px solid #7d1b52;
        background-color: rgba(20, 0, 30, 0.78);
        box-shadow: 0 0 14px rgba(100, 0, 120, 0.35);
    }

    /* Tabla de datos */
    div[data-testid="stDataFrame"] {
        border: 1px solid #7d1b52;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 0 14px rgba(100, 0, 120, 0.35);
    }

    /* Tarjeta para cada registro */
    .goth-card {
        background: rgba(12, 0, 20, 0.82);
        border: 1px solid #7d1b52;
        border-radius: 18px;
        padding: 16px 18px;
        margin-bottom: 12px;
        box-shadow: 0 0 14px rgba(110, 0, 90, 0.35);
    }

    /* Separador decorativo */
    .goth-divider {
        border-top: 1px solid #7d1b52;
        margin: 18px 0;
    }

    /* Contenedor del gráfico */
    div[data-testid="stVegaLiteChart"],
    div[data-testid="stArrowVegaLiteChart"] {
        background: rgba(12, 0, 20, 0.65);
        border-radius: 18px;
        padding: 14px;
        border: 1px solid #7d1b52;
        box-shadow: 0 0 14px rgba(110, 0, 90, 0.35);
    }

    /* Expander */
    details {
        background: rgba(12, 0, 20, 0.75) !important;
        border: 1px solid #7d1b52 !important;
        border-radius: 16px !important;
    }

    summary {
        color: #f5d6ff !important;
        font-weight: bold;
    }

    /* Símbolos de la lluvia gótica */
    .goth-symbol {
        position: fixed;
        top: -60px;
        z-index: 999999;
        pointer-events: none;
        animation-name: goth-fall;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
        text-shadow: 0 0 10px #ff4fa3;
    }

    /* Animación de lluvia gótica */
    @keyframes goth-fall {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        80% {
            opacity: 1;
        }
        100% {
            transform: translateY(110vh) rotate(360deg);
            opacity: 0;
        }
    }

    /* Arañas blancas al actualizar la página */
    .white-spider {
        position: fixed;
        top: -60px;
        z-index: 999998;
        pointer-events: none;
        animation-name: spider-fall;
        animation-timing-function: linear;
        animation-fill-mode: forwards;
        color: white;
        text-shadow: 0 0 8px #ffffff, 0 0 14px #cfcfff;
    }

    /* Animación de caída de arañas */
    @keyframes spider-fall {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
        }
        85% {
            opacity: 1;
        }
        100% {
            transform: translateY(110vh) rotate(25deg);
            opacity: 0;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -------------------------------
# Función para cargar datos guardados
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


# -------------------------------
# Función para guardar datos en CSV
# -------------------------------
def guardar_datos(df):
    df.to_csv(DATA_FILE, index=False)


# -------------------------------
# Efecto visual personalizado: lluvia gótica
# -------------------------------
def gothic_rain():
    symbols = ["🦇", "🕯️", "🌙", "🖤", "🥀", "☕"]
    elements = ""

    for i in range(45):
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

    for i in range(35):
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
# Función para decidir el efecto según la energía media
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
# Función para mostrar el efecto pendiente
# -------------------------------
def mostrar_efecto_pendiente():
    efecto = st.session_state.get("efecto_pendiente")

    if efecto == "balloons":
        st.balloons()
    elif efecto == "gothic":
        gothic_rain()

    st.session_state.efecto_pendiente = None


# -------------------------------
# Función para eliminar un registro individual
# -------------------------------
def eliminar_registro(indice):
    st.session_state.historial_vibe = st.session_state.historial_vibe.drop(
        index=indice
    ).reset_index(drop=True)

    guardar_datos(st.session_state.historial_vibe)
    lanzar_efecto_segun_energia(st.session_state.historial_vibe)

    st.rerun()


# -------------------------------
# Cargar datos al iniciar la aplicación
# -------------------------------
if "historial_vibe" not in st.session_state:
    st.session_state.historial_vibe = cargar_datos()

if "efecto_pendiente" not in st.session_state:
    st.session_state.efecto_pendiente = None


# -------------------------------
# Título principal
# -------------------------------
st.title("🦇 Gothic Team Vibe Dashboard")
st.markdown("### 🕯️ ¿Cómo late hoy el alma del equipo?")

# Mostrar arañas blancas al cargar o actualizar la página
spider_rain()

# Mostrar efecto pendiente después de añadir, borrar o eliminar datos
mostrar_efecto_pendiente()


# -------------------------------
# Barra lateral con formulario
# -------------------------------
with st.sidebar:
    st.header("🖤 Tu Registro")

    nombre = st.text_input("Nombre", placeholder="Ej. Morticia")

    humor = st.selectbox(
        "Estado del alma",
        [
            "🌙 Serenidad nocturna",
            "🦇 Energía vampírica",
            "☕ Café oscuro urgente",
            "🥀 Dramáticamente al límite",
        ],
    )

    energia = st.slider("Nivel de energía vital (%)", 0, 100, 50)

    boton_registrar = st.button("Registrar mi Vibe 🕯️")


# -------------------------------
# Procesar nuevo registro
# -------------------------------
if boton_registrar:
    if nombre.strip() == "":
        st.warning("Escribe tu nombre antes de invocar el registro.")
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

        st.success("Registro guardado en el grimorio del equipo 🖤")
        st.rerun()


# -------------------------------
# Visualización de datos
# -------------------------------
df = st.session_state.historial_vibe

if not df.empty:
    promedio = df["Energia"].mean()

    col1, col2 = st.columns(2)

    col1.metric("Energía Vital Promedio", f"{int(promedio)}%")
    col2.metric("Registros en el Grimorio", len(df))

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
    # Gráfico oscuro con Altair
    # -------------------------------
    st.subheader("📊 Historial de Energía Vital")

    chart = (
        alt.Chart(df)
        .mark_bar(
            color="#8a0058",
            cornerRadiusTopLeft=6,
            cornerRadiusTopRight=6,
        )
        .encode(
            x=alt.X(
                "Nombre:N",
                title="Nombre",
                axis=alt.Axis(
                    labelColor="#f2e6ff",
                    titleColor="#e8c3ff",
                    labelAngle=0,
                ),
            ),
            y=alt.Y(
                "Energia:Q",
                title="Energía (%)",
                axis=alt.Axis(
                    labelColor="#f2e6ff",
                    titleColor="#e8c3ff",
                ),
                scale=alt.Scale(domain=[0, 100]),
            ),
            tooltip=[
                alt.Tooltip("Nombre:N", title="Nombre"),
                alt.Tooltip("Humor:N", title="Estado"),
                alt.Tooltip("Energia:Q", title="Energía (%)"),
            ],
        )
        .properties(
            height=360,
            background="#0b0014",
        )
        .configure_view(
            stroke="#7d1b52",
        )
        .configure_axis(
            gridColor="#2d1238",
            domainColor="#7d1b52",
            tickColor="#7d1b52",
            labelColor="#f2e6ff",
            titleColor="#e8c3ff",
        )
    )

    st.altair_chart(chart, use_container_width=True)

    # -------------------------------
    # Lista de registros con eliminación individual
    # -------------------------------
    st.subheader("📜 Registros guardados")

    for indice, fila in df.iterrows():
        st.markdown('<div class="goth-card">', unsafe_allow_html=True)

        col_nombre, col_humor, col_energia, col_boton = st.columns([3, 4, 2, 2])

        col_nombre.write(f"**🖤 {fila['Nombre']}**")
        col_humor.write(fila["Humor"])
        col_energia.write(f"⚡ {fila['Energia']}%")

        if col_boton.button("🗑️ Eliminar", key=f"delete_{indice}"):
            eliminar_registro(indice)

        st.markdown("</div>", unsafe_allow_html=True)

    # -------------------------------
    # Tabla completa dentro de un desplegable
    # -------------------------------
    with st.expander("🕯️ Ver tabla completa del grimorio"):
        st.dataframe(df, use_container_width=True)

    # -------------------------------
    # Botón para borrar todo el historial
    # -------------------------------
    st.markdown('<div class="goth-divider"></div>', unsafe_allow_html=True)

    if st.button("🗑️ Borrar todo el grimorio"):
        st.session_state.historial_vibe = pd.DataFrame(
            columns=["Nombre", "Humor", "Energia"]
        )

        guardar_datos(st.session_state.historial_vibe)
        st.session_state.efecto_pendiente = "gothic"

        st.rerun()

else:
    st.info("🦇 El grimorio está vacío. Sé la primera en dejar tu vibe.")