import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")

# BANNER FINAL - ESTE SÍ SE VE SIEMPRE
st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:30px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0; font-size:34px;">🏔️ TEZIUTLÁN, PUEBLA</h1>
<h3 style="color:#ffd700; margin:8px 0; letter-spacing:2px;">LA PERLA DE LA SIERRA • PUEBLO MÁGICO</h3>
<p style="color:#e0e0e0; margin:0;">Amanecer entre la niebla • Sierra Norte</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.title("IA de Teziutlán - Hecha por Ulises")
st.markdown("**Publicidad, menús y tareas con IA en 10 segundos**")
st.caption("📍 100% Teziuteca - WhatsApp: 231 113 5547")
st.divider()

MODELO = "openai/gpt-oss-20b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres la IA de Teziutlan creada por Ulises, ayudas a negocios locales de Teziutlan."}]

for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input("Escribe tu idea de negocio...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages)
        ans = resp.choices[0].message.content
        st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.link_button("💬 WhatsApp: 231 113 5547", "https://wa.me/522311135547", type="primary", use_container_width=True)
