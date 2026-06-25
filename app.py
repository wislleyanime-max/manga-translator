import streamlit as st
import google.generativeai as genai

genai.configure(
    api_key=st.secrets["GEMINI_API_KEY"]
)

modelo = genai.GenerativeModel("gemini-2.5-flash")

st.title("Tradutor de Mangá")

texto = st.text_area("Cole um texto coreano")

if st.button("Traduzir"):
    resposta = modelo.generate_content(
        f"""
        Traduza para português brasileiro.

        Mostre:
        - Tradução principal
        - 3 alternativas
        - Confiança
        - Observações culturais

        Texto:
        {texto}
        """
    )

    st.write(resposta.text)
