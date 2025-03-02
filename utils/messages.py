import streamlit as st
import time

def show_status_message(message, status):
    if status == 'error':
        error_placeholder = st.empty()  # Usando st.empty() para controlar a exibição
        error_placeholder.error(message)
        time.sleep(3)
        error_placeholder.empty()  # Remove o erro