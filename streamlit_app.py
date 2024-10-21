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
    {'icon': '<img src="https://c5.rgstatic.net/m/419438641133902/images/icons/svgicons/new-index-logo.svg" width="40"/>', 'label': 'ResearchGate', 'url': 'https://www.researchgate.net/profile/Tiago_Holanda'},
    {'icon': '<img src="https://www.pikpng.com/pngl/m/424-4243430_reviewers-for-these-journals-can-track-verify-and.png" width="80"/>', 'label': 'Publons', 'url': 'https://publons.com/researcher/3962699/tiago-holanda/'},
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
    
    st.markdown("""
    <ul class="texto">
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>NMC Integrativa</strong><br>
            <strong>Função:</strong> Especialista de Geoprocessamento / Coordenação de Projetos<br>
            <strong>Período:</strong> 04/06/2024 - Presente
        </div>
        <img src="data:image/png;base64,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" alt="Logo NMC" width="150" style="margin-left: 10px;">
    </li>
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>RAC Soluções Ambientais</strong><br>
            <strong>Função:</strong> Analista de Planejamento / Geoprocessamento Pleno / Coordenador de Campo<br>
            <strong>Período:</strong> 10/03/2023 até 27/05/2024<br>
            <strong>Atuação:</strong> Prestação de serviço para a Fundação Renova nos programas 07 e 08 no reassentamento familiar.
        </div>
        <img src="https://lh3.googleusercontent.com/lSrRMNY3tolnT8AkKaY3ee6QZ4WrkSs1sLP8UtZpQSvdN2seU4lA6ZQzpr8YTTc0378jXzrHtytynw_tcDuLZLvHeiD1N4aWvffRXp5qNaOyC-F6=w1280" alt="Logo RAC" width="150" style="margin-left: 10px;">
        <img src="https://www.fundacaorenova.org/wp-content/themes/fundacao-2016/web/assets/images/logo.svg" alt="Logo RAC" width="150" style="margin-left: 10px;">
    </li>
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>Empresa Caroá Topografia e Agrimensura</strong><br>
            <strong>Função:</strong> Prestador de Serviço Técnico-Científico<br>
            <strong>Período:</strong> 30/06/2021 até o momento
        </div>
        <img src="https://caroatopoagri.com.br/wp-content/uploads/2021/09/CAROA_PAISAGEM_preto-2048x833.png" alt="Logo Caroá" width="150" style="margin-left: 10px;">
    </li>
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>Fundação Universidade de Pernambuco (UPE)</strong><br>
            <strong>Função:</strong> Professor do Departamento de Geografia<br>
            <strong>Disciplinas Ministradas:</strong> Cartografia, Geotecnologias, Climatologia, Biogeografia, Geopolítica<br>
            <strong>Período:</strong> 10/02/2021 até 19/07/2022
        </div>
        <img src="https://www.upe.br/images/industrix/logo-nova4.png" alt="Logo UPE" width="80" style="margin-left: 10px;">
    </li>
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>Secretaria de Educação e Esporte de Pernambuco</strong><br>
            <strong>Função:</strong> Professor de Geografia<br>
            <strong>Período:</strong> 01/10/2021 até 15/07/2022
        </div>
        <img src="data:image/png;base64,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" alt="Logo SEE-PE" width="100" style="margin-left: 10px;">
    </li>
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>Município do Cabo de Santo Agostinho</strong><br>
            <strong>Função:</strong> Professor de Geografia<br>
            <strong>Período:</strong> 15/08/2019 até 30/12/2020
        </div>
        <img src="data:image/jpeg;base64,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" alt="Logo Cabo de Santo Agostinho" width="80" style="margin-left: 10px;">
    </li>
    <li style="display: flex; justify-content: flex-start; align-items: center;">
        <div>
            <strong>Corpo Técnico de Perícia Ambiental no Município de Ipojuca-PE</strong><br>
            <strong>Período:</strong> Março/2021 até Abril/2021
        </div>
        <img src="https://www.ipojuca.pe.gov.br/wp-content/uploads/2024/07/logosemslogan.png" alt="Logo Ipojuca" width="150" style="margin-left: 10px;">
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
