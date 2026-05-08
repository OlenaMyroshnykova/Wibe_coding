import os
import random
import streamlit as st
import pandas as pd
import altair as alt

# -------------------------------
# Configuración de la página
# -------------------------------
st.set_page_config(
    page_title="Gothic Team Vibe",
    page_icon="🦇",
    layout="wide"
)

DATA_FILE = "historial_vibe.csv"
REQUIRED_COLUMNS = ["Nombre", "Vibe", "Energía"]

# -------------------------------
# CSS
# -------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(120, 0, 60, 0.35), transparent 35%),
            radial-gradient(circle at bottom right, rgba(40, 0, 80, 0.45), transparent 35%),
            linear-gradient(135deg, #07020d 0%, #130015 45%, #050008 100%);
        color: #f2e6ff;
    }

    header[data-testid="stHeader"] {
        background: #07020d !important;
    }

    h1, h2, h3 {
        color: #f8e9ff;
        font-family: Georgia, serif;
    }

    .main-title {
        font-size: 48px;
        font-weight: 800;
        text-align: center;
        color: #f9d9ff;
        text-shadow: 0 0 14px #b000ff;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #d9b3ff;
        margin-bottom: 30px;
    }

    .box {
        background: rgba(25, 0, 35, 0.85);
        border: 1px solid rgba(220, 150, 255, 0.35);
        border-radius: 22px;
        padding: 25px;
        margin: 15px 0;
        box-shadow: 0 0 25px rgba(160, 0, 255, 0.35);
    }

    .result-card {
        background: linear-gradient(135deg, rgba(40, 0, 55, 0.95), rgba(90, 0, 85, 0.8));
        border: 1px solid rgba(255, 190, 255, 0.4);
        border-radius: 25px;
        padding: 30px;
        margin-top: 20px;
        text-align: center;
        box-shadow: 0 0 35px rgba(200, 0, 255, 0.45);
    }

    .result-name {
        font-size: 38px;
        font-weight: bold;
        color: #ffffff;
        text-shadow: 0 0 12px #ff66ff;
    }

    .result-vibe {
        font-size: 24px;
        color: #ffccff;
        margin-top: 10px;
    }

    .result-energy {
        font-size: 26px;
        color: #ffe066;
        margin-top: 10px;
    }

    .stButton > button {
        background: linear-gradient(135deg, #7b00ff, #ff007f);
        color: white;
        border: none;
        border-radius: 18px;
        padding: 12px 25px;
        font-weight: bold;
        font-size: 17px;
        box-shadow: 0 0 18px rgba(255, 0, 180, 0.6);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #ff007f, #7b00ff);
        color: #ffffff;
        border: none;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #120018, #25002f);
    }

    div[data-testid="stMetricValue"] {
        color: #ffe066;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Datos del equipo
# -------------------------------
TEAM = [
    {
        "name": "Ana",
        "icon": "🖤",
        "vibes": [
            "Misterio elegante",
            "Energía de luna nueva",
            "Drama controlado",
            "Aura de castillo antiguo",
            "Poder silencioso"
        ]
    },
    {
        "name": "Olena",
        "icon": "🖤",
        "vibes": [
            "Café urgente",
            "Código nocturno",
            "Magia de debugging",
            "Inteligencia peligrosa",
            "Reina del caos organizado"
        ]
    },
    {
        "name": "Luy",
        "icon": "🖤",
        "vibes": [
            "Serenidad nocturna",
            "Energía de biblioteca encantada",
            "Calma con sombra",
            "Sabiduría oscura",
            "Vibe de bosque mágico"
        ]
    }
]

# -------------------------------
# Funciones
# -------------------------------
def crear_historial_vacio():
    return pd.DataFrame(columns=REQUIRED_COLUMNS)


def cargar_historial():
    if not os.path.exists(DATA_FILE):
        return crear_historial_vacio()

    try:
        historial = pd.read_csv(DATA_FILE)
    except Exception:
        return crear_historial_vacio()

    # Si el archivo viejo tiene columnas incorrectas, lo ignoramos
    if not all(col in historial.columns for col in REQUIRED_COLUMNS):
        return crear_historial_vacio()

    historial = historial[REQUIRED_COLUMNS].copy()

    historial["Nombre"] = historial["Nombre"].astype(str)
    historial["Vibe"] = historial["Vibe"].astype(str)
    historial["Energía"] = pd.to_numeric(historial["Energía"], errors="coerce")

    historial = historial.dropna(subset=["Energía"])
    historial["Energía"] = historial["Energía"].astype(int)

    return historial


def guardar_registro(nombre, vibe, energia):
    historial = cargar_historial()

    nuevo_registro = pd.DataFrame(
        [
            {
                "Nombre": nombre,
                "Vibe": vibe,
                "Energía": energia
            }
        ]
    )

    historial = pd.concat([historial, nuevo_registro], ignore_index=True)
    historial.to_csv(DATA_FILE, index=False)


def generar_vibe(persona):
    vibe = random.choice(persona["vibes"])
    energia = random.randint(0, 100)
    return vibe, energia


def limpiar_historial():
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)


# -------------------------------
# Título
# -------------------------------
st.markdown(
    '<div class="main-title">🦇 Gothic Team Vibe 🦇</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Generador gótico de energía y vibes del equipo</div>',
    unsafe_allow_html=True
)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("⚙️ Menú")
st.sidebar.write("Opciones de la aplicación")

mostrar_historial = st.sidebar.checkbox("Mostrar registros guardados", value=True)
mostrar_grafico = st.sidebar.checkbox("Mostrar gráfico de energía", value=True)

if st.sidebar.button("🗑️ Borrar historial"):
    limpiar_historial()
    st.sidebar.success("Historial borrado correctamente.")
    st.rerun()

# -------------------------------
# Selección
# -------------------------------
st.markdown("## 🕯️ Selecciona una persona del equipo")

nombres = [persona["name"] for persona in TEAM]

nombre_seleccionado = st.selectbox(
    "Elige un nombre:",
    nombres
)

persona_seleccionada = next(
    persona for persona in TEAM
    if persona["name"] == nombre_seleccionado
)

# -------------------------------
# Generador
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="box">
            <h3>🔮 Generar vibe</h3>
            <p>Pulsa el botón para generar una vibe gótica aleatoria.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    generar = st.button("✨ Generar vibe")

with col2:
    equipo_html = "<div class='box'><h3>👥 Equipo</h3>"
    for persona in TEAM:
        equipo_html += f"<p>{persona['icon']} <strong>{persona['name']}</strong></p>"
    equipo_html += "</div>"

    st.markdown(equipo_html, unsafe_allow_html=True)

# -------------------------------
# Resultado
# -------------------------------
if generar:
    vibe, energia = generar_vibe(persona_seleccionada)

    guardar_registro(
        persona_seleccionada["name"],
        vibe,
        energia
    )

    st.markdown(
        f"""
        <div class="result-card">
            <div class="result-name">{persona_seleccionada["icon"]} {persona_seleccionada["name"]}</div>
            <div class="result-vibe">🌙 {vibe}</div>
            <div class="result-energy">⚡ Energía: {energia}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# -------------------------------
# Cargar historial actualizado
# -------------------------------
historial = cargar_historial()

# -------------------------------
# Historial
# -------------------------------
if mostrar_historial:
    st.markdown("## 📜 Registros guardados")

    if historial.empty:
        st.info("Aún no hay registros guardados.")
    else:
        st.dataframe(
            historial,
            use_container_width=True,
            hide_index=True
        )

# -------------------------------
# Gráfico
# -------------------------------
if mostrar_grafico:
    st.markdown("## 📊 Gráfico de energía")

    if historial.empty:
        st.info("Todavía no hay datos para mostrar el gráfico.")
    else:
        historial_grafico = historial.copy()
        historial_grafico["Registro"] = range(1, len(historial_grafico) + 1)

        chart = (
            alt.Chart(historial_grafico)
            .mark_bar()
            .encode(
                x=alt.X("Registro:O", title="Registro"),
                y=alt.Y("Energía:Q", title="Energía (%)"),
                color=alt.Color("Nombre:N", title="Persona"),
                tooltip=["Nombre", "Vibe", "Energía"]
            )
            .properties(height=350)
        )

        st.altair_chart(chart, use_container_width=True)

# -------------------------------
# Estadísticas
# -------------------------------
st.markdown("## 🧮 Estadísticas")

if historial.empty:
    st.info("Aún no hay estadísticas disponibles.")
else:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de registros", len(historial))

    with col2:
        energia_media = round(historial["Energía"].mean(), 2)
        st.metric("Energía media", f"{energia_media}%")

    with col3:
        persona_top = (
            historial.groupby("Nombre")["Energía"]
            .mean()
            .sort_values(ascending=False)
            .index[0]
        )
        st.metric("Persona con más energía media", persona_top)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")

st.markdown(
    """
    <p style="text-align:center; color:#cfa8ff;">
        🦇 Proyecto creado con Python, Pandas, Altair y Streamlit 🦇
    </p>
    """,
    unsafe_allow_html=True
)