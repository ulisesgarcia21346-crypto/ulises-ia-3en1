import streamlit as st
st.title("Ulises IA 3 en 1")
idea = st.text_input("Que quieres crear?")
if st.button("Crear"):
    st.image(f"https://image.pollinations.ai/prompt/{idea}")
    st.success("Vendido!")
