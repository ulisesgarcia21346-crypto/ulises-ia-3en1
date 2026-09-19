import streamlit as st
from groq import Groq
import urllib.parse
from datetime import datetime

st.set_page_config(page_title="IA Teziutlan Negocios", page_icon="🏔️", layout="wide")

st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:25px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0;">🏔️ IA DE NEGOCIOS - TEZIUTLÁN</h1>
<h3 style="color:#ffd700; margin:8px 0;">Datos + Publicidad + Fotos para tu negocio</h3>
</div>
""", unsafe_allow_html=True)

client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODELO = "openai/gpt-oss-120b"

SYSTEM_PROMPT = """
Eres la IA de Negocios de Teziutlán, Puebla, creada por Ulises.
Eres experto en negocios locales de Teziutlán.

Cuando te pregunten por un negocio, SIEMPRE responde en este formato:

📊 **DATOS DEL NEGOCIO EN TEZIUTLÁN:**
- Mejor horario para vender: (ej: 8-11am y 6-9pm porque la gente va al centro)
- Precio promedio en Teziutlán: (ej: café americano $35-45)
- Cliente ideal teziuteco: (ej: estudiantes del centro, familias del barrio)
- Competencia en Teziutlán: (cuántos hay y dónde)

📱 **PUBLICIDAD LISTA PARA FACEBOOK:**
3 copies con gancho local (menciona Catedral, Cerro de Chignautla, neblina, Parque Juárez)

📸 **FOTO PERFECTA:**
Describe la foto exacta que debe tomar

#️⃣ **HASHTAGS TEZIUTLÁN:**
5 hashtags locales

Siempre usa datos de Teziutlán, no genericos.
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":SYSTEM_PROMPT}]

# --- SIDEBAR CON DATOS ---
with st.sidebar:
    st.header("🏪 Tu Negocio")
    tipo_negocio = st.selectbox("¿Qué vendes?", ["Café / Cafetería", "Tacos / Comida", "Ropa / Boutique", "Uñas / Belleza", "Pan / Postres", "Otro"])
    st.info(f"Modo: {tipo_negocio}")
    st.write("**Horarios que más venden en Teziutlán:**")
    st.write("☕ Mañana: 8-11am (oficinistas)\n🌮 Tarde: 2-5pm (comida)\n🌙 Noche: 7-10pm (antojo)")
    st.divider()
    st.link_button("💬 WhatsApp Ulises", "https://wa.me/522311135547", use_container_width=True)

# --- CHAT ---
for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input(f"Pregunta sobre tu {tipo_negocio}... Ej: ¿Cuánto cobrar por café?")

if prompt:
    full_prompt = f"Mi negocio es: {tipo_negocio}. Mi pregunta: {prompt}"
    st.session_state.messages.append({"role":"user","content":full_prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages, temperature=0.8, max_tokens=2000)
        ans = resp.choices[0].message.content
        st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

# --- GENERADOR RAPIDO DE FOTO ---
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.subheader("🎨 Foto para tu negocio")
    idea = st.text_input("Describe la foto", placeholder="cafe humeante en el parque")
    if st.button("Generar Foto", use_container_width=True):
        idea_limpia = idea.replace("é","e").replace("á","a").replace("í","i").replace("ó","o").replace("ú","u")
        encoded = urllib.parse.quote(f"{idea_limpia}, Teziutlan Puebla Mexico, professional photo")
        url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&seed=42"
        st.image(url, caption="Foto lista para tu publicidad")

with col2:
    st.subheader("💰 Calculadora de Precios Teziutlán")
    costo = st.number_input("¿Cuánto te cuesta hacerlo?", min_value=0, value=20)
    if costo > 0:
        precio_venta = costo * 2.5
        ganancia = precio_venta - costo
        st.metric("Precio sugerido en Teziutlán", f"${precio_venta:.0f}")
        st.metric("Tu ganancia", f"${ganancia:.0f}")
        st.caption(f"En Teziutlán la gente paga 2.5x el costo en {tipo_negocio}")
