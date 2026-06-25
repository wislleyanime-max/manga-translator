import streamlit as st
from PIL import Image

st.title("Tradutor de Mangá")

imagem = st.file_uploader(
    "Envie uma imagem",
    type=["png", "jpg", "jpeg"]
)

if imagem:
    img = Image.open(imagem)

    st.image(img)

    st.subheader("Texto detectado")
    st.write("(OCR será adicionado aqui)")

    st.subheader("Tradução")
    st.write("(Tradução aparecerá aqui)")
