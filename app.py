import pandas as pd
import streamlit as st

from config import COLUMNS, PAGE_ICON, PAGE_TITLE
from storage import cargar_datos, guardar_datos, crear_registro, eliminar_por_indice
from styles import aplicar_estilos
from effects import (
    spider_rain,
    lanzar_efecto_segun_energia,
    mostrar_efecto_pendiente,
)
from charts import mostrar_grafico_energia
from components import (
    mostrar_formulario,
    mostrar_metricas,
    mostrar_mensaje_energia,
    mostrar_registros,
    mostrar_tabla_completa,
    mostrar_boton_borrar_todo,
)


# -------------------------------
# Configuración inicial de Streamlit
# -------------------------------
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

aplicar_estilos()


# -------------------------------
# Inicializar estado de sesión
# -------------------------------
if "historial_vibe" not in st.session_state:
    st.session_state.historial_vibe = cargar_datos()

if "efecto_pendiente" not in st.session_state:
    st.session_state.efecto_pendiente = None


# -------------------------------
# Función para eliminar un registro
# -------------------------------
def eliminar_registro(indice):
    st.session_state.historial_vibe = eliminar_por_indice(
        st.session_state.historial_vibe,
        indice,
    )

    guardar_datos(st.session_state.historial_vibe)
    lanzar_efecto_segun_energia(st.session_state.historial_vibe)

    st.rerun()


# -------------------------------
# Título principal
# -------------------------------
st.title("🦇 Gothic Team Vibe Dashboard")
st.markdown("### 🕯️ ¿Cómo late hoy el alma del equipo?")

spider_rain()
mostrar_efecto_pendiente()


# -------------------------------
# Formulario lateral
# -------------------------------
nombre, humor, energia, boton_registrar = mostrar_formulario()


# -------------------------------
# Procesar nuevo registro
# -------------------------------
if boton_registrar:
    if nombre.strip() == "":
        st.warning("Escribe tu nombre antes de invocar el registro.")
    else:
        nuevo_registro = crear_registro(nombre, humor, energia)

        st.session_state.historial_vibe = pd.concat(
            [st.session_state.historial_vibe, nuevo_registro],
            ignore_index=True,
        )

        guardar_datos(st.session_state.historial_vibe)
        lanzar_efecto_segun_energia(st.session_state.historial_vibe)

        st.success("Registro guardado en el grimorio del equipo 🖤")
        st.rerun()


# -------------------------------
# Visualización principal
# -------------------------------
df = st.session_state.historial_vibe

if not df.empty:
    promedio = mostrar_metricas(df)
    mostrar_mensaje_energia(promedio)
    mostrar_grafico_energia(df)
    mostrar_registros(df, eliminar_registro)
    mostrar_tabla_completa(df)

    if mostrar_boton_borrar_todo():
        st.session_state.historial_vibe = pd.DataFrame(columns=COLUMNS)

        guardar_datos(st.session_state.historial_vibe)
        st.session_state.efecto_pendiente = "gothic"

        st.rerun()

else:
    st.info("🦇 El grimorio está vacío. Sé la primera en dejar tu vibe.")