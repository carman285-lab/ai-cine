import streamlit as st
from openai import OpenAI
import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AI CINE - Hans Drews Arango", page_icon="🎬")

# Estética de cine
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1 { color: #e50914; } 
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 AI CINE: De la Clase a la Pantalla")
st.subheader("Transforma tus metodologías activas en una superproducción")

# --- PASO 1: LA IDEA ---
st.info("Docente, cuéntanos qué sucede en tu aula. ¡Suelta tu creatividad!")
idea_docente = st.text_area("Describe tu proyecto o actividad:", 
                            placeholder="Ej: Mis estudiantes están creando robots para limpiar el río Otún...")

# --- PASO 2: SELECCIÓN DE DESTINO ---
col1, col2 = st.columns(2)
with col1:
    producto_final = st.selectbox("¿Qué verán en el cine al final de año?", 
                                 ["Cortometraje", "Documental", "Roleplay", "Campaña Publicitaria", "Película"])
with col2:
    tipo_publicidad = st.selectbox("¿Qué publicidad crearemos hoy?", 
                                  ["Infografía", "Afiche", "Video publicitario corto"])

# --- PASO 3: LÓGICA DE IA ---
if st.button("🌟 GENERAR MI PROYECTO"):
    if idea_docente:
        with st.spinner("Nuestro productor de IA está diseñando tu estreno..."):
            # Aquí simulamos la respuesta mientras conectamos la API real
            time.sleep(2) 
            
            st.success("¡Proyecto listo para el estreno!")
            
            st.markdown("### 🏆 Nombres sugeridos por la IA:")
            # En el siguiente paso haremos que estos nombres sean reales
            st.write(f"1. {producto_final}: El Despertar del Hans Drews")
            st.write(f"2. {idea_docente[:20]}...: El Musical")
            
            st.info("Próximo paso: Generación del Video Teaser y el PDF de Ruta.")
    else:
        st.warning("Por favor, escribe una idea para comenzar.")
