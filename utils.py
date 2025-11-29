"""
Módulo de utilidades e configurações compartilhadas
"""

import streamlit as st
import requests
import smtplib
import logging
import os
from email.message import EmailMessage
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('portfolio.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()

# ============= CONFIGURAÇÕES =============

PROFESSIONAL_LINKS = [
    {
        'icon': '<img src="https://cdn-icons-png.flaticon.com/512/300/300221.png" width="40"/>',
        'label': 'Google Acadêmico',
        'url': 'https://scholar.google.com.br/citations?user=XLu_qAIAAAAJ&hl=pt-BR'
    },
    {
        'icon': '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40"/>',
        'label': 'LinkedIn',
        'url': 'https://www.linkedin.com/in/tiago-holanda-082928141/'
    },
    {
        'icon': '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40"/>',
        'label': 'GitHub',
        'url': 'https://github.com/tiagofholanda'
    },
    {
        'icon': '<img src="https://lattes.cnpq.br/image/layout_set_logo?img_id=1311768&t=1729293336662" width="40"/>',
        'label': 'Lattes',
        'url': 'http://lattes.cnpq.br/4969639760120080'
    },
    {
        'icon': '<img src="https://c5.rgstatic.net/m/419438641133902/images/icons/svgicons/new-index-logo.svg" width="40"/>',
        'label': 'ResearchGate',
        'url': 'https://www.researchgate.net/profile/Tiago_Holanda'
    },
    {
        'icon': '<img src="https://www.pikpng.com/pngl/m/424-4243430_reviewers-for-these-journals-can-track-verify-and.png" width="80"/>',
        'label': 'Publons',
        'url': 'https://publons.com/researcher/3962699/tiago-holanda/'
    },
    {
        'icon': '<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" width="40"/>',
        'label': 'ORCID',
        'url': 'https://orcid.org/0000-0001-6898-5027'
    },
    {
        'icon': '<img src="https://www.elsevier.com/images/elsevier-logo.svg" width="80"/>',
        'label': 'Scopus',
        'url': 'https://www.scopus.com/authid/detail.uri?authorId=57376293300'
    },
]

# ============= FUNÇÕES DE VALIDAÇÃO E EMAIL =============

def validar_email(email: str) -> bool:
    """
    Valida se o e-mail fornecido é válido.
    
    Args:
        email: String contendo o endereço de e-mail
        
    Returns:
        True se válido, False caso contrário
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        logger.warning(f"E-mail inválido: {email} - {str(e)}")
        return False


def enviar_email(nome: str, email_remetente: str, mensagem: str) -> bool:
    """
    Envia um e-mail com as informações fornecidas.
    
    Args:
        nome: Nome do remetente
        email_remetente: E-mail do remetente
        mensagem: Conteúdo da mensagem
        
    Returns:
        True se enviado com sucesso, False caso contrário
    """
    try:
        # Configuração do e-mail
        email_destino = os.getenv('EMAIL_DESTINO')
        email_usuario = os.getenv('EMAIL_USUARIO')
        email_senha = os.getenv('EMAIL_SENHA')

        if not all([email_destino, email_usuario, email_senha]):
            logger.error("Variáveis de ambiente de e-mail não configuradas")
            st.error("❌ Configurações de e-mail não encontradas. Por favor, configure as variáveis de ambiente.")
            return False

        msg = EmailMessage()
        msg.set_content(f"Nome: {nome}\nE-mail: {email_remetente}\n\nMensagem:\n{mensagem}")
        msg['Subject'] = f"Contato do Portfólio - {nome}"
        msg['From'] = email_usuario
        msg['To'] = email_destino

        # Configuração do servidor SMTP (Gmail)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
            servidor.login(email_usuario, email_senha)
            servidor.send_message(msg)
        
        logger.info(f"E-mail enviado com sucesso de {email_remetente}")
        return True
        
    except smtplib.SMTPException as e:
        logger.error(f"Erro SMTP ao enviar e-mail: {str(e)}")
        st.error(f"❌ Erro ao enviar e-mail: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Erro inesperado ao enviar e-mail: {str(e)}")
        st.error(f"❌ Erro inesperado: {str(e)}")
        return False


# ============= FUNÇÕES DE CACHE E LOTTIE =============

@st.cache_data(show_spinner=False)
def load_lottie_url(url: str):
    """
    Carrega animação Lottie de uma URL com cache.
    
    Args:
        url: URL da animação Lottie
        
    Returns:
        Dados JSON da animação ou None se falhar
    """
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.json()
        else:
            logger.warning(f"Erro ao carregar Lottie: Status {r.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        logger.warning(f"Erro ao carregar Lottie de {url}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Erro ao processar Lottie: {str(e)}")
        return None


@st.cache_data(show_spinner=False)
def load_image(image_path: str):
    """
    Carrega imagem com cache.
    
    Args:
        image_path: Caminho local da imagem
        
    Returns:
        Objeto PIL Image ou None se falhar
    """
    try:
        from PIL import Image
        return Image.open(image_path)
    except Exception as e:
        logger.error(f"Erro ao carregar imagem {image_path}: {str(e)}")
        return None


# ============= FUNÇÕES DE RENDERIZAÇÃO =============

def render_social_links(links=None):
    """
    Renderiza links de redes sociais em HTML.
    
    Args:
        links: Lista de dicionários com ícone, label e url
        
    Returns:
        String HTML contendo os links formatados
    """
    if links is None:
        links = PROFESSIONAL_LINKS
    
    links_html = '<div class="icone-rede">'
    for link in links:
        links_html += f'<a href="{link["url"]}" target="_blank" title="{link["label"]}">{link["icon"]}</a>'
    links_html += '</div>'
    return links_html


def apply_custom_css():
    """
    Aplica estilos CSS personalizados no Streamlit.
    """
    # CSS inline principal
    st.markdown("""
        <style>
        /* Importando font Google */
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');

        :root {
            --primary-color: #0066cc;
            --secondary-color: #00acc1;
            --text-color: #262730;
            --background-color: #ffffff;
            --secondary-bg: #f0f2f6;
        }

        html, body, [class*="css"] {
            font-family: 'Montserrat', sans-serif;
        }

        .titulo-principal {
            font-size: 2.5em;
            color: var(--text-color);
            text-align: center;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        
        .subtitulo {
            font-size: 2em;
            color: var(--text-color);
            margin-top: 1.5rem;
            margin-bottom: 1rem;
            font-weight: 600;
            border-bottom: 3px solid var(--primary-color);
            padding-bottom: 0.5rem;
        }
        
        .texto {
            font-size: 1.1em;
            color: var(--text-color);
            text-align: justify;
            line-height: 1.6;
        }

        ul.texto li {
            margin-bottom: 1rem;
            padding-left: 1.5rem;
        }

        a, a:hover, a:visited {
            color: var(--primary-color);
            text-decoration: none;
        }

        .formulario {
            background-color: var(--secondary-bg);
            padding: 2rem;
            border-radius: 12px;
            border-left: 4px solid var(--primary-color);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            margin: 1.5rem 0;
        }

        .icone-rede {
            text-align: center;
            margin-top: 2rem;
            display: flex;
            justify-content: center;
            gap: 1rem;
            flex-wrap: wrap;
        }

        .icone-rede a {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: var(--secondary-bg);
            transition: all 0.3s ease;
            margin: 0 10px;
        }

        .icone-rede a:hover {
            background-color: var(--primary-color);
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
        }

        .icone-rede img {
            width: 30px;
            vertical-align: middle;
        }

        .stButton > button {
            width: 100%;
            padding: 0.75rem 1.5rem;
            font-size: 1.05rem;
            border-radius: 8px;
            border: 2px solid var(--primary-color);
            background-color: var(--primary-color);
            color: white;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: transparent;
            color: var(--primary-color);
            box-shadow: 0 4px 12px rgba(0, 102, 204, 0.3);
        }

        .stSuccess {
            border-left: 4px solid #00c853 !important;
        }

        .stError {
            border-left: 4px solid #d32f2f !important;
        }

        hr {
            border: none;
            height: 2px;
            background: linear-gradient(to right, transparent, var(--primary-color), transparent);
            margin: 2rem 0;
        }

        @media (max-width: 480px) {
            .titulo-principal {
                font-size: 1.8em;
            }
            
            .subtitulo {
                font-size: 1.3em;
            }
            
            .formulario {
                padding: 1rem;
            }
        }
        </style>
        """, unsafe_allow_html=True)
