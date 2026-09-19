import streamlit as st
from groq import Groq
import urllib.parse

st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")

st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:30px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0;">🏔️ TEZIUTLÁN, PUEBLA</h1>
<h3 style="color:#ffd700; margin:8px 0;">LA PERLA DE LA SIERRA • PUEBLO MÁGICO</h3>
<p style="color:#e0e0e0;">Ahora con Generador de Imágenes</p>
</div>
""", unsafe_allow_html=True)

st.divider()

MODELO = "openai/gpt-oss-120b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

SYSTEM_PROMPT = "Eres la IA de Teziutlán creada por Ulises. Eres experto en marketing local. Cuando te pidan publicidad, das 3 ideas de copy + descripción de la foto perfecta para Teziutlán."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":SYSTEM_PROMPT}]

# MOSTRAR CHAT
for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

# CAJA DE TEXTO
prompt = st.chat_input("Pregúntame lo que sea... Ej: Hazme publicidad de café")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages, temperature=0.8, max_tokens=1500)
        ans = resp.choices[0].message.content
        st.write(ans)

        # GENERADOR DE IMAGEN AUTOMATICO
        if "caf" in prompt.lower() or "publicidad" in prompt.lower() or "imagen" in prompt.lower():
            st.write("---")
            st.write("🎨 **Generando imagen para tu publicidad...**")
            # Prompt para imagen
            prompt_imagen = f"{prompt}, Teziutlan Puebla, neblina de la sierra, taza de cafe humeante, estilo profesional, 4k"
            encoded = urllib.parse.quote(prompt_imagen)
            url_imagen = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true"
            st.image(url_imagen, caption="Imagen generada para tu negocio de Teziutlán")
            ans += f"\n\n[Imagen: {url_imagen}]"

        st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()

# BOTON DE IMAGEN RAPIDA
st.subheader("🎨 Generador Rápido de Fotos")
idea_foto = st.text_input("¿Qué foto quieres? Ej: tamales humeantes en el Parque Juárez")
if st.button("Generar Foto", type="primary", use_container_width=True):
    if idea_foto:
        encoded = urllib.parse.quote(f"{idea_foto}, Teziutlan Puebla Pueblo Magico, foto profesional, alta calidad")
        url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true"
        st.image(url, caption=idea_foto)

st.divider()
st.link_button("💬 WhatsApp Ulises - 231 113 5547", "https://wa.me/522311135547", type="primary", use_container_width=True)
