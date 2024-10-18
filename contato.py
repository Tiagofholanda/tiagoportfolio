import streamlit as st

# Título do site
st.title("Contato")

# Barra lateral para navegação
st.sidebar.title("Navegação")
selection = st.sidebar.radio("Ir para", ["Contato"])

# Seção de Contato
if selection == "Contato":
    st.header("Contato")
    st.write("""
    - **WhatsApp**: (81) 99667-4681
    - **E-mails**: tfholanda@gmail.com / tiagofholanda@hotmail.com
    """)
    st.markdown("[Lattes](http://buscatextual.cnpq.br/buscatextual/visualizacv.do?id=K8557733H3)")
    st.markdown("[ResearchGate](https://www.researchgate.net/profile/Tiago_Holanda)")
    st.markdown("[Researchers](https://publons.com/researcher/3962699/tiago-holanda/)")
    st.markdown("[ORCID](https://orcid.org/0000-0001-6898-5027)")
    st.markdown("[Scopus](https://www.scopus.com/authid/detail.uri?authorId=57376293300)")
