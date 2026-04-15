import streamlit as st
import requests

st.set_page_config(page_title="AI CINE - Hans Drews Arango", page_icon="🎬")
st.title("🎬 AI CINE - Productor Inteligente")

idea = st.text_area("Describe tu proyecto pedagógico:", placeholder="Ej: Un viaje a la luna...")

if st.button("🌟 GENERAR PROYECTO"):
    if idea:
        # Sacamos la llave de los Secrets
        api_key = st.secrets.get("GEMINI_API_KEY")
        
        if not api_key:
            st.error("Configura la llave GEMINI_API_KEY en los Secrets de Streamlit.")
        else:
            with st.spinner("Consultando con el comité creativo..."):
                # Conexión directa (esto se salta el error 404 de los modelos)
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
                headers = {'Content-Type': 'application/json'}
                payload = {
                    "contents": [{
                        "parts": [{"text": f"Eres un experto en cine. Genera 5 nombres creativos y potentes en español para este proyecto escolar: {idea}. Al final da un consejo corto para el profesor."}]
                    }]
                }
                
                try:
                    response = requests.post(url, headers=headers, json=payload)
                    data = response.json()
                    
                    # Extraer el texto de la respuesta
                    texto_ia = data['candidates'][0]['content']['parts'][0]['text']
                    
                    st.success("¡Propuestas Listas!")
                    st.markdown(texto_ia)
                except Exception as e:
                    st.error("La llave API no parece estar funcionando. Verifica que la copiaste bien.")
    else:
        st.warning("Escribe una idea primero.")
