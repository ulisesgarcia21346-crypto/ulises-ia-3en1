import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan - Ulises", page_icon="🏔️", layout="wide")

# FOTO QUE SI CARGA - SIN NECESIDAD DE SUBIR ARCHIVO
st.image("https://images.unsplash.com/photo-1518638150340-f706e86654b8?q=80&w=1200", caption="🏔️ Teziutlán, Puebla - La Perla de la Sierra - Pueblo Mágico", use_container_width=True)

st.title("🏔️ IA de Teziutlán - La Perla de la Sierra")
st.markdown("### Creada por Ulises | Publicidad con IA en 10 segundos")
st.caption("📍 100% Teziuteca - WhatsApp: 231 113 5547")

col1, col2, col3 = st.columns(3)
with col1: st.metric("⚡ Rápida", "1000 p/s")
with col2: st.metric("📍 Hecha en", "Teziutlán")
with col3: st.metric("💰 Desde", "$99")

st.divider()

MODELO = "openai/gpt-oss-20b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres la IA de Teziutlan creada por Ulises."}]

tab1, tab2 = st.tabs(["💬 Prueba Gratis", "📲 Contrátame"])

with tab1:
    for m in st.session_state.messages[1:]:
        with st.chat_message(m["role"]): st.write(m["content"])
    prompt = st.chat_input("Ej: Hazme publicidad para tacos...")
    if prompt:
        st.session_state.messages.append({"role":"user","content":prompt})
        with st.chat_message("user"): st.write(prompt)
        with st.chat_message("assistant"):
            resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages)
            ans = resp.choices[0].message.content
            st.write(ans)
            st.session_state.messages.append({"role":"assistant","content":ans})

with tab2:
    st.header("¿Quieres que te haga tu publicidad?")
    st.link_button("💬 Mándame WhatsApp", "https://wa.me/522311135547", type="primary")
