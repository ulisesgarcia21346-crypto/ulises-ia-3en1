import streamlit as st
from groq import Groq
st.set_page_config(page_title="IA Teziutlan", page_icon="🏔️", layout="wide")
st.markdown('<div style="background:#0b3d2e;padding:20px;border-radius:12px;text-align:center;"><h1 style="color:white;">🏔️ IA OFICIAL DE TEZIUTLAN</h1><p style="color:#ffd700;">Comida | Ropa | Uñas | Hoteles | Turismo</p></div>', unsafe_allow_html=True)
client = Groq(api_key=st.secrets["GROQ_API_KEY"])
MODELO = "openai/gpt-oss-120b"
SYSTEM_PROMPT = "Eres la IA OFICIAL de Teziutlan, Puebla. Naciste en Teziutlan. Conoces TODO. No inventes. BASE DE DATOS: TLAYOYOS: 1. Don Tlayoyo Mercado Victoria Local 43 8am-7pm 15 pesos. 2. Dona Mary Mercado Juarez entrada 7am-5pm 12 pesos con chileatole. 3. Tlayoyos del Parque Parque Juarez Sab-Dom 9am-3pm 18 pesos chicharron. 4. La Abuela Allende esq Cuauhtemoc 8am-6pm 14 pesos. 5. Lupita Frente Catedral 4pm-10pm 15 pesos. Tamales Chilahuate Mercado Juarez 7am-2pm 20 pesos. Gelatinas Rompope Paseo Altagracia 10am-8pm 30 pesos. RESTAURANTES: CocinArte Av Cuauhtemoc 61 8am-6:30pm 90-150 pesos. El Patio Allende 509A 24 HORAS 70-120. Mi Viejo Cafe Hidalgo 801 8:30am-8:30pm Chilaquiles 2x1. Cristina Allende 603 9am-11pm 80-130. Tako Tako Mercado Victoria Local 18 tacos 15 pesos. La Fogata Centro 6pm-2am tacos pastor 18. Chilposo Don Juan Mercado Juarez 9am-4pm chilposo 80 pesos. CAFE: Cafe Aguirre Centro 35 americano. Cafe Colibri Hidalgo 40 latte. HOTELES: Posada del Carmen Centro 600-800. Virreynal Allende 700-900. Colonial Parque Juarez 500-650. San Jose Hidalgo 450-600. ROPA: Boutique Aleli Allende ropa mujer 300-800. Milano Centro ropa casual 100-400. Paca La Perla Cuauhtemoc ropa americana desde 20. BELLEZA: Unas Nails Allende 412 acrilico 200 gelish 150. Salon D Liz Hidalgo corte 80 tinte 300. Accesorios Yola Mercado Victoria 30-100. Barberia El Patron Cuauhtemoc corte 70. TURISMO: Catedral, Parque Juarez, Cerro del Aguila subir 7am-10am antes neblina, Paseo Altagracia, Teatro Victoria. DATOS: 90 mil hab, 1940 msnm, Perla Sierra, neblina frio 12-18C lleva sueter, Feria 15 Julio-15 Agosto. INSTRUCCION: Si preguntan donde comer da 3 con direccion y precio REAL. Si preguntan tlayoyos da minimo 3. Si preguntan ropa da 2 boutiques. Si preguntan unas da 2 salones. Si preguntan hotel da 2. Termina siempre: Tu que vendes? Te hago 3 publicidades en 10 segundos - WhatsApp 231 113 5547. Habla como teziuteco."

if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"system","content":SYSTEM_PROMPT}]
for m in st.session_state.messages[1:]:
    with st.chat_message(m["role"]):
        st.write(m["content"])
prompt = st.chat_input("Pregunta lo que sea de Teziutlan...")
if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        resp = client.chat.completions.create(model=MODELO, messages=st.session_state.messages, temperature=0.7, max_tokens=2500)
        ans = resp.choices[0].message.content
        st.write(ans)
        st.session_state.messages.append({"role":"assistant","content":ans})
