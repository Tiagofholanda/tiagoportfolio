"""
Módulo contendo as páginas do portfólio
"""

import streamlit as st
from streamlit_lottie import st_lottie
import time
from utils import (
    load_lottie_url, 
    validar_email, 
    enviar_email,
    PROFESSIONAL_LINKS,
    render_social_links
)


def pagina_home():
    """Exibe a página inicial."""
    st.markdown('<h1 class="titulo-principal">Portfólio de Tiago Holanda</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="texto">
        🎓 Olá! Sou Tiago Holanda, um profissional dedicado nas áreas de <strong>Geografia</strong> e <strong>Geoinformação</strong>. 
        Specialista em Geoprocessamento, WebGIS e análise geoespacial avançada.
        <br><br>
        Navegue pelo meu portfólio para conhecer mais sobre minha trajetória acadêmica, projetos desenvolvidos e como entrar em contato.
    </p>
    """, unsafe_allow_html=True)
    
    # Animação Lottie
    lottie_animation = load_lottie_url("https://assets1.lottiefiles.com/packages/lf20_3vbOcw.json")
    if lottie_animation:
        st_lottie(lottie_animation, height=300)
    
    # Links profissionais
    st.markdown(render_social_links(), unsafe_allow_html=True)
    
    # Destaque de informações
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📚 Experiência", "7+ anos", "Em Geoinformação")
    with col2:
        st.metric("🏆 Projetos", "15+", "Concluídos")
    with col3:
        st.metric("🔧 Tecnologias", "20+", "Dominadas")


def pagina_curriculo():
    """Exibe o currículo profissional e acadêmico."""
    st.markdown('<h1 class="titulo-principal">Currículo Profissional e Acadêmico</h1>', unsafe_allow_html=True)
    
    # Resumo profissional
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.image("https://avatars.githubusercontent.com/u/111590174?v=4", use_column_width=True)
        st.markdown(render_social_links(), unsafe_allow_html=True)
    
    with col2:
        st.markdown('<h2 class="subtitulo">Resumo Profissional</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p class="texto">
            Profissional com sólida experiência em Geografia e Ciências Geodésicas, atuando como especialista em 
            <strong>Geoprocessamento</strong> e <strong>Análise de Dados Geoespaciais</strong>. 
            Doutorando em Geografia pela Universidade Federal Fluminense (UFF), com foco em aplicações avançadas de GIS.
        </p>
        """, unsafe_allow_html=True)
    
    # Experiência profissional
    st.markdown('<h2 class="subtitulo">Experiência Profissional</h2>', unsafe_allow_html=True)
    
    experiencias = [
        {
            "empresa": "NMC Integrativa",
            "funcao": "Especialista de Geoprocessamento / Coordenação de Projetos",
            "periodo": "04/06/2024 - Presente",
            "logo": "https://lh3.googleusercontent.com/d"
        },
        {
            "empresa": "RAC Soluções Ambientais",
            "funcao": "Analista de Planejamento / Geoprocessamento Pleno",
            "periodo": "10/03/2023 até 27/05/2024"
        },
        {
            "empresa": "Empresa Caroá Topografia",
            "funcao": "Prestador de Serviço Técnico-Científico",
            "periodo": "30/06/2021 até o momento"
        },
    ]
    
    for exp in experiencias:
        with st.expander(f"🏢 {exp['empresa']} - {exp['periodo']}"):
            st.markdown(f"<p class='texto'><strong>Função:</strong> {exp['funcao']}</p>", unsafe_allow_html=True)
    
    # Competências Técnicas
    st.markdown('<h2 class="subtitulo">Competências Técnicas</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**GIS e Processamento**")
        st.write("• ArcGIS Desktop/Pro • QGIS • Global Mapper")
        st.write("• Agisoft Metashape • Pix4D Mapper")
        
        st.markdown("**Programação**")
        st.write("• Python (dados geoespaciais) • R • JavaScript/HTML5")
    
    with col2:
        st.markdown("**Tecnologias Específicas**")
        st.write("• Drones/RPAS • GNSS • Sensoriamento Remoto")
        st.write("• Delft 3D • XBeach")


def pagina_portfolio():
    """Exibe o portfólio de projetos."""
    st.markdown('<h1 class="titulo-principal">Portfólio de Projetos</h1>', unsafe_allow_html=True)
    
    projetos = [
        {
            "titulo": "Plataforma WebGIS Integrada",
            "descricao": "Desenvolvimento de plataforma WebGIS com Python e Folium para análise geoespacial avançada.",
            "tecnologias": ["Python", "Folium", "Streamlit", "PostGIS"],
            "emoji": "🗺️"
        },
        {
            "titulo": "Automatização com Python",
            "descricao": "Scripts para automatização de tarefas, integração de APIs e processamento em massa de dados geoespaciais.",
            "tecnologias": ["Python", "GDAL", "Shapely", "APIs REST"],
            "emoji": "🤖"
        },
        {
            "titulo": "Dashboard Interativo",
            "descricao": "Dashboard com visualização de KPIs e métricas em tempo real usando Streamlit e Plotly.",
            "tecnologias": ["Streamlit", "Plotly", "Pandas", "Python"],
            "emoji": "📊"
        },
    ]
    
    for projeto in projetos:
        with st.expander(f"{projeto['emoji']} {projeto['titulo']}"):
            st.markdown(f"<p class='texto'>{projeto['descricao']}</p>", unsafe_allow_html=True)
            
            # Tags de tecnologias
            cols = st.columns(len(projeto['tecnologias']))
            for col, tech in zip(cols, projeto['tecnologias']):
                col.write(f"```\n{tech}\n```")


def pagina_contato():
    """Exibe página de contato com formulário."""
    st.markdown('<h1 class="titulo-principal">Contato</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="texto">
        Fique à vontade para entrar em contato comigo através dos seguintes canais:
    </p>
    """, unsafe_allow_html=True)
    
    # Informações de contato
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("📧 **E-mail Profissional**")
        st.write("tfholanda@gmail.com")
    
    with col2:
        st.markdown("📧 **E-mail Pessoal**")
        st.write("tiagofholanda@hotmail.com")
    
    # Redes e Plataformas
    st.markdown('<h2 class="subtitulo">Redes e Plataformas</h2>', unsafe_allow_html=True)
    st.markdown(render_social_links(), unsafe_allow_html=True)
    
    # Animação Lottie
    lottie_contact = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_SdQJtK.json")
    if lottie_contact:
        st_lottie(lottie_contact, height=300)
    
    # Formulário de contato
    st.markdown('<h2 class="subtitulo">Enviar uma Mensagem</h2>', unsafe_allow_html=True)
    
    with st.form(key='email_form'):
        st.markdown('<div class="formulario">', unsafe_allow_html=True)
        
        nome = st.text_input("👤 Nome completo", placeholder="Seu nome")
        email_remetente = st.text_input("📧 E-mail", placeholder="seu.email@exemplo.com")
        mensagem = st.text_area("💬 Mensagem", placeholder="Escreva sua mensagem aqui...", height=150)
        
        col1, col2 = st.columns([3, 1])
        with col2:
            submit_button = st.form_submit_button(label="📤 Enviar", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

        if submit_button:
            if not nome or not email_remetente or not mensagem:
                st.error("❌ Por favor, preencha todos os campos!")
            elif not validar_email(email_remetente):
                st.error("❌ Por favor, insira um endereço de e-mail válido.")
            else:
                with st.spinner('📤 Enviando mensagem...'):
                    time.sleep(1)  # Simular processamento
                    sucesso = enviar_email(nome, email_remetente, mensagem)
                    if sucesso:
                        st.success("✅ Mensagem enviada com sucesso! Obrigado pelo contato.")
