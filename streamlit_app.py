import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan - Ulises", page_icon="🏔️", layout="wide")

# FOTO PRINCIPAL DE TEZIUTLAN
st.image("teziutlan.jpg", use_container_width=True)

st.title("🏔️ IA de Teziutlán - La Perla de la Sierra")
st.markdown("### Creada por Ulises | Publicidad, menús y tareas con IA en 10 seg")
st.caption("📍 100% Teziuteca - WhatsApp: 231 113 5547")

col1, col2, col3 = st.columns(3)
with col1: st.metric("⚡ Rápida", "1000 pal/seg")
with col2: st.metric("📍 Hecha en", "Teziutlán")
with col3: st.metric("💰 Desde", "$99")

st.divider()

MODELO = "openai/gpt-oss-20b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres la IA de Teziutlan creada por Ulises. Ayudas a negocios locales."}]

tab1, tab2, tab3 = st.tabs(["💬 Prueba Gratis", "🍽️ Para Negocios", "📲 Contrátame"])

with tab1:
    for m in st.session_state.messages[1:]:
        with st.chat_message(m["role"]): st.write(m["content"])
    prompt = st.chat_input("Ej: Hazme un menú para tacos...")
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"): st.write(prompt)
        with st.chat_message("assistant"):
            resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages)
            ans = resp.choices[0].message.content
            st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

with tab2:
    st.header("Para Negocios de Teziutlan")
    negocio = st.text_input("Nombre de tu negocio")
    if st.button("🚀 Generar 3 Publicidades", type="primary"):
        r = client.chat.completions.create(model=MODELO, messages=[{"role":"user","content":f"Haz 3 posts vendedores para {negocio} en Teziutlan"}])
        st.success(r.choices[0].message.content)
        st.balloons()

with tab3:
    st.header("¿Quieres que te haga el trabajo?")
    st.link_button("💬 WhatsApp: 231 113 5547 - Soy Ulises", "https://wa.me/522311135547?text=Hola%20Ulises%20vi%20tu%20IA%20de%20Teziutlan", type="primary")
