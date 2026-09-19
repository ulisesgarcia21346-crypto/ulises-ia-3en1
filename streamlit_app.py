import streamlit as st
from groq import Groq
import urllib.parse

st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")

st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:25px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0;">🏔️ IA DE NEGOCIOS - TEZIUTLÁN</h1>
<h3 style="color:#ffd700; margin:8px 0;">Datos reales + Publicidad</h3>
</div>
""", unsafe_allow_html=True)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODELO = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """
Eres la IA de Negocios de Teziutlán, Puebla, creada por Ulises.
Conoces los negocios REALES de Teziutlán con datos verificados.

BASE DE DATOS REAL DE TEZIUTLÁN:

1. CocinArte - Av Cuauhtémoc 61, Centro. 8am-6:30pm. $90-150 por platillo. Fusion serrana, tacos de carnitas con mango, mole. Rating 4.6
2. El Patio - Allende 509A, Centro. ABIERTO 24 HORAS. Desayunos, tacos al pastor, enchiladas.
3. Mi Viejo Café - Av Hidalgo 801, Centro. 8:30am-8:30pm. Chilaquiles 2x1 Lun-Vie 8am-12pm. Rating 4.9
4. Tlayoyos Don Tlayoyo - Mercado Victoria Local 43. 8am-7pm. 28 años de tradición. Tlayoyos de frijol con pipian.
5. Taquería El Tako Tako - Mercado Victoria Local 18. 8am-8pm. Tacos típicos.
6. Cristina Restaurante - Allende 603. 9am-11pm. Chilaquiles, burritos de chistorra.
7. Gelatinas con Rompope - Paseo Altagracia Calderón y en el centro comercial subterráneo. Postre típico.
8. Tamales de Chilahuate - Mercado Juárez, Parque Juárez. Con atole de grano.

COMIDA TIPICA: tlayoyos, chilposo, chileatole, tamales de chilahuate, gelatinas con rompope, atole de grano.

Cuando pregunten "¿dónde comer?" responde con 3 opciones reales según presupuesto, horario y antojo, con dirección y horario exacto. No inventes.
Luego ofrece hacerle publicidad para su negocio.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":SYSTEM_PROMPT}]

for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input("Ej: ¿Dónde comer rico en Teziutlán?")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages, temperature=0.7, max_tokens=2000)
        ans = resp.choices[0].message.content
        st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.link_button("💬 WhatsApp Ulises - 231 113 5547", "https://wa.me/522311135547", use_container_width=True)
