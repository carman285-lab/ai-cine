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

# --- PASO 3: LÓGICA DE IA REAL ---
if st.button("🌟 GENERAR MI PROYECTO"):
    if idea_docente:
        with st.spinner("Consultando con el comité de guionistas de IA..."):
            try:
                # Conexión con OpenAI usando los Secretos de Streamlit
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                
                prompt_sistema = f"""
                Eres un creativo de Hollywood experto en Naming. 
                Un docente del colegio Hans Drews Arango tiene esta idea: "{idea_docente}"
                Su objetivo final es realizar un {producto_final}.
                
                Genera 5 nombres creativos, poderosos y memorables. 
                Mézclalos: algunos en español, otros bilingües, y algunos con un toque de acción o misterio.
                No uses nombres genéricos.
                """

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt_sistema}]
                )
                
                nombres_ia = response.choices[0].message.content

                st.success("¡Propuestas de Naming Listas!")
                st.markdown("### 🏆 Títulos Sugeridos para tu Producción:")
                st.write(nombres_ia)
                
                st.info(f"Seleccionado: {producto_final} | Publicidad: {tipo_publicidad}")
                
            except Exception as e:
                st.error("Error: Verifica que hayas configurado la OPENAI_API_KEY en los Secrets de Streamlit.")
                st.write(e)
    else:
        st.warning("Por favor, escribe una idea para que la IA pueda trabajar.")
