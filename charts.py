import altair as alt
import streamlit as st


# -------------------------------
# Mostrar gráfico oscuro de energía
# -------------------------------
def mostrar_grafico_energia(df):
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