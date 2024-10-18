import streamlit as st

# Título do site
st.title("Currículo Profissional e Acadêmico")

# Barra lateral para navegação
st.sidebar.title("Navegação")
selection = st.sidebar.radio("Ir para", ["Currículo Profissional", "Currículo Acadêmico"])

# Seção de Currículo Profissional
if selection == "Currículo Profissional":
    st.header("Currículo Profissional")
    st.write("""
    - **Doutorando em Geografia** - Universidade Federal Fluminense (UFF)
    - **Mestre em Ciências Geodésicas e Tecnologias da Geoinformação** - Universidade Federal de Pernambuco (UFPE)
    - **Licenciatura em Geografia** - Universidade Federal de Pernambuco (UFPE)
    - **Especialização em Georreferenciamento**
    - **Técnico em Geoprocessamento e Agrimensura**
    - **Experiência Profissional**:
      - Desenvolvimento de soluções WebGIS e análise de dados.
      - Integração de mapas com sistemas de CRM.
      - Automatização de processos utilizando Python, PyQt5, e Streamlit.
    """)

# Seção de Currículo Acadêmico
elif selection == "Currículo Acadêmico":
    st.header("Currículo Acadêmico")
    st.write("""
    - **Doutorando em Geografia** - Universidade Federal Fluminense (UFF)
    - **Mestre em Ciências Geodésicas e Tecnologias da Geoinformação** - Universidade Federal de Pernambuco (UFPE)
    - **Licenciatura em Geografia** - Universidade Federal de Pernambuco (UFPE)
    - **Especialização em Georreferenciamento**
    - **Técnico em Geoprocessamento e Agrimensura**
    """)
