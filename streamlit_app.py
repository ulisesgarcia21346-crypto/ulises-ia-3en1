import streamlit as st

st.set_page_config(page_title="Ulises IA 3 en 1")
st.title("🚀 Ulises IA 3 en 1")
st.success("¡App arreglada! Ya funciona")
st.write("De Teziutlán para el mundo")

mensaje = st.chat_input("Escribe algo aquí...")
if mensaje:
    st.write(f"Dijiste: {mensaje}")
