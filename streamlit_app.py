import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan - Ulises", page_icon="🏔️", layout="wide")

# FOTO CON RESPALDO - YA NO SE ROMPE
try:
    st.image("teziutlan.jpg", use_container_width=True)
except:
    st.markdown("# 🏔️ TEZIUTLÁN, PUEBLA - LA PERLA DE LA SIERRA")
    st.markdown("### Pueblo Mágico - Amanecer entre la niebla")

st.title("🏔️ IA de Teziutlán")
st.caption("Creada por Ulises - 100% Teziuteca - Whats 231 113 5547")

MODELO = "openai/gpt-oss-20b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres la IA de Teziutlan de Ulises."}]

prompt = st.chat_input("Escribe aquí...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages)
    ans = resp.choices[0].message.content
    st.session_state.messages.append({"role":"assistant","content":ans})
    st.write(ans)
