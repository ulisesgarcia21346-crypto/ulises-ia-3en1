import streamlit as st
st.title("Ulises IA 3 en 1 - Teziutlan")
st.write("Creada por Ulises Vazquez")
idea = st.text_input("Que imagen quieres?")
if st.button("Crear imagen"):
    url = f"https://image.pollinations.ai/prompt/{idea}?nologo=true&seed=1"
    st.image(url)
    st.success("Lista para vender en $200!")
