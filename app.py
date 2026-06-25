import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

modelo = genai.GenerativeModel("gemini-2.5-flash")

st.title("Tradutor de Mangá e HQ")

idioma = st.selectbox(
    "Traduzir para:",
    [
        "Português",
        "Inglês",
        "Espanhol",
        "Francês",
        "Alemão",
        "Italiano"
    ]
)

arquivo = st.file_uploader(
    "Envie uma imagem",
    type=["png", "jpg", "jpeg"]
)

if arquivo:
    imagem = Image.open(arquivo)

    st.image(imagem)

    if st.button("Traduzir imagem"):
        with st.spinner("Traduzindo..."):
            resposta = modelo.generate_content([
                f"""
                Analise a imagem.

                Detecte automaticamente o idioma.

                Extraia todo o texto encontrado.

                Traduza para {idioma}.

                Para cada trecho mostre:

                Texto original

                Tradução principal

                Alternativas:
                - opção 1
                - opção 2
                - opção 3

                Confiança (%)

                Observações culturais quando necessário.

                Organize a resposta de forma limpa e fácil de ler.
                """,
                imagem
            ])

            st.write(resposta.text)
