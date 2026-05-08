import os
import pandas as pd
from config import DATA_FILE, COLUMNS


# -------------------------------
# Cargar datos guardados desde CSV
# -------------------------------
def cargar_datos():
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)

        for columna in COLUMNS:
            if columna not in df.columns:
                df[columna] = ""

        return df[COLUMNS]

    return pd.DataFrame(columns=COLUMNS)


# -------------------------------
# Guardar datos en CSV
# -------------------------------
def guardar_datos(df):
    df.to_csv(DATA_FILE, index=False)


# -------------------------------
# Crear un registro nuevo
# -------------------------------
def crear_registro(nombre, humor, energia):
    return pd.DataFrame(
        [
            {
                "Nombre": nombre.strip(),
                "Humor": humor,
                "Energia": energia,
            }
        ]
    )


# -------------------------------
# Eliminar un registro por índice
# -------------------------------
def eliminar_por_indice(df, indice):
    return df.drop(index=indice).reset_index(drop=True)