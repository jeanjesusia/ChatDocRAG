import os
import time
import openai
import streamlit as st
from decouple import config
from utils.text_preprocessing import process_pdf
from utils.messages import show_status_message
from utils.vector_store import load_existing_vector_store
from utils.vector_store import add_to_vector_store, check_key
from utils.chat_messages import ask_question

# Configurações da página do Streamlit
st.set_page_config(page_title="ChatDoc - RAG", page_icon="img/chat.png")

# Variáveis de configuração
VALID_API_KEY = False  # Indicador se a chave da API é válida
persist_directory = 'data/vector_db'  # Diretório de persistência do vetor
vector_store = None  # Armazenamento do vetor (inicializado como None)

# Sidebar
with st.sidebar:
    st.header("Bem-vindo ao :blue[Chat]:green[Doc]!")

    # Campo de entrada para a chave da API
    api_key = st.text_input(
        "API KEY", 
        placeholder="YOUR_API_KEY", 
        help="Digite a chave da API fornecida pelo serviço. Mantenha-a segura."
    )

    # Validação da chave da API
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        try:
            check_key(api_key)
            st.success("Sua chave da API é válida!")
            VALID_API_KEY = True
        except openai.AuthenticationError:
            show_status_message("Chave da API inválida!", "error")
        except Exception as e:
            st.warning(f"🚨 Erro com a chave da API: {str(e)}")

    # Upload de arquivos PDF
    uploaded_files = st.file_uploader(
        label="Envie seus arquivos PDF",
        type=['pdf'],
        accept_multiple_files=True
    )

    # Processamento do arquivo PDF
    if uploaded_files:
        if not api_key:
            st.warning("Você precisa fornecer sua chave da API", icon="⚠️")
        else:
            try:
                st.spinner("Processando seu arquivo, aguarde...")
                vector_store = load_existing_vector_store(persist_directory)
                all_chunks = process_pdf(uploaded_files)
                vector_store = add_to_vector_store(
                    chunks=all_chunks,
                    vector_store=vector_store,
                    persist_directory=persist_directory
                )
            except Exception as e:
                st.warning(f"Erro ao processar o arquivo: {str(e)}")

    # Seleção do modelo
    model_options = [
        'gpt-3.5-turbo',
        'gpt-4',
        'gpt-4-turbo',
        'gpt-4o-mini',
        'gpt-4o'
    ]
    selected_model = st.sidebar.selectbox("Selecione um modelo:", options=model_options)

# Layout principal
col1, col2 = st.columns([1, 4])

# Exibindo imagem e texto no layout
with col1:
    st.image("img/bate-papo.png", width=85)

with col2:
    st.header(":blue[Chat]:green[Doc] - Ask your :green[Documents]")

# Iniciando o histórico de mensagens, se necessário
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Campo de entrada para perguntas
question = st.chat_input("Como posso ajudar?")

# Função para exibir o histórico de mensagens
def display_messages():
    """Exibe todas as mensagens armazenadas em st.session_state.messages."""
    for message in st.session_state.messages:
        st.chat_message(message.get('role')).write(message.get('content'))

# Lógica de interação com o modelo
if question and VALID_API_KEY and selected_model:
    vector_store = load_existing_vector_store(persist_directory)
    display_messages()
    st.chat_message('user').write(question)
    st.session_state.messages.append({'role': 'user', 'content': question})

    # Fazendo a consulta para o modelo selecionado
    response = ask_question(
        model=selected_model,
        query=question,
        vector_store=vector_store
    )

    # Exibindo a resposta do modelo
    st.chat_message('ai').write(response)
    st.session_state.messages.append({'role': 'ai', 'content': response})

elif question:
    # Caso a chave da API não seja válida, mas haja uma pergunta
    with st.spinner("Processando..."):
        display_messages()
        st.chat_message('user').write(question)
        st.session_state.messages.append({'role': 'user', 'content': question})
        time.sleep(1)
        st.chat_message('assistant').write("Por favor, forneça a chave da API!")
        st.session_state.messages.append({'role': 'assistant', 'content': "Por favor, forneça a chave da API!"})
