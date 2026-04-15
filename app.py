import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="AI CINE - Hans Drews Arango", page_icon="🎬")

# Estética de cine
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; color: #ffffff; }
    h1 { color: #00f2ff; } 
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 AI CINE: Productor Inteligente")
st.subheader("Impulsado por Google Gemini")

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
        with st.spinner("Gemini está analizando tu propuesta creativa..."):
            try:
                # Obtener la llave de los Secretos
                api_key = st.secrets["GEMINI_API_KEY"]
                
                # Configurar Google Generative AI
                genai.configure(api_key=api_key)
                
                # Definir el modelo (versión estable)
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                Actúa como un experto en Naming para cine. 
                Un docente del colegio Hans Drews Arango tiene esta idea: "{idea_docente}"
                Su objetivo final es realizar un {producto_final}.
                
                Genera 5 nombres creativos, poderosos y memorables. 
                Mézclalos: algunos en español, otros bilingües, y algunos con un toque de acción o misterio.
                No uses nombres genéricos. 
                Al final, da un consejo muy corto de productor para el docente.
                """

                response = model.generate_content(prompt)
                
                st.success("¡Propuestas Listas!")
                st.markdown(response.text)
                st.info(f"Ruta seleccionada: {producto_final} + {tipo_publicidad}")
                
            except Exception as e:
                st.error(f"Hubo un problema técnico. Verifica la GEMINI_API_KEY en Secrets.")
                st.write(f"Detalle del error: {e}")
    else:
        st.warning("Por favor, escribe una idea para que la IA pueda trabajar.")
