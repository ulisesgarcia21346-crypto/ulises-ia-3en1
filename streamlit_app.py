import streamlit as st

st.set_page_config(page_title="Ulises IA 3 en 1", page_icon="🚀", layout="wide")

st.title("🚀 Ulises IA 3 en 1")
st.caption("De Teziutlán para el mundo")

# --- MENU 3 EN 1 ---
tab1, tab2, tab3 = st.tabs(["💬 Chat IA", "🧠 Asistente Tareas", "✨ Ideas"])

with tab1:
    st.subheader("Chat")
    st.write("Habla con Ulises IA")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    prompt = st.chat_input("Escribe tu pregunta...")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        # Respuesta simple (luego le conectamos API)
        respuesta = f"¡Hola! Soy Ulises IA. Recibí tu mensaje: '{prompt}'. Estoy listo para ayudarte."
        
        with st.chat_message("assistant"):
            st.write(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})

with tab2:
    st.subheader("Generador de tareas / texto")
    tema = st.text_input("¿Qué necesitas? Ej: tarea de historia")
    if st.button("Generar", key="btn2"):
        if tema:
            st.success(f"Aquí tienes ayuda con: {tema}")
            st.write(f"**Plan para:** {tema}\n\n1. Introducción\n2. Desarrollo\n3. Conclusión\n4. Fuentes")
        else:
            st.warning("Escribe algo primero")

with tab3:
    st.subheader("Generador de Ideas")
    idea = st.text_input("Escribe un tema para darte ideas", key="idea")
    if st.button("Dame ideas", key="btn3"):
        if idea:
            st.info(f"3 ideas para **{idea}**:")
            st.write("1. Una app móvil\n2. Un negocio local en Teziutlán\n3. Un video para TikTok explicándolo")
        else:
            st.warning("Escribe un tema")

st.divider()
st.write("Hecho por Ulises Garcia - 2026")
