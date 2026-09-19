import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")

# ESTE BANNER NUNCA SE ROMPE
st.markdown("""
<div style="background: linear-gradient(to right, #0f2e1f, #2d6a4f); padding:25px; border-radius:15px; text-align:center; border:2px solid #d4af37;">
<h1 style="color:white; margin:0;">🏔️ TEZIUTLÁN, PUEBLA</h1>
<p style="color:#ffd700; margin:5px; font-weight:bold; letter-spacing:2px;">LA PERLA DE LA SIERRA • PUEBLO MÁGICO</p>
<p style="color:white; margin:0; font-size:12px;">Amanecer entre la niebla • Sierra Norte</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# Intenta mostrar tu foto, si no, muestra la de Wikipedia que SI funciona
try:
    st.image("teziutlan.jpg", use_container_width=True)
except:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Catedral_de_Teziutl%C3%A1n.jpg/800px-Catedral_de_Teziutl%C3%A1n.jpg", caption="Catedral de Teziutlán", use_container_width=True)

st.title("IA de Teziutlán - Hecha por Ulises")
st.caption("WhatsApp: 231 113 5547")

MODELO = "openai/gpt-oss-20b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres IA de Teziutlan."}]

prompt = st.chat_input("Escribe tu idea de negocio...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages)
    ans = resp.choices[0].message.content
    st.write(ans)
    st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.link_button("💬 WhatsApp Ulises", "https://wa.me/522311135547", type="primary")
