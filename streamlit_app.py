import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests
import smtplib
import time
import logging
from email.message import EmailMessage
import os
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGENS_DIR = os.path.join(BASE_DIR, "Imagem")
EXTENSOES_IMAGEM = (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp")

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

# Funções auxiliares para carregar projetos locais
def _gerar_descricao_projeto(caminho_projeto: str, titulo: str, total_imagens: int) -> str:
    candidatos = ["descricao.txt", "descricao.md", "README.md", "readme.md"]
    for nome_arquivo in candidatos:
        caminho_arquivo = os.path.join(caminho_projeto, nome_arquivo)
        if os.path.isfile(caminho_arquivo):
            try:
                with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read().strip()
                    if conteudo:
                        return conteudo
            except OSError as erro:
                logging.warning("Não foi possível ler %s: %s", caminho_arquivo, erro)

    return f"Projeto {titulo} com {total_imagens} imagem(ns) demonstrando atividades realizadas nesta frente de trabalho."


@st.cache_data(show_spinner=False)
def carregar_projetos_locais(caminho_base):
    projetos = []
    if not os.path.isdir(caminho_base):
        return projetos

    for pasta in sorted(os.listdir(caminho_base)):
        caminho_projeto = os.path.join(caminho_base, pasta)
        if not os.path.isdir(caminho_projeto):
            continue

        imagens = [
            os.path.join(caminho_projeto, arquivo)
            for arquivo in sorted(os.listdir(caminho_projeto))
            if arquivo.lower().endswith(EXTENSOES_IMAGEM)
        ]

        if not imagens:
            continue

        titulo = pasta.replace("_", " ").title()
        descricao = _gerar_descricao_projeto(caminho_projeto, titulo, len(imagens))

        projetos.append(
            {
                "titulo": titulo,
                "descricao": descricao,
                "imagens": imagens,
            }
        )

    return projetos

# Carregar animações Lottie
lottie_animation_home = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_3vbOcw.json")
lottie_animation_contato = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_SdQJtK.json")

# Adicionar estilos CSS personalizados para responsividade
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');

    :root {
        --bg-color: #0f172a;
        --card-bg: rgba(15,23,42,0.6);
        --accent: #3b82f6;
        --accent-light: #93c5fd;
        --text-light: #f8fafc;
        --muted: #94a3b8;
    }

    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background: var(--bg-color);
        color: var(--text-light);
    }

    .titulo-principal {
        font-size: 2.8em;
        text-align: center;
        font-weight: 700;
        color: var(--text-light);
    }
    
    .subtitulo {
        font-size: 2em;
        color: var(--accent);
        margin-top: 24px;
        margin-bottom: 12px;
        font-weight: 600;
    }
    
    .texto {
        font-size: 1.05em;
        color: var(--text-light);
        text-align: justify;
        line-height: 1.6;
    }

    ul.texto li {
        margin-bottom: 10px;
    }

    a, a:hover, a:visited {
        color: var(--accent-light);
        text-decoration: none;
    }

    .formulario {
        background-color: var(--card-bg);
        padding: 24px;
        border-radius: 14px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
    }

    .icone-rede {
        text-align: center;
        margin-top: 24px;
    }
    .icone-rede a {
        margin: 0 10px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        background: rgba(59,130,246,0.1);
        padding: 10px;
        border-radius: 12px;
        transition: transform 0.2s ease;
    }
    .icone-rede a:hover {
        transform: translateY(-3px);
    }
    .icone-rede img {
        width: 40px;
        vertical-align: middle;
    }

    .hero {
        background: linear-gradient(135deg, rgba(59,130,246,0.25), rgba(14,165,233,0.15));
        padding: 40px;
        border-radius: 24px;
        box-shadow: 0 20px 50px rgba(2,6,23,0.4);
        margin-bottom: 30px;
    }

    .btn-primary {
        display: inline-block;
        padding: 12px 28px;
        border-radius: 999px;
        background: var(--accent);
        color: #fff !important;
        font-weight: 600;
        border: none;
        transition: background 0.2s ease, transform 0.2s ease;
    }
    .btn-primary:hover {
        background: #1d4ed8;
        transform: translateY(-2px);
    }

    .btn-ghost {
        display: inline-block;
        padding: 12px 28px;
        border-radius: 999px;
        border: 1px solid rgba(148,163,184,0.4);
        color: var(--text-light) !important;
        font-weight: 600;
        transition: border 0.2s ease, transform 0.2s ease;
    }
    .btn-ghost:hover {
        border-color: var(--accent);
        transform: translateY(-2px);
    }

    .section-divider {
        width: 120px;
        height: 4px;
        background: linear-gradient(90deg, var(--accent), transparent);
        border-radius: 999px;
        margin: 16px 0 24px;
    }

    .portfolio-badge {
        display: inline-flex;
        background: rgba(99,102,241,0.15);
        color: var(--accent-light);
        border-radius: 999px;
        padding: 6px 14px;
        font-size: 0.85em;
        margin-bottom: 12px;
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
    {'icon': '<img src="https://www.elsevier.com/images/elsevier-logo.svg" width="80"/>', 'label': 'Scopus', 'url': 'https://www.scopus.com/authid/detail.uri?authorId=57376293300'},
]

# Função para Currículo
def mostrar_curriculo():
    """
    Exibe o currículo profissional e acadêmico.
    """
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
            Especialista em Geoprocessamento, Sistemas WebGIS e Análise de Dados, com atuação em desenvolvimento de soluções espaciais, automação de processos com Python e R, integração de bancos PostGIS e visualização de dados em plataformas como Streamlit, Power BI e React/Mapbox. Experiência comprovada em projetos para setores público e privado, além de sólida produção acadêmica e atividades de docência.
        </p>
        """, unsafe_allow_html=True)

    # Dados pessoais
    st.markdown('<h2 class="subtitulo">Dados Pessoais</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Nome:</strong> Tiago Fernando de Holanda</li>
        <li><strong>Endereço:</strong> Rua Rio Grande do Sul, n.º 711, Barro Preto – Belo Horizonte/MG</li>
        <li><strong>Telefones:</strong> (81) 99667-4681</li>
        <li><strong>E-mails:</strong> tfholanda@gmail.com / tiagofholanda@hotmail.com</li>
        <li><strong>Estado Civil:</strong> Solteiro</li>
        <li><strong>Data de Nascimento:</strong> 08/07/1995</li>
        <li><strong>Nacionalidade:</strong> Brasileiro</li>
        <li><strong>Naturalidade:</strong> Cabo de Santo Agostinho/PE</li>
        <li><strong>CNH:</strong> Categoria B</li>
    </ul>
    """, unsafe_allow_html=True)

    # Formação
    st.markdown('<h2 class="subtitulo">Formação Acadêmica e Técnica</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Graduando em Análise e Desenvolvimento de Sistemas – Estácio</li>
        <li>Graduado em Geografia – UFPE (2018)</li>
        <li>Mestre em Ciências Geodésicas e Tecnologia da Geoinformação – UFPE (2020)</li>
        <li>Técnico em Geoprocessamento – IF Sul de Minas</li>
        <li>Técnico em Agrimensura – Especialista em Georreferenciamento</li>
    </ul>
    """, unsafe_allow_html=True)

    # Experiências profissionais
    st.markdown('<h2 class="subtitulo">Experiências Profissionais</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>
            <strong>UFABC</strong><br>
            <strong>Função:</strong> Tutor e Professor da Especialização em Geoprocessamento<br>
            <strong>Atuação:</strong> Orientação de TCC, tutoria em disciplinas específicas e acompanhamento pedagógico da pós-graduação.<br>
            <strong>Período:</strong> 10/07/2023 – 01/08/2025
        </li>
        <li>
            <strong>DEVGIS</strong><br>
            <strong>Função:</strong> Desenvolvedor WebGIS / Especialista de Geoprocessamento<br>
            <strong>Atuação:</strong> React + Mapbox GL JS, APIs REST, dashboards em tempo real, otimização de performance com grandes volumes de dados, integração PostGIS/frontend e bibliotecas internas de mapeamento.<br>
            <strong>Período:</strong> 10/02/2024 – 01/10/2025
        </li>
        <li>
            <strong>AERO Engenharia</strong><br>
            <strong>Função:</strong> Especialista de Geoprocessamento<br>
            <strong>Atuação:</strong> Estruturação de dados GIS, automações com Python e R, dashboards em R/Python, IA para detecção de focos de dengue e implantação de WebGIS com Geoserver/Geonode em nuvem.<br>
            <strong>Período:</strong> 10/02/2025 – 01/10/2025
        </li>
        <li>
            <strong>NMC Integrativa</strong><br>
            <strong>Função:</strong> Especialista de Geoprocessamento / Coordenação de Projetos<br>
            <strong>Atuação:</strong> Estruturação de dados, automação com Python e R, dashboards para gestão e planejamento de tarefas internas.<br>
            <strong>Período:</strong> 04/06/2024 – 15/12/2024
        </li>
        <li>
            <strong>RAC Soluções Ambientais (Fundação Renova)</strong><br>
            <strong>Função:</strong> Analista de Planejamento / Geoprocessamento<br>
            <strong>Atuação:</strong> Automação, mapeamento aerofotogramétrico com drones, dashboards, sensoriamento remoto e supervisão de contratos nos programas 07 e 08 de reassentamento.<br>
            <strong>Período:</strong> 10/03/2023 – 27/05/2024
        </li>
        <li>
            <strong>Empresa Caroá Topografia e Agrimensura</strong><br>
            <strong>Função:</strong> Prestador de serviço técnico-científico<br>
            <strong>Atuação:</strong> Planejamento e execução de mapeamentos aerofotogramétricos e implantação de GIS.<br>
            <strong>Período:</strong> 30/06/2021 – 10/03/2023
        </li>
        <li>
            <strong>Corpo Técnico de Perícia Ambiental – Ipojuca/PE</strong><br>
            <strong>Função:</strong> Consultor Técnico<br>
            <strong>Atuação:</strong> Estruturação de mapeamentos aerofotogramétricos e GIS para perícias ambientais.<br>
            <strong>Período:</strong> 03/2021 – 04/2021
        </li>
        <li>
            <strong>Professor do Departamento de Geografia – UPE</strong><br>
            <strong>Disciplinas:</strong> Cartografia Básica, Cartografia Temática, Estatística Aplicada, Geotecnologias e Afins.<br>
            <strong>Período:</strong> 01/2020 – 07/2021
        </li>
    </ul>
    """, unsafe_allow_html=True)

    # Projetos, Pesquisas e Atuação Acadêmica
    st.markdown('<h2 class="subtitulo">Projetos, Pesquisas e Atuação Acadêmica</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Projeto PELDTAMS (UFPE): monitoramento anual de praia com Drone e GNSS (2017 – atual).</li>
        <li>Doutorado em Ponta de Pedra – PE: monitoramento costeiro com Drone e GNSS (2017 – 2018).</li>
        <li>Monitoramento da Caatinga em Itacuruba/PE com Drone (fev/2019).</li>
        <li>Mestrado – Monitoramento da Praia do Paiva/PE com GNSS e Drone.</li>
        <li>Monitoramento com Drone na Reserva Biológica Ilha Atol das Rocas (2020 – atual).</li>
    </ul>
    """, unsafe_allow_html=True)

    # Competências Técnicas
    st.markdown('<h2 class="subtitulo">Competências Técnicas</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Softwares de processamento e modelagem:</strong> Agisoft Photoscan/Metashape, Pix4D Mapper, Bentley, Trimble Business Center, GTR Processor, TOPCOM.</li>
        <li><strong>GIS:</strong> ArcGIS Desktop/Online/Pro/Server, ArcGIS Apps, QGIS, Global Mapper e manipulação de bancos PostGIS.</li>
        <li><strong>Modelagem Costeira:</strong> DELFT 3D, XBEACH, SMC.</li>
        <li><strong>Programação:</strong> Python, R (incluindo IA), HTML5, JavaScript, desenvolvimento Streamlit, React, Mapbox GL JS.</li>
        <li><strong>Sensoriamento e Topografia:</strong> Operação de drones (RPAS), GNSS, aerofotogrametria, geração de dashboards e análises em Power BI.</li>
    </ul>
    """, unsafe_allow_html=True)

    # Cursos
    st.markdown('<h2 class="subtitulo">Cursos e Capacitações</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>R para geoprocessamento de dados espaciais – UFF (20h)</li>
        <li>Python para geoprocessamento de dados espaciais</li>
        <li>Capacitação ET-EDGV – UFPE (4h)</li>
        <li>Disseminação do banco de dados do IBGE – UFPE (4h)</li>
        <li>Análises de qualidade de dados espaciais – Graltec (2h)</li>
        <li>Introdução ao AutoCAD 3D – Graltec (2h)</li>
        <li>Banco de Dados Espaciais – Graltec (1h)</li>
        <li>VANTs na Topografia – Graltec (2h)</li>
        <li>Mapeamento Aéreo Express – Droneng (2h)</li>
        <li>Google Earth no Geoprocessamento – Graltec (2h)</li>
    </ul>
    """, unsafe_allow_html=True)

    # Conteúdos elaborados
    st.markdown('<h2 class="subtitulo">Conteúdos e Palestras Elaboradas</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li>Palestra/curso sobre drones aplicados à climatologia (UFPE).</li>
        <li>Curso ministrado no Encontro do Pensamento Geográfico – EPG/UFPE (2019).</li>
        <li>Curso para o LACCOST/Departamento de Oceanografia da UFPE (2020).</li>
        <li>Curso no Departamento de Geografia da UFPE – AMPLAGEO (2020).</li>
        <li>Curso no Departamento de Oceanografia da UFPE – LABOGEO (2020).
    </ul>
    """, unsafe_allow_html=True)

# Função para Portfólio
def mostrar_portfolio():
    """
    Exibe o portfólio de projetos.
    """
    st.markdown('<h1 class="titulo-principal">Portfólio de Projetos</h1>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Abaixo estão alguns dos projetos mais relevantes que desenvolvi ao longo da minha carreira:</p>', unsafe_allow_html=True)
    
    projetos = carregar_projetos_locais(IMAGENS_DIR)

    if not projetos:
        st.info("Adicione imagens em subpastas dentro da pasta 'Imagem' para mostrar os projetos automaticamente.")
        return

    projetos_por_pagina = 3
    total_paginas = (len(projetos) + projetos_por_pagina - 1) // projetos_por_pagina
    pagina = st.number_input("Página", min_value=1, max_value=max(1, total_paginas), value=1, step=1)

    inicio = (pagina - 1) * projetos_por_pagina
    fim = inicio + projetos_por_pagina
    projetos_pagina = projetos[inicio:fim]

    for projeto in projetos_pagina:
        with st.container():
            st.markdown("""
                <div class="texto" style="background-color: var(--secondary-background-color, #f5f5f5); padding: 20px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); margin-bottom: 25px;">
            """, unsafe_allow_html=True)
            st.markdown(f"<h2 class='subtitulo' style='margin-top:0'>{projeto['titulo']}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p class='texto'>{projeto['descricao']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='color:#888;'>Total de imagens: {len(projeto['imagens'])}</p>", unsafe_allow_html=True)

            cols = st.columns(2)
            for idx, imagem in enumerate(projeto['imagens']):
                cols[idx % 2].image(imagem, use_column_width=True, caption=f"Imagem {idx + 1}")

            st.markdown("""</div>""", unsafe_allow_html=True)

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