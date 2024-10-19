# utils.py

import streamlit as st
import requests
import smtplib
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError
from config import EMAIL_DESTINO, EMAIL_USUARIO, EMAIL_SENHA

def validar_email(email):
    """
    Valida se o e-mail fornecido é válido.

    Parâmetros:
    - email (str): O endereço de e-mail a ser validado.

    Retorna:
    - bool: True se o e-mail for válido, False caso contrário.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

def enviar_email(nome, email_remetente, mensagem):
    """
    Envia um e-mail com as informações fornecidas.

    Parâmetros:
    - nome (str): Nome do remetente.
    - email_remetente (str): Endereço de e-mail do remetente.
    - mensagem (str): Conteúdo da mensagem.

    Retorna:
    - bool: True se o e-mail foi enviado com sucesso, False caso contrário.
    """
    try:
        if not all([EMAIL_DESTINO, EMAIL_USUARIO, EMAIL_SENHA]):
            st.error("Configurações de e-mail não encontradas. Por favor, configure as variáveis de ambiente.")
            return False

        msg = EmailMessage()
        msg.set_content(f"Nome: {nome}\nE-mail: {email_remetente}\n\nMensagem:\n{mensagem}")
        msg['Subject'] = f"Contato do Portfólio - {nome}"
        msg['From'] = EMAIL_USUARIO
        msg['To'] = EMAIL_DESTINO

        # Configuração do servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Exemplo com Gmail
        servidor.starttls()
        servidor.login(EMAIL_USUARIO, EMAIL_SENHA)
        servidor.send_message(msg)
        servidor.quit()
        return True
    except smtplib.SMTPException as e:
        st.error(f"Ocorreu um erro ao enviar o e-mail: {e}")
        return False
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")
        return False

@st.cache_data(show_spinner=False)
def load_lottie_url(url):
    """
    Carrega uma animação Lottie a partir de uma URL.

    Parâmetros:
    - url (str): URL da animação Lottie.

    Retorna:
    - dict: Dados da animação Lottie em formato JSON, ou None se falhar.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
        return response.json()
    except Exception:
        return None
