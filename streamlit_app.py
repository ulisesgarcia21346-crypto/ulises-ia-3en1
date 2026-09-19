import streamlit as st
from groq import Groq

st.set_page_config(page_title="IA Teziutlan Completa", page_icon="🏔️", layout="wide")

# --- ESTILO ---
st.markdown("""
<div style="background: linear-gradient(135deg, #0b3d2e, #1e6d4f); padding:25px; border-radius:15px; text-align:center; border:2px solid #c9a227;">
<h1 style="color:white; margin:0;">🏔️ IA OFICIAL DE TEZIUTLÁN</h1>
<h3 style="color:#ffd700; margin:8px 0;">Comida | Ropa | Uñas | Hoteles | Turismo | Todo Teziutlán</h3>
<p style="color:white; margin:0;">Hecha por Ulises - Teziuteco - 231 113 5547</p>
</div>
""", unsafe_allow_html=True)

# --- CLIENTE GROQ ---
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODELO = "openai/gpt-oss-120b"

# --- BASE DE DATOS COMPLETA ---
SYSTEM_PROMPT = """
Eres la IA OFICIAL de Teziutlán, Puebla. Naciste en Teziutlán, eres del Barrio del Carmen. Conoces TODO de Teziutlán. No inventes nada, solo usa esta base de datos. H
