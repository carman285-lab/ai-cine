import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AI CINE - Hans Drews Arango", page_icon="🎬")

st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1 { color: #00f2ff; } 
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 AI CINE: Productor Inteligente")
st.subheader("Configuración Especial Hans Drews Arango")

# --- PASO 1: LA IDEA ---
idea_docente = st.text_area("Describe tu proyecto o actividad:", 
                            placeholder="Ej: Un viaje a la luna...")

col1, col2 = st.columns(2)
with col1:
    producto_final = st.selectbox("¿Qué verán en el cine?", ["Cortometraje", "Documental", "Película"])
with col2:
    tipo_publicidad = st.selectbox("Publicidad:", ["Infografía", "Afiche"])

# --- PASO 3: LÓGICA DE IA ---
if st.button("🌟 GENERAR MI PROYECTO"):
    if idea_docente:
        with st.spinner("Conectando con el satélite de Gemini..."):
            try:
                # 1. Configurar la API
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                
                # 2. Intentar usar el modelo más moderno (1.5 Flash)
                # Si falla, el código probará con el modelo Pro automáticamente
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    test_response = model.generate_content("Hola")
                except:
                    model = genai.GenerativeModel('gemini-pro')
                
                prompt = f"""
                Actúa como un experto en Naming para cine. 
                Idea del docente: "{idea_docente}" para un {producto_final}.
                Colegio: Hans Drews Arango.
                
                Genera 5 nombres creativos y memorables.
                Da un consejo corto de productor.
                """

                response = model.generate_content(prompt)
                
                st.success("¡Propuestas Listas!")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"Error técnico: {e}")
                st.info("Prueba a reiniciar la app en 'Manage app -> Reboot'")
    else:
        st.warning("Por favor, escribe una idea.")
