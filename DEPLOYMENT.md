# Guia de Deployment e Manutenção do Portfólio

## 🚀 Deployment no Streamlit Cloud

Para manter seu site sempre ativo sem hibernação, siga estes passos:

### 1. **Deploy no Streamlit Cloud**
- Acesse [streamlit.io](https://streamlit.io)
- Faça login com sua conta GitHub
- Clique em "New app"
- Selecione seu repositório `tiagoportfolio`
- Branch: `main`
- Main file path: `streamlit_app.py`
- Clique em "Deploy"

### 2. **Manter o Site Sempre Ativo**

O repositório agora possui um workflow automático (`.github/workflows/keep-alive.yml`) que faz ping no seu site a cada 6 horas, mantendo-o ativo.

**Não é necessário configurar nada!** O GitHub Actions cuida disso automaticamente.

### 3. **Variáveis de Ambiente (.env)**

Crie um arquivo `.env` na raiz do projeto com:

```env
EMAIL_DESTINO=seu-email@gmail.com
EMAIL_USUARIO=seu-email@gmail.com
EMAIL_SENHA=sua-senha-app-google
```

**Para Gmail:**
1. Ative a Autenticação em Dois Fatores
2. Vá para: https://myaccount.google.com/apppasswords
3. Gere uma senha de app
4. Cole no `.env`

### 4. **Adicionar Variáveis no Streamlit Cloud**

No painel do Streamlit Cloud:
1. Vá para "Settings" da sua aplicação
2. Clique em "Secrets"
3. Adicione as variáveis:

```
EMAIL_DESTINO = seu-email@gmail.com
EMAIL_USUARIO = seu-email@gmail.com
EMAIL_SENHA = sua-senha-app-google
```

## 📋 Mudanças Realizadas

### 1. **Anti-Hibernação**
- ✅ Criado workflow GitHub Actions que faz ping a cada 6 horas
- ✅ Arquivo: `.github/workflows/keep-alive.yml`

### 2. **Novas Experiências Adicionadas**
- ✅ **UFABC** - Tutor e Professor da Especialização (10/07/2023 - 01/08/2025)
- ✅ **DEVGIS** - Desenvolvedor WebGIS / Especialista (10/02/2024 - 01/10/2025)
- ✅ **AERO Engenharia** - Especialista de Geoprocessamento (10/02/2025 - 01/10/2025)
- ✅ **NMC Integrativa** - Atualizada com atuação detalhada

### 3. **Correções de Erros**
- ✅ Removido import faltante de `time`
- ✅ Removidos placeholder images que causavam ERR_NAME_NOT_RESOLVED
- ✅ Melhorado CSS responsivo
- ✅ Configuração do Streamlit para modo headless

### 4. **Melhorias no Requirements.txt**
- ✅ Versions fixadas para melhor compatibilidade
- ✅ Adicionado `watchdog` para auto-reload
- ✅ Estrutura: `pandas>=2.0.0`, `streamlit>=1.28.0`, etc.

## 🔧 Configurações do Streamlit

O arquivo `.streamlit/config.toml` contém:
- Modo headless ativado
- Auto-save habilitado
- XSRF protection ativado
- Logger em modo error

## 📝 Notas Importantes

1. **GitHub Actions**
   - O workflow roda a cada 6 horas
   - Não requer configuração manual
   - Mantém seu site ativo indefinidamente

2. **Email**
   - Sempre use senhas de app, não a senha principal
   - Gmail requer verificação em 2 fatores

3. **Certificado SSL**
   - Streamlit Cloud fornece HTTPS gratuito
   - Seu site está seguro automaticamente

## 🐛 Troubleshooting

**Site ainda está hibernando?**
- Verifi que o workflow está ativado em `.github/workflows/`
- Confirme que seu repositório é público
- Aguarde 6 horas para o próximo ping automático

**Formulário de email não funciona?**
- Verifique as variáveis de ambiente no Streamlit Cloud
- Teste a senha de app no Gmail
- Ative "Acesso de apps menos seguros" se necessário

## 📚 Recursos Úteis

- [Streamlit Cloud Docs](https://docs.streamlit.io/deploy/streamlit-cloud)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Gmail App Passwords](https://support.google.com/accounts/answer/185833)

---

**Última atualização:** 29 de Novembro, 2025
**Status:** ✅ Ativo e Otimizado
