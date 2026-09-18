import streamlit as st

st.title("Ulises IA 3 en 1 - Teziutlan")
st.write("Creada por Ulises Vazquez")

idea = st.text_input("Que imagen quieres crear?")

if st.button("Crear imagen"):
    if idea:
        url = f"https://image.pollinations.ai/prompt/{idea}?nologo=true&seed=1"
        st.image(url)
        st.success("Lista para vender en $200!")
    else:
        st.warning("Escribe algo primero")
