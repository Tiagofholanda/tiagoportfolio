# config.py

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações de e-mail
EMAIL_DESTINO = os.environ.get('EMAIL_DESTINO')
EMAIL_USUARIO = os.environ.get('EMAIL_USUARIO')
EMAIL_SENHA = os.environ.get('EMAIL_SENHA')

# Estilos CSS
CSS_STYLE = """
<style>
/* Seu CSS personalizado aqui */
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
"""

# Lista de links com ícones, labels e URLs
LINKS_PROFISSIONAIS = [
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/300/300221.png" width="40"/>', 'label': 'Google Acadêmico', 'url': 'https://scholar.google.com.br/citations?user=XLu_qAIAAAAJ&hl=pt-BR'},
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="40"/>', 'label': 'LinkedIn', 'url': 'https://www.linkedin.com/in/tiagofholanda'},
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="40"/>', 'label': 'GitHub', 'url': 'https://github.com/tiagofholanda'},
    {'icon': '<img src="https://lattes.cnpq.br/image/layout_set_logo?img_id=1311768&t=1729293336662" width="40"/>', 'label': 'Lattes', 'url': 'http://lattes.cnpq.br/K8557733H3'},
    {'icon': '<img src="https://help.researchgate.net/hc/theming_assets/01HZPWT1CS5WRP04ZJX0DM6135" width="40"/>', 'label': 'ResearchGate', 'url': 'https://www.researchgate.net/profile/Tiago_Holanda'},
    {'icon': '<img src="https://www.freepnglogos.com/uploads/publons-logo-transparent-png-30.png" width="80"/>', 'label': 'Publons', 'url': 'https://publons.com/researcher/3962699/tiago-holanda/'},
    {'icon': '<img src="https://upload.wikimedia.org/wikipedia/commons/0/06/ORCID_iD.svg" width="40"/>', 'label': 'ORCID', 'url': 'https://orcid.org/0000-0001-6898-5027'},
    {'icon': '<img src="https://cdn-icons-png.flaticon.com/512/3313/3313487.png" width="80"/>', 'label': 'Scopus', 'url': 'https://www.scopus.com/authid/detail.uri?authorId=57376293300'},
]

# Animações Lottie URLs
LOTTIE_ANIMATIONS = {
    'home': "https://assets1.lottiefiles.com/packages/lf20_3vbOcw.json",
    'contato': "https://assets2.lottiefiles.com/packages/lf20_SdQJtK.json",
}
