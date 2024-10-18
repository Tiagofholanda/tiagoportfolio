import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# Função para carregar animações Lottie
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Carregar animação Lottie
lottie_animation = load_lottie_url("https://assets7.lottiefiles.com/private_files/lf30_dxgf5fxz.json")

# Configuração da página
st.set_page_config(page_title="Portfólio de Tiago Holanda", page_icon=":earth_americas:", layout="wide")

# Adicionar estilos CSS personalizados
st.markdown("""
    <style>
    /* Importando fonte Montserrat */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
    }

    /* Estilo para títulos */
    .titulo-principal {
        font-size:50px;
        color:#1F4E79;
        text-align:center;
        font-weight:bold;
    }
    
    /* Estilo para subtítulos */
    .subtitulo {
        font-size:30px;
        color:#1F4E79;
        margin-top:20px;
        margin-bottom:10px;
    }
    
    /* Estilo para texto */
    .texto {
        font-size:18px;
        color:#000000;
        text-align:justify;
    }

    /* Estilo para links */
    a, a:hover, a:visited {
        color:#1F4E79;
        text-decoration:none;
    }

    /* Estilo para formulário de contato */
    .formulario {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    }

    /* Estilo para animações Lottie */
    .lottie {
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Função para Currículo
def mostrar_curriculo():
    st.markdown('<h1 class="titulo-principal">Currículo Profissional e Acadêmico</h1>', unsafe_allow_html=True)
    
    # Layout com imagem e resumo
    col1, col2 = st.columns([1, 2])
    with col1:
        # Carregar imagem a partir da URL
        st.image("https://avatars.githubusercontent.com/u/111590174?v=4", width=250)
    with col2:
        st.markdown('<h2 class="subtitulo">Resumo Profissional</h2>', unsafe_allow_html=True)
        st.markdown("""
        <p class="texto">
        Profissional com sólida experiência em Geografia e Ciências Geodésicas, atuando como especialista em **Geoprocessamento** e **Análise de Dados Geoespaciais**. Doutorando em Geografia pela **Universidade Federal Fluminense (UFF)**, com foco em aplicações avançadas de **GIS** e **tecnologias de geoinformação**. Possuo histórico comprovado no desenvolvimento de soluções **WebGIS**, integração de sistemas **CRM** e automatização de processos utilizando **Python**, **PyQt5** e **Streamlit**. Minha trajetória acadêmica e profissional reflete um compromisso contínuo com a inovação tecnológica e a excelência na análise espacial.
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

# Função para Portfólio
def mostrar_portfolio():
    st.markdown('<h1 class="titulo-principal">Portfólio de Projetos</h1>', unsafe_allow_html=True)
    st.markdown('<p class="texto">Abaixo estão alguns dos projetos mais relevantes que desenvolvi ao longo da minha carreira:</p>', unsafe_allow_html=True)
    
    # Projetos
    projetos = [
        {
            "titulo": "Desenvolvimento de Plataforma WebGIS Integrada",
            "descricao": "Criação de uma plataforma WebGIS utilizando Python e Folium para análise geoespacial avançada, integrada com sistemas CRM para gerenciamento de clientes e vendas.",
            "imagem": "data/projeto1.png"
        },
        {
            "titulo": "Automatização de Processos com Python",
            "descricao": "Desenvolvimento de scripts para automatização de tarefas repetitivas, integração de APIs e processamento em massa de dados geoespaciais.",
            "imagem": "data/projeto2.png"
        },
        {
            "titulo": "Dashboard Interativo para Análise de Desempenho",
            "descricao": "Criação de dashboards interativos utilizando Streamlit e Plotly para visualização de KPIs e métricas de desempenho em tempo real.",
            "imagem": "data/projeto3.png"
        }
    ]
    
    # Exibir projetos em cards
    for projeto in projetos:
        st.markdown(f"""
        <h2 class="subtitulo">{projeto['titulo']}</h2>
        <p class="texto">{projeto['descricao']}</p>
        """, unsafe_allow_html=True)
        # Se tiver imagens dos projetos, descomente a linha abaixo e certifique-se de que o caminho está correto
        # image = Image.open(projeto['imagem'])
        # st.image(image, use_column_width=True)
        st.markdown("<hr>", unsafe_allow_html=True)

# Função para Contato
def mostrar_contato():
    st.markdown('<h1 class="titulo-principal">Contato</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="texto">Fique à vontade para entrar em contato comigo através dos seguintes canais:</p>
    """, unsafe_allow_html=True)
    
    # Informações de contato
    st.markdown("""
    <ul class="texto">
        <li><strong>WhatsApp:</strong> (81) 99667-4681</li>
        <li><strong>E-mail:</strong> tfholanda@gmail.com / tiagofholanda@hotmail.com</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Formulário de contato
    st.markdown('<h2 class="subtitulo">Enviar uma Mensagem</h2>', unsafe_allow_html=True)
    st.markdown('<div class="formulario">', unsafe_allow_html=True)
    with st.form(key='email_form'):
        nome = st.text_input("Nome")
        email = st.text_input("E-mail")
        mensagem = st.text_area("Mensagem")
        submit_button = st.form_submit_button(label="Enviar")
    st.markdown('</div>', unsafe_allow_html=True)

    if submit_button:
        st.success("Mensagem enviada com sucesso!")
    
st.markdown('<h2 class="subtitulo">Redes e Perfis</h2>', unsafe_allow_html=True)
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)

with col1:
    st.markdown('📚 [Google Acadêmico](https://scholar.google.com.br/citations?user=XLu_qAIAAAAJ&hl=pt-BR)')
with col2:
    st.markdown('<img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="20"/> [LinkedIn](https://www.linkedin.com/in/tiagofholanda)', unsafe_allow_html=True)
with col3:
    st.markdown('🐱 [GitHub](https://github.com/tiagofholanda)')
with col4:
    st.markdown('📄 [Lattes](http://lattes.cnpq.br/K8557733H3)')
with col5:
    st.markdown('🧑‍🔬 [ResearchGate](https://www.researchgate.net/profile/Tiago_Holanda)')
with col6:
    st.markdown('🎓 [Researchers](https://publons.com/researcher/3962699/tiago-holanda/)')
with col7:
    st.markdown('🌐 [ORCID](https://orcid.org/0000-0001-6898-5027)')
with col8:
    st.markdown('🔬 [Scopus](https://www.scopus.com/authid/detail.uri?authorId=57376293300)')


# Navegação usando barra lateral
st.sidebar.title("Navegação")
selection = st.sidebar.radio("Ir para", ["Início", "Currículo", "Portfólio", "Contato"])

# Carregar a página selecionada
if selection == "Início":
    st.markdown('<h1 class="titulo-principal">Bem-vindo ao meu Portfólio!</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="texto">
    Sou **Tiago Holanda**, especialista em Geoprocessamento e Análise de Dados Geoespaciais. Este portfólio apresenta minha trajetória profissional, projetos desenvolvidos e formas de contato. Sinta-se à vontade para explorar e conhecer mais sobre meu trabalho.
    </p>
    """, unsafe_allow_html=True)
    st.image("https://avatars.githubusercontent.com/u/111590174?v=4", width=300)

    # Animação Lottie
    st.markdown('<div class="lottie">', unsafe_allow_html=True)
    st_lottie(lottie_animation, height=300)
    st.markdown('</div>', unsafe_allow_html=True)

elif selection == "Currículo":
    mostrar_curriculo()

elif selection == "Portfólio":
    mostrar_portfolio()

elif selection == "Contato":
    mostrar_contato()
