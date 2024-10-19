import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import smtplib
from email.message import EmailMessage
import os  # Para variáveis de ambiente
from email_validator import validate_email, EmailNotValidError  # Validação de e-mail
from dotenv import load_dotenv  # Para carregar variáveis de ambiente do .env

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração da página
st.set_page_config(page_title="Portfólio de Tiago Holanda", page_icon="🌎", layout="wide")

# Função para carregar animações Lottie com cache para melhorar o desempenho
@st.cache_data(show_spinner=False)
def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception:
        return None

# Carregar animações Lottie
lottie_animation_home = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_3vbOcw.json")
lottie_animation_contato = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_SdQJtK.json")

# Adicionar estilos CSS personalizados para responsividade
st.markdown("""
    <style>
    /* Importando fonte Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilo para títulos */
    .titulo-principal {
        font-size: 2.5em;
        color: var(--text-color);
        text-align: center;
        font-weight: bold;
    }
    
    /* Estilo para subtítulos */
    .subtitulo {
        font-size: 2em;
        color: var(--text-color);
        margin-top: 20px;
        margin-bottom: 10px;
    }
    
    /* Estilo para texto */
    .texto {
        font-size: 1.2em;
        color: var(--text-color);
        text-align: justify;
    }

    /* Estilo para listas */
    ul.texto li {
        margin-bottom: 10px;
    }

    /* Estilo para links */
    a, a:hover, a:visited {
        color: var(--primary-color);
        text-decoration: none;
    }

    /* Estilo para formulário de contato */
    .formulario {
        background-color: var(--secondary-background-color);
        padding: 20px;
        border-radius: 10px;
        /* Ajustar a sombra conforme o tema */
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    }

    /* Estilo para animações Lottie */
    .lottie {
        margin-top: 20px;
    }

    /* Estilo para os ícones das redes sociais */
    .icone-rede {
        text-align: center;
        margin-top: 20px;
    }
    .icone-rede a {
        margin: 0 10px;
    }
    .icone-rede img {
        width: 40px;
        vertical-align: middle;
    }

    /* Responsividade */
    @media (min-width: 768px) {
        .titulo-principal {
            font-size: 2.5em;
        }
        .subtitulo {
            font-size: 2em;
        }
        .texto {
            font-size: 1.2em;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# Função para validar e-mail usando email-validator
def validar_email(email):
    """
    Valida se o e-mail fornecido é válido.
    """
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

# Função para enviar e-mail
def enviar_email(nome, email_remetente, mensagem):
    """
    Envia um e-mail com as informações fornecidas.
    """
    try:
        # Configuração do e-mail
        email_destino = os.environ.get('EMAIL_DESTINO')  # Use variáveis de ambiente para segurança
        email_usuario = os.environ.get('EMAIL_USUARIO')
        email_senha = os.environ.get('EMAIL_SENHA')

        if not all([email_destino, email_usuario, email_senha]):
            st.error("Configurações de e-mail não encontradas. Por favor, configure as variáveis de ambiente.")
            return False

        msg = EmailMessage()
        msg.set_content(f"Nome: {nome}\nE-mail: {email_remetente}\n\nMensagem:\n{mensagem}")
        msg['Subject'] = f"Contato do Portfólio - {nome}"
        msg['From'] = email_usuario
        msg['To'] = email_destino

        # Configuração do servidor SMTP
        servidor = smtplib.SMTP('smtp.gmail.com', 587)  # Exemplo com Gmail
        servidor.starttls()
        servidor.login(email_usuario, email_senha)
        servidor.send_message(msg)
        servidor.quit()
        return True
    except smtplib.SMTPException as e:
        st.error(f"Ocorreu um erro ao enviar o e-mail: {e}")
        return False
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {e}")
        return False

# Lista de links com ícones, labels e URLs
links_profissionais = [
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/300/300221.png" width="40"/>', 'label': 'Google Acadêmico', 'url': 'https://scholar.google.com.br/citations?user=XLu_qAIAAAAJ&hl=pt-BR'},
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40"/>', 'label': 'LinkedIn', 'url': 'https://www.linkedin.com/in/tiago-holanda-082928141/'},
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40"/>', 'label': 'GitHub', 'url': 'https://github.com/tiagofholanda'},
    {'icon': '<img src="https://lattes.cnpq.br/image/layout_set_logo?img_id=1311768&t=1729293336662" width="40"/>', 'label': 'Lattes', 'url': 'http://lattes.cnpq.br/4969639760120080'},
    {'icon': '<img src="https://help.researchgate.net/hc/theming_assets/01HZPWT1CS5WRP04ZJX0DM6135" width="40"/>', 'label': 'ResearchGate', 'url': 'https://www.researchgate.net/profile/Tiago_Holanda'},
    {'icon': '<img src="https://www.freepnglogos.com/uploads/publons-logo-transparent-png-30.png" width="80"/>', 'label': 'Publons', 'url': 'https://publons.com/researcher/3962699/tiago-holanda/'},
    {'icon': '<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" width="40"/>', 'label': 'ORCID', 'url': 'https://orcid.org/0000-0001-6898-5027'},
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/3313/3313487.png" width="80"/>', 'label': 'Scopus', 'url': 'https://www.scopus.com/authid/detail.uri?authorId=57376293300'},
]

# Função para Currículo
def mostrar_curriculo():
    """
    Exibe o currículo profissional e acadêmico.
    """
    st.markdown('<h1 class="titulo-principal">Currículo Profissional e Acadêmico</h1>', unsafe_allow_html=True)
    
    # Layout usando apenas CSS responsivo
    col1, col2 = st.columns([1, 2], gap="large")
    with col1:
        st.image("https://avatars.githubusercontent.com/u/111590174?v=4", use_column_width=True)
        # Ícones de redes sociais
        links_html = '<div class="icone-rede">'
        for link in links_profissionais:
            links_html += f'<a href="{link["url"]}" target="_blank" title="{link["label"]}">{link["icon"]}</a> '
        links_html += '</div>'
        st.markdown(links_html, unsafe_allow_html=True)
    with col2:
        st.markdown('<h2 class="subtitulo">Resumo Profissional</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p class="texto">
            Profissional com sólida experiência em Geografia e Ciências Geodésicas, atuando como especialista em Geoprocessamento e Análise de Dados Geoespaciais. Doutorando em Geografia pela Universidade Federal Fluminense (UFF), com foco em aplicações avançadas de GIS e tecnologias de geoinformação.
        </p>
        <p class="texto">
            Possuo histórico comprovado no desenvolvimento de soluções WebGIS e na integração de sistemas de automatização de processos utilizando Python, R, PyQt5 e Streamlit. Experiência em aerofotogrametria com drones e análises espaciais e temporais complexas. Minha trajetória acadêmica e profissional reflete um compromisso contínuo com a inovação tecnológica e a excelência na análise espacial, abrangendo um amplo espectro de tecnologias GIS e aplicações geoespaciais avançadas.
        </p>
        """, unsafe_allow_html=True)
    
    # Experiência Profissional
    st.markdown('<h2 class="subtitulo">Experiência Profissional</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>NMC Integrativa</strong><br>
            <strong>Função:</strong> Especialista de Geoprocessamento / Coordenação de Projetos<br>
            <strong>Período:</strong> 04/06/2024 - Presente
        </li>
        <li><strong>RAC Soluções Ambientais</strong><br>
            <strong>Função:</strong> Analista de Planejamento / Geoprocessamento Pleno / Coordenador de Campo<br>
            <strong>Período:</strong> 10/03/2023 até 27/05/2024<br>
            <strong>Atuação:</strong> Prestação de serviço para a Fundação Renova nos programas 07 e 08 no reassentamento familiar.
        </li>
        <li><strong>Empresa Caroá Topografia e Agrimensura</strong><br>
            <strong>Função:</strong> Prestador de Serviço Técnico-Científico<br>
            <strong>Período:</strong> 30/06/2021 até 10/03/2023
        </li>
        <li><strong>Fundação Universidade de Pernambuco (UPE)</strong><br>
            <strong>Função:</strong> Professor do Departamento de Geografia<br>
            <strong>Disciplinas Ministradas:</strong> Cartografia, Geotecnologias, Climatologia, Biogeografia, Geopolítica<br>
            <strong>Período:</strong> 10/02/2021 até 19/07/2022
        </li>
        <li><strong>Secretaria de Educação e Esporte de Pernambuco</strong><br>
            <strong>Função:</strong> Professor de Geografia<br>
            <strong>Período:</strong> 01/10/2021 até 15/07/2022
        </li>
        <li><strong>Município do Cabo de Santo Agostinho</strong><br>
            <strong>Função:</strong> Professor de Geografia<br>
            <strong>Período:</strong> 15/08/2019 até 30/12/2020
        </li>
        <li><strong>Corpo Técnico de Perícia Ambiental no Município de Ipojuca-PE</strong><br>
            <strong>Período:</strong> Março/2021 até Abril/2021
        </li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Projetos e Pesquisas
    st.markdown('<h2 class="subtitulo">Projetos e Pesquisas</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Universidade Federal de Pernambuco (UFPE)</strong><br>
            <strong>Projeto PELDTAMS:</strong> Monitoramento anual de praia utilizando Drone e GNSS para levantamento e comparação de produtos.<br>
            <strong>Período:</strong> Junho/2017 até o presente
        </li>
        <li><strong>Projeto de Doutorado em Ponta de Pedra - PE:</strong> Monitoramento da praia com GNSS e Drone.<br>
            <strong>Período:</strong> Agosto/2017 até Agosto/2018
        </li>
        <li><strong>Monitoramento da Caatinga em Itacuruba-PE utilizando Drone.</strong><br>
            <strong>Período:</strong> Fevereiro de 2019
        </li>
        <li><strong>Projeto de Mestrado:</strong> Monitoramento da Praia do Paiva – PE usando GNSS e Drone.
        </li>
        <li><strong>Monitoramento com Drone na Reserva Biológica Ilha Atol das Rocas, Oceano Atlântico.</strong><br>
            <strong>Período:</strong> Janeiro de 2020 até 2023
        </li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Competências Técnicas
    st.markdown('<h2 class="subtitulo">Competências Técnicas</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <h3>Softwares de Processamento e Modelagem:</h3>
    <ul class="texto">
        <li>Agisoft Photoscan e Metashape</li>
        <li>Pix4D Mapper</li>
        <li>Bentley Systems</li>
        <li>Trimble Business Center (64-bit)</li>
        <li>GTR Processor</li>
        <li>TOPCOM</li>
    </ul>
    
    <h3>Sistemas de Informação Geográfica (GIS):</h3>
    <ul class="texto">
        <li>ArcGIS Desktop, ArcGIS Online, ArcGIS Pro, ArcGIS Apps</li>
        <li>QGIS</li>
        <li>Global Mapper</li>
    </ul>
    
    <h3>Modelagem Costeira:</h3>
    <ul class="texto">
        <li>DELFT 3D</li>
        <li>XBEACH</li>
        <li>SMC – Sistema de Modelagem Costeira</li>
    </ul>
    
    <h3>Linguagens e Ferramentas de Programação:</h3>
    <ul class="texto">
        <li>Python (básico)</li>
        <li>R (básico)</li>
        <li>HTML5 e JavaScript (noções)</li>
    </ul>
    
    <h3>Tecnologias de Sensoriamento Remoto e Topografia:</h3>
    <ul class="texto">
        <li>Experiência em mapeamento com drones (RPAS)</li>
        <li>GNSS</li>
        <li>Sensoriamento Remoto aplicado a ambientes costeiros</li>
    </ul>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <p class="texto">
        Minha trajetória acadêmica e profissional reflete um compromisso contínuo com a inovação tecnológica e a excelência na análise espacial, abrangendo um amplo espectro de tecnologias GIS e aplicações geoespaciais avançadas.
    </p>
    """, unsafe_allow_html=True)

# Função para Portfólio
def mostrar_portfolio():
    """
    Exibe o portfólio de projetos.
    """
    st.markdown('<h1 class="titulo-principal">Portfólio de Projetos</h1>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Abaixo estão alguns dos projetos mais relevantes que desenvolvi ao longo da minha carreira:</p>', unsafe_allow_html=True)
    
    # Projetos
    projetos = [
        {
            "titulo": "Desenvolvimento de Plataforma WebGIS Integrada",
            "descricao": "Criação de uma plataforma WebGIS utilizando Python e Folium para análise geoespacial avançada, integrada com sistemas CRM para gerenciamento de clientes e vendas.",
            "imagem": "https://via.placeholder.com/300x200.png?text=Projeto+1"
        },
        {
            "titulo": "Automatização de Processos com Python",
            "descricao": "Desenvolvimento de scripts para automatização de tarefas repetitivas, integração de APIs e processamento em massa de dados geoespaciais.",
            "imagem": "https://via.placeholder.com/300x200.png?text=Projeto+2"
        },
        {
            "titulo": "Dashboard Interativo para Análise de Desempenho",
            "descricao": "Criação de dashboards interativos utilizando Streamlit e Plotly para visualização de KPIs e métricas de desempenho em tempo real.",
            "imagem": "https://via.placeholder.com/300x200.png?text=Projeto+3"
        }
    ]
    
    # Exibir projetos
    for projeto in projetos:
        st.markdown(f"<h2 class='subtitulo'>{projeto['titulo']}</h2>", unsafe_allow_html=True)
        st.image(projeto['imagem'], use_column_width=True)
        st.markdown(f"<p class='texto'>{projeto['descricao']}</p>", unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# Função para Contato
def mostrar_contato():
    """
    Exibe as informações de contato e um formulário para envio de mensagens.
    """
    st.markdown('<h1 class="titulo-principal">Contato</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="texto">Fique à vontade para entrar em contato comigo através dos seguintes canais:</p>
    """, unsafe_allow_html=True)
    
    # Informações de contato
    st.markdown("""
    <ul class="texto">
        <li><strong>E-mail:</strong> tfholanda@gmail.com / tiagofholanda@hotmail.com</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Exibir os links profissionais
    st.markdown('<h2 class="subtitulo">Redes e Plataformas</h2>', unsafe_allow_html=True)
    links_html = '<div class="icone-rede">'
    for link in links_profissionais:
        links_html += f'<a href="{link["url"]}" target="_blank" title="{link["label"]}">{link["icon"]}</a> '
    links_html += '</div>'
    st.markdown(links_html, unsafe_allow_html=True)
    
    # Formulário de contato
    st.markdown('<h2 class="subtitulo">Enviar uma Mensagem</h2>', unsafe_allow_html=True)
    st.markdown('<div class="formulario">', unsafe_allow_html=True)
    with st.form(key='email_form'):
        nome = st.text_input("Nome")
        email_remetente = st.text_input("E-mail")
        mensagem = st.text_area("Mensagem")
        submit_button = st.form_submit_button(label="Enviar")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit_button:
        if nome and email_remetente and mensagem:
            if validar_email(email_remetente):
                with st.spinner('Enviando mensagem...'):
                    sucesso = enviar_email(nome, email_remetente, mensagem)
                    if sucesso:
                        st.success("Mensagem enviada com sucesso!")
            else:
                st.error("Por favor, insira um endereço de e-mail válido.")
        else:
            st.error("Por favor, preencha todos os campos.")

# Função para a Home
def mostrar_home():
    """
    Exibe a página inicial.
    """
    st.markdown("""
    <p class="texto">
        Olá! Sou Tiago Holanda, um profissional dedicado nas áreas de Geografia e Geoinformação. Navegue pelo meu portfólio para conhecer mais sobre minha trajetória acadêmica, projetos desenvolvidos e como entrar em contato.
    </p>
    """, unsafe_allow_html=True)
    st_lottie(lottie_animation_home, height=300)
    
    # Exibir os links profissionais
    links_html = '<div class="icone-rede">'
    for link in links_profissionais:
        links_html += f'<a href="{link["url"]}" target="_blank" title="{link["label"]}">{link["icon"]}</a> '
    links_html += '</div>'
    st.markdown(links_html, unsafe_allow_html=True)

# Inicializar o estado da página
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

# Função de navegação
def navigation():
    st.markdown('<h1 class="titulo-principal">Portfólio de Tiago Holanda</h1>', unsafe_allow_html=True)
    menu_items = ["Home", "Currículo", "Portfólio", "Contato"]
    cols = st.columns(len(menu_items))
    for i, item in enumerate(menu_items):
        if cols[i].button(item):
            st.session_state.page = item

navigation()

# Exibir a página selecionada
if st.session_state.page == "Home":
    mostrar_home()
elif st.session_state.page == "Currículo":
    mostrar_curriculo()
elif st.session_state.page == "Portfólio":
    mostrar_portfolio()
elif st.session_state.page == "Contato":
    mostrar_contato()
