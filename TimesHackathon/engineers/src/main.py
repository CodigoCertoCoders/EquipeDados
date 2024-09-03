import streamlit as st
from load import insert_db, queries

st.set_page_config(layout="wide")
st.title('Gerenciamento do banco de dados do código certo (formulário)')

def atualizar_dados():
    if st.button('Atualizar dados no banco'):
        with st.spinner('Atualizando dados...'):
            resultado = insert_db()
            if resultado == 'Dados atualizados':
                st.success(resultado)
            else:
                st.error(f"Erro: {resultado}")

def mostrar_dados():
    if st.button('Mostrar as 100 linhas mais recentes do banco'):
        with st.spinner('Carregando...'):
            df = queries()
            if 'erro' not in df:
                st.dataframe(df)
            else:
                st.error(f"Erro ao carregar dados: {df}")

col1, col2 = st.columns(2)

with col1:
    atualizar_dados()

with col2:
    mostrar_dados()
