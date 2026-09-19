import streamlit as st
from groq import Groq

st.set_page_config(page_title="Ulises IA 3 en 1", page_icon="🚀")
st.title("🚀 Ulises IA 3 en 1")
st.caption("De Teziutlán para el mundo - IA Real Activa")

try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
    st.success("✅ IA Conectada")
except:
    st.error("Falta GROQ_API_KEY en Secrets")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres Ulises IA, asistente de Teziutlán, útil y amigable. Respondes en español."}]

tab1, tab2, tab3 = st.tabs(["💬 Chat IA", "🧠 Tareas", "✨ Ideas"])

with tab1:
    for m in st.session_state.messages[1:]:
        with st.chat_message(m["role"]):
            st.write(m["content"])
    prompt = st.chat_input("Pregunta lo que quieras...")
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            resp = client.chat.completions.create(model="llama-3.1-8b-instant", messages=st.session_state.messages)
            ans = resp.choices[0].message.content
            st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

with tab2:
    tarea = st.text_area("¿Qué tarea quieres planear?")
    if st.button("Crear Plan"):
        if tarea:
            r = client.chat.completions.create(model="llama-3.1-8b-instant", messages=[{"role":"user","content":f"Plan paso a paso para: {tarea}"}])
            st.success(r.choices[0].message.content)

with tab3:
    tema = st.text_input("Tema para ideas")
    if st.button("Dame 5 ideas"):
        if tema:
            r = client.chat.completions.create(model="llama-3.1-8b-instant", messages=[{"role":"user","content":f"5 ideas virales para: {tema}"}])
            st.info(r.choices[0].message.content)
