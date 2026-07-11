import streamlit as st
import pandas as pd
import random

st.title("Verdad o Reto 🎯")

st.markdown("""
Bienvenido a **Verdad o Reto**, el clásico donde no hay escapatoria.  
Elige una categoría y saca una Verdad o un Reto al azar.
""")

st.divider()

# --- Diccionario de categorías -> archivos csv (verdad, reto) ---
categorias = {
    "Completo": {
        "verdad": "data/verdad/full_verdad_limpio",
        "reto": "data/reto/full_reto_limpio"
    },
    "Básico": {
        "verdad": "data/verdad/categories/basic.csv",
        "reto": "data/reto/categories/basic.csv"
    },
    "Party": {
        "verdad": "data/verdad/categories/party.csv",
        "reto": "data/reto/categories/party.csv"
    },
    "Hot": {
        "verdad": "data/verdad/categories/hot.csv",
        "reto": "data/reto/categories/hot.csv"
    },
}

categoria = st.selectbox("Selecciona una categoría", list(categorias.keys()))
csv_verdad = categorias[categoria]["verdad"]
csv_reto = categorias[categoria]["reto"]

col_a, col_b = st.columns(2)
with col_a:
    st.caption(f"Verdades: `{csv_verdad}`")
with col_b:
    st.caption(f"Retos: `{csv_reto}`")

# --- Cargar ambos CSV en dataframes temporales ---
if st.button("Cargar categoría"):
    try:
        df_v = pd.read_csv(csv_verdad)
        df_r = pd.read_csv(csv_reto)
        st.session_state.df_verdades = df_v.copy()
        st.session_state.df_retos = df_r.copy()
        st.session_state.categoria_actual = categoria
        st.session_state.frase_actual = None
        st.session_state.tipo_actual = None
        st.success(f"Cargadas {len(df_v)} verdades y {len(df_r)} retos de '{categoria}'")
    except FileNotFoundError as e:
        st.error(f"No se encontró el archivo: {e.filename}")

st.divider()

# --- Lógica de selección aleatoria ---
if "df_verdades" in st.session_state and "df_retos" in st.session_state:

    df_verdades = st.session_state.df_verdades
    df_retos = st.session_state.df_retos

    restantes_v = len(df_verdades)
    restantes_r = len(df_retos)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Verdades restantes", restantes_v)
        if st.button("🗣️ Sacar Verdad"):
            if restantes_v > 0:
                idx = random.randint(0, restantes_v - 1)
                frase = df_verdades.iloc[idx]["frase"]
                st.session_state.frase_actual = frase
                st.session_state.tipo_actual = "Verdad"
                st.session_state.df_verdades = df_verdades.drop(index=idx).reset_index(drop=True)
                st.rerun()
            else:
                st.warning("No quedan más verdades en esta categoría")

    with col2:
        st.metric("Retos restantes", restantes_r)
        if st.button("🔥 Sacar Reto"):
            if restantes_r > 0:
                idx = random.randint(0, restantes_r - 1)
                frase = df_retos.iloc[idx]["frase"]
                st.session_state.frase_actual = frase
                st.session_state.tipo_actual = "Reto"
                st.session_state.df_retos = df_retos.drop(index=idx).reset_index(drop=True)
                st.rerun()
            else:
                st.warning("No quedan más retos en esta categoría")

    st.divider()

    if st.session_state.get("frase_actual") is not None:
        etiqueta = st.session_state.get("tipo_actual", "")
        color = "#FF4B4B" if etiqueta == "Reto" else "#4B8BFF"
        st.markdown(
            f"""
            <div style="
                background-color: #262730;
                border: 2px solid {color};
                border-radius: 12px;
                padding: 30px;
                text-align: center;
                margin-top: 15px;
            ">
                <p style="font-size: 16px; color: {color}; margin: 0 0 10px 0; text-transform: uppercase; letter-spacing: 2px;">
                    {etiqueta}
                </p>
                <p style="font-size: 26px; font-weight: 600; color: white; margin: 0;">
                    {st.session_state.frase_actual}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
else:
    st.info("Selecciona una categoría y pulsa 'Cargar categoría' para empezar")