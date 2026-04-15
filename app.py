import streamlit as st
import google.generativeai as genai

st.title("🎬 AI CINE - Productor")

# Configuración directa
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Falta la GEMINI_API_KEY en Secrets.")

idea = st.text_input("Tu idea de clase:")

if st.button("Generar Nombres"):
    if idea:
        try:
            # Usamos la llamada más básica posible
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(f"Genera 3 nombres de película para esta idea escolar: {idea}")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Escribe algo primero.")
