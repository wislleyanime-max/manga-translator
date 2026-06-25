import streamlit as st

st.title("Tradutor de Mangá")

imagem = st.file_uploader(
    "Envie uma imagem",
    type=["png", "jpg", "jpeg"]
)

if imagem:
    st.image(imagem)
    st.success("Imagem carregada com sucesso!")
