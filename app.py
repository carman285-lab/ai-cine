import streamlit as st
import google.generativeai as genai
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AI CINE - Hans Drews Arango", page_icon="🎬")

st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1 { color: #00f2ff; } 
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 AI CINE: Productor Inteligente")
st.subheader("Impulsado por Google Gemini")

# --- PASO 1: LA IDEA ---
idea_docente = st.text_area("Describe tu proyecto pedagógico:", 
                            placeholder="Ej: Estudiantes de inglés graban un podcast sobre leyendas de Pereira...")

col1, col2 = st.columns(2)
with col1:
    producto_final = st.selectbox("Producto de fin de año:", 
                                 ["Cortometraje", "Documental", "Roleplay", "Campaña Publicitaria", "Película"])
with col2:
    tipo_publicidad = st.selectbox("Pieza publicitaria inicial:", 
                                  ["Infografía", "Afiche", "Video publicitario corto"])

# --- PASO 3: LÓGICA DE GEMINI ---
if st.button("🌟 GENERAR MI PROYECTO"):
    if idea_docente:
        with st.spinner("Gemini está analizando tu propuesta creativa..."):
            try:
                # Configurar la API de Google
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                Actúa como un experto en Naming para cine. 
                Idea del docente: "{idea_docente}"
                Tipo de producto: {producto_final}
                Colegio: Hans Drews Arango.
                
                Genera 5 nombres creativos y memorables (algunos bilingües).
                Luego, da un consejo corto de productor para lograr este {producto_final}.
                """

                response = model.generate_content(prompt)
                
                st.success("¡Propuestas Listas!")
                st.markdown(response.text)
                st.info(f"Ruta: {producto_final} -> {tipo_publicidad}")
                
            except Exception as e:
                st.error("Error de conexión. Verifica la GEMINI_API_KEY en Secrets.")
    else:
        st.warning("Por favor, describe tu idea.")
