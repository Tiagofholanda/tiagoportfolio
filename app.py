# app.py

import streamlit as st
from streamlit_lottie import st_lottie
from utils import validar_email, enviar_email, load_lottie_url
from config import CSS_STYLE, LINKS_PROFISSIONAIS, LOTTIE_ANIMATIONS

# Configuração da página
st.set_page_config(page_title="Portfólio de Tiago Holanda", page_icon="🌎", layout="wide")

# Aplicar estilos CSS
st.markdown(CSS_STYLE, unsafe_allow_html=True)

# Carregar animações Lottie
lottie_animation_home = load_lottie_url(LOTTIE_ANIMATIONS['home'])
lottie_animation_contato = load_lottie_url(LOTTIE_ANIMATIONS['contato'])

# Inicializar o estado da página
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def mostrar_home():
    """
    Exibe a página inicial.
    """
    st.markdown('<h1 class="titulo-principal">Bem-vindo ao meu Portfólio</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="texto">
        Olá! Sou Tiago Holanda, um profissional dedicado nas áreas de Geografia e Geoinformação. Navegue pelo meu portfólio para conhecer mais sobre minha trajetória acadêmica, projetos desenvolvidos e como entrar em contato.
    </p>
    """, unsafe_allow_html=True)
    st_lottie(lottie_animation_home, height=300)
    # Exibir os links profissionais
    links_html = '<div class="icone-rede">'
    for link in LINKS_PROFISSIONAIS:
        links_html += f'<a href="{link["url"]}" target="_blank" title="{link["label"]}">{link["icon"]}</a> '
    links_html += '</div>'
    st.markdown(links_html, unsafe_allow_html=True)

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
        for link in LINKS_PROFISSIONAIS:
            links_html += f'<a href="{link["url"]}" target="_blank" title="{link["label"]}">{link["icon"]}</a> '
        links_html += '</div>'
        st.markdown(links_html, unsafe_allow_html=True)
    with col2:
        st.markdown('<h2 class="subtitulo">Resumo Profissional</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p class="texto">
        Doutorando em Geografia pela <strong>Universidade Federal Fluminense (UFF)</strong>, desenvolvendo pesquisas no <strong>Laboratório de Geografia Física (LAGEF - UFF)</strong>, no <strong>H2O - Grupo de Pesquisa em Hidrodinâmica, Hidráulica e Oceanografia</strong>, e no <strong>Laboratório de Cartografia Costeira (LACCOST)</strong>. Possuo Mestrado em Ciências Geodésicas e Tecnologias da Geoinformação pela <strong>UFPE</strong> e Graduação em Geografia também pela <strong>UFPE</strong>, onde atuei no Centro de Filosofia e Ciências Humanas-CFCH, no Departamento de Ciência Geográfica.
        </p>
        <p class="texto">
        Minhas áreas de atuação incluem:
        </p>
        <ul class="texto">
            <li>Geomorfologia Costeira e Dinâmica Costeira</li>
            <li>Morfodinâmica Costeira e monitoramento geodésico da linha de costa SIG</li>
            <li>Erosão e proteção Costeira</li>
            <li>Geoprocessamento e sensoriamento remoto com Drones em áreas costeiras</li>
        </ul>
        <p class="texto">
        Também faço parte do corpo editorial e sou revisor de revistas científicas como a <strong>Revista Brasileira de Meio Ambiente (RVBMA)</strong>, <strong>Revista Brasileira de Sensoriamento Remoto (RBSR)</strong> e outras.
        </p>
        """, unsafe_allow_html=True)
    # Formação Acadêmica
    st.markdown('<h2 class="subtitulo">Formação Acadêmica</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Doutorado em Geografia</strong> - Universidade Federal Fluminense (UFF)</li>
        <li><strong>Mestrado em Ciências Geodésicas e Tecnologias da Geoinformação</strong> - Universidade Federal de Pernambuco (UFPE)</li>
        <li><strong>Licenciatura em Geografia</strong> - Universidade Federal de Pernambuco (UFPE)</li>
        <li><strong>Especialização em Georreferenciamento</strong></li>
        <li><strong>Técnico em Geoprocessamento e Agrimensura</strong></li>
    </ul>
    """, unsafe_allow_html=True)
    # Experiência Profissional
    st.markdown('<h2 class="subtitulo">Experiência Profissional</h2>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="texto">
        <li><strong>Especialista em GIS</strong> - NMC (2024 - Presente)
            <ul>
                <li>Desenvolvimento de soluções WebGIS aplicadas ao setor ambiental e consultoria.</li>
                <li>Integração de mapas interativos com sistemas CRM para otimizar processos empresariais.</li>
                <li>Automatização de fluxos de trabalho utilizando Python, PyQt5 e Streamlit.</li>
            </ul>
        </li>
        <li><strong>Analista GEO e Planejamento Sênior</strong> - Fundação Renova
            <ul>
                <li>Responsável por projetos de planejamento e análise espacial para recuperação ambiental.</li>
                <li>Atuação nos programas 07 e 08, focados na recuperação produtiva e econômica de famílias afetadas.</li>
            </ul>
        </li>
    </ul>
    """, unsafe_allow_html=True)

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
    for link in LINKS_PROFISSIONAIS:
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

def navigation():
    """
    Cria a barra de navegação do aplicativo.
    """
    st.markdown('<h1 class="titulo-principal">Portfólio de Tiago Holanda</h1>', unsafe_allow_html=True)
    menu_items = ["Home", "Currículo", "Portfólio", "Contato"]
    cols = st.columns(len(menu_items))
    for i, item in enumerate(menu_items):
        if cols[i].button(item):
            st.session_state.page = item

# Exibir a barra de navegação
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
