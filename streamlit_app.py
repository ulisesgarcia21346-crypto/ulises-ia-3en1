import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")

# BANNER
st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:30px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0; font-size:34px;">🏔️ TEZIUTLÁN, PUEBLA</h1>
<h3 style="color:#ffd700; margin:8px 0; letter-spacing:2px;">LA PERLA DE LA SIERRA • PUEBLO MÁGICO</h3>
<p style="color:#e0e0e0; margin:0;">Inteligencia Artificial 100% Teziuteca</p>
</div>
""", unsafe_allow_html=True)

st.write("")
st.title("IA de Teziutlán - Hecha por Ulises")
st.caption("📍 Hecha en Teziutlán • WhatsApp: 231 113 5547")
st.divider()

# CEREBRO MÁS INTELIGENTE
MODELO = "llama-3.3-70b-versatile"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# PROMPT PARA QUE SEA IGUAL DE INTELIGENTE QUE YO
SYSTEM_PROMPT = """
Eres la IA de Teziutlán, creada por Ulises, un emprendedor de Teziutlán, Puebla.

Tu personalidad:
- Eres cálido, inteligente, útil y un poco juguetón, igual que Meta AI.
- Hablas como de Teziutlán, conoces la Sierra Norte, el frío, la neblina, la Catedral, el Parque Juárez, el Teatro Victoria.
- Eres experto en: marketing para negocios locales, hacer menús, publicidad para Facebook, WhatsApp, ideas de ventas, tareas de escuela, recetas, consejos.
- Cuando alguien te pregunta algo, no solo respondes, EXPLICAS el porqué, das ejemplos, das 3 opciones.
- Siempre ayudas a vender más. Si alguien tiene una tienda, fonda, taller, le das ideas prácticas para Teziutlán.
- Nunca dices que eres Llama o Groq, tú eres "La IA de Teziutlán hecha por Ulises".
- Si te preguntan cosas difíciles, las explicas fácil, sin palabras rebuscadas.
- Eres breve en celular, pero das la sustancia real.

Tu objetivo: Que la gente de Teziutlán diga "¡esta IA sí me ayuda de verdad!"
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":SYSTEM_PROMPT}]

for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

prompt = st.chat_input("Pregúntame lo que sea... negocio, tarea, receta...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        # CEREBRO GRANDE + CREATIVIDAD ALTA
        resp = client.chat.completions.create(
            model=MODELO,
            messages=st.session_state.messages,
            temperature=0.8,
            max_tokens=1000
        )
        ans = resp.choices[0].message.content
        st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})

st.divider()
st.link_button("💬 Contratar a Ulises - WhatsApp", "https://wa.me/522311135547?text=Hola%20Ulises%20tu%20IA%20ya%20esta%20bien%20inteligente", type="primary", use_container_width=True)
