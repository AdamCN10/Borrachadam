import streamlit as st

st.set_page_config(
    page_title="Borrachadam 2.0",
    page_icon="🍺",
    layout="centered"
)

# Definición de cada juego como página
ruleta = st.Page("games/ruleta.py", title="Ruleta rusa de chupitos", icon="🎯")
verdad_reto = st.Page("games/verdad_reto.py", title="Verdad o Reto", icon="🎲")
yo_nunca = st.Page("games/yo_nunca.py", title="Yo nunca", icon="🙈")
mas_probable = st.Page("games/probable.py", title="Quién es más probable", icon="☝️")
que_prefieres = st.Page("games/prefieres.py", title="Qué prefieres", icon="👍")


# Página home opcional dentro del propio app.py
def home():
    st.title("Borrachadam 2.0🍻")
    st.write("Elige un modo de juego en el menú lateral para empezar.")
    st.image("https://img.magnific.com/premium-vector/hand-holding-beer-logo-design-template-inspiration-vector-illustration_556641-1768.jpg")

home_page = st.Page(home, title="Inicio", icon="🏠", default=True)

pg = st.navigation([home_page, yo_nunca, verdad_reto, mas_probable, que_prefieres, ruleta])
pg.run()