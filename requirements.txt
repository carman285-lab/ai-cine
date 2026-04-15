# --- PASO 3: LÓGICA DE IA REAL ---
if st.button("🌟 GENERAR MI PROYECTO"):
    if idea_docente:
        with st.spinner("Consultando con el comité de guionistas de IA..."):
            try:
                # Conexión con OpenAI
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
                
                st.info(f"Seleccionado: {producto_final} + Publicidad: {tipo_publicidad}")
                
            except Exception as e:
                st.error("Necesitamos configurar la API Key para que la IA pueda pensar.")
    else:
        st.warning("Por favor, describe tu idea para que la IA pueda trabajar.")
