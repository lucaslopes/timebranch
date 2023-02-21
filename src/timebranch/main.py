import streamlit as st


def create_folhas_form():
    descricao = st.text_input('Descrição da atividade')
    inicio_button = st.button('Iniciar atividade')
    termino_button = st.button('Terminar atividade')
    concluido = st.checkbox('Atividade concluída')
    feedback = st.text_input('Feedback')
    projeto = st.text_input('Projeto')


def main():
    st.title('TimeBranch')
    st.header('Folhas')
    create_folhas_form()


__name__ == '__main__' and main()