import streamlit as st
import pandas as pd
import random

st.title("¿Qué prefieres? 🤔")

st.markdown("""
Bienvenido a **¿Qué prefieres?**, el juego de decisiones imposibles.  
Se muestran dos opciones y todos deben votar en voz alta o con la mano cuál prefieren.  
Quien quede en el grupo minoritario (o dude demasiado) bebe.

Elige una categoría y descubre el siguiente dilema.
""")

st.divider()

# --- Diccionario de categorías -> archivo csv ---
categorias = {
    "Completo": "data/prefieres/full_prefieres_limpio.csv",
    "Básico": "data/prefieres/categories/basic.csv",
    "Party": "data/prefieres/categories/party.csv",
    "Hot": "data/prefieres/categories/hot.csv",
#    ".": "data/prefieres/raw/secret.csv"
}

categoria = st.selectbox("Selecciona una categoría", list(categorias.keys()))
csv_path = categorias[categoria]
st.caption(f"Archivo a cargar: `{csv_path}`")

# --- Cargar el CSV en un dataframe temporal ---
if st.button("Cargar categoría"):
    try:
        df = pd.read_csv(csv_path)
        st.session_state.df_frases = df.copy()
        st.session_state.categoria_actual = categoria
        st.session_state.frase_actual = None
        st.success(f"Cargadas {len(df)} frases de la categoría '{categoria}'")
    except FileNotFoundError:
        st.error(f"No se encontró el archivo {csv_path}")

st.divider()

# --- Lógica de selección aleatoria ---
if "df_frases" in st.session_state and st.session_state.df_frases is not None:

    df_frases = st.session_state.df_frases
    restantes = len(df_frases)

    if st.button("🎲 Sacar frase al azar"):
        if restantes > 0:
            idx = random.randint(0, restantes - 1)
            frase = df_frases.iloc[idx]['pref']
            st.session_state.frase_actual = frase
            st.session_state.df_frases = df_frases.drop(index=idx).reset_index(drop=True)
            st.rerun()
        else:
            st.warning("No quedan más frases en esta categoría")

    if st.session_state.get("frase_actual") is not None:
        st.markdown(
            f"""
            <div style="
                background-color: #262730;
                border: 2px solid #FF4B4B;
                border-radius: 12px;
                padding: 30px;
                text-align: center;
                margin-top: 15px;
            ">
                <p style="font-size: 26px; font-weight: 600; color: white; margin: 0;">
                    {st.session_state.frase_actual}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.metric("Frases restantes", len(df_frases))
else:
    st.info("Selecciona una categoría y pulsa 'Cargar categoría' para empezar")