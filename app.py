import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
  api_key="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"
)

st.title("revisor de texto curriculum con IA")

puesto = st.text_input("¿Para que puesto estás aplicando?")
cv_text = st.text_area("Pegá tu currículum aca:")

if st.button("revisar CV"):
    if not cv_text.strip():
        st.warning("Por favor, ingresá el contenido del CV.")
    else:
        prompt = f"""
        Sos un experto en Recursos Humanos. Vas a recibir el contenido de un currículum vitae.
        Analizá la gramática, el estilo y la adecuación al perfil profesional indicado.
        Brindá sugerencias claras y puntuales para mejorar el contenido.

        Dividí la respuesta en las siguientes secciones:
        1. Correcciones gramaticales y ortográficas.
        2. Mejora de estilo/redacción.
        3. Recomendaciones para hacerlo más atractivo para el puesto de {puesto}.
        4. Comentario general final.

        Currículum:
        {cv_text}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.subheader("Análisis del CV:")
        st.write(response.choices[0].message.content)

st.title("-----Como funciona?------")
st.write("Pega el contenido formato texto de tu currículum vitae y la IA revisara el resultado y te dara una devolucion, esta app utiliza la API de OpenAi, modelo gpt-4o-mini.")