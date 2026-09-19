import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")

st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:30px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0;">🏔️ TEZIUTLÁN, PUEBLA</h1>
<h3 style="color:#ffd700; margin:8px 0;">LA PERLA DE LA SIERRA • PUEBLO MÁGICO</h3>
</div>
""", unsafe_allow_html=True)

st.divider()

MODELO = "openai/gpt-oss-120b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

SYSTEM_PROMPT = "Eres la IA de Teziutlán creada por Ulises. Eres cálido, inteligente, útil. Conoces Teziutlán, su neblina, Catedral. Ayudas con marketing local, publicidad, tareas. Explicas con ejemplos y das 3 opciones."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":SYSTEM_PROMPT}]

for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]): st.write(m["content"])

prompt = st.chat_input("Pregúntame lo que sea...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"): st.write(prompt)
    with st.chat_message("assistant"):
        resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages, temperature=0.8, max_tokens=1500)
        ans = resp.choices[0].message.content
        st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.link_button("💬 WhatsApp Ulises", "https://wa.me/522311135547", type="primary", use_container_width=True)
