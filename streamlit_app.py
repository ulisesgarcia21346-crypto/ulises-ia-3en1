import streamlit as st
from groq import Groq
import urllib.parse
st.set_page_config(page_title="IA Teziutlán - Ulises", page_icon="🏔️", layout="wide")
st.title("🏔️ IA de Teziutlán - Hecha por Ulises")
st.markdown("### ✅ Te hago menús, corridos, tareas y publicidad con IA en 10 seg")
col1, col2, col3 = st.columns(3)
with col1: st.metric("⚡ Súper Rápida", "1000 pal/seg")
with col2: st.metric("📍 Hecha en", "Teziutlán")
with col3: st.metric("💰 Desde", "$99")
st.divider()
MODELO = "openai/gpt-oss-20b"
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":"Eres la IA de Negocios de Teziutlán, creada por Ulises. Ayudas a negocios locales."}]
tab1, tab2, tab4 = st.tabs(["💬 Prueba Gratis", "🍽️ Para Negocios", "📲 Contrátame"])
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
            texto = f"Mira lo que hace la IA de Ulises:\n\n{ans}\n\nhttps://ulises-ia-3en1.streamlit.app"
            link = f"https://wa.me/?text={urllib.parse.quote(texto)}"
            st.link_button("📲 Compartir por WhatsApp", link)
        st.session_state.messages.append({"role":"assistant","content":ans})
with tab2:
    st.header("Para Restaurantes y Negocios")
    negocio = st.text_input("Nombre de tu negocio", placeholder="Ej: Tacos Don Lucho")
    if st.button("Generar Publicidad"):
        r = client.chat.completions.create(model=MODELO, messages=[{"role":"user","content":f"Haz 3 posts para Facebook muy vendores para {negocio} en Teziutlán, con emojis"}])
        st.success(r.choices[0].message.content)
with tab4:
    st.header("¿Quieres que te haga el trabajo?")
    st.write("Mándame WhatsApp y te lo hago en 10 minutos.")
    st.link_button("💬 Mándame WhatsApp - 231 113 5547", "https://wa.me/522311135547?text=Hola%20Ulises%20vi%20tu%20IA%20de%20Teziutlan%20quiero%20trabajo")
    st.write("Precios: $99 un trabajo, $299 tu propia IA")
