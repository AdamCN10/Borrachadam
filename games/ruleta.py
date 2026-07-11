import streamlit as st
import random

st.title("🎯 Ruleta rusa de chupitos")

if "jugadores" not in st.session_state:
    st.session_state.jugadores = []

nuevo_jugador = st.text_input("Nombre del jugador", key="input_jugador")

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Añadir jugador"):
        if nuevo_jugador.strip():
            st.session_state.jugadores.append(nuevo_jugador.strip())
            st.rerun()
        else:
            st.warning("Escribe un nombre antes de añadir")

with col2:
    if st.button("🗑️ Limpiar lista"):
        st.session_state.jugadores = []
        st.rerun()

st.subheader("Jugadores en la partida")
if st.session_state.jugadores:
    for i, j in enumerate(st.session_state.jugadores, start=1):
        st.write(f"{i}. {j}")
else:
    st.info("Aún no hay jugadores añadidos")

st.divider()

if st.button("🎯 Girar la ruleta"):
    if st.session_state.jugadores:
        elegido = random.choice(st.session_state.jugadores)
        st.success(f"¡{elegido} bebe! 🍺")
    else:
        st.warning("Añade al menos un jugador antes de girar")