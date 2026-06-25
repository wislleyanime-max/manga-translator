import streamlit as st
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

modelo = genai.GenerativeModel("gemini-2.5-flash")

st.title("Tradutor de Mangá")

arquivo = st.file_uploader(
"Envie uma imagem",
type=["png", "jpg", "jpeg"]
)

if arquivo:
imagem = Image.open(arquivo)

```
st.image(imagem)

if st.button("Traduzir imagem"):
    resposta = modelo.generate_content([
        """
        Analise a imagem.

        Extraia todo texto encontrado.

        Traduza para português brasileiro.

        Para cada trecho mostre:

        Tradução Principal

        Alternativas:
        - opção 1
        - opção 2
        - opção 3

        Confiança (%)

        Observações culturais quando necessário.
        """,
        imagem
    ])

    st.write(resposta.text)
```
