import streamlit as st
import os
import json
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="TechDesk AI - Enterprise IT Support",
    page_icon="💻",
    layout="wide"
)

st.title("💻 TechDesk AI — Assistente Inteligente de Suporte Corporativo")
st.markdown("---")

# Carregar dados locais (JSON / CSV / TXT)
@st.cache_data
def carregar_dados_sistema():
    dados = {}
    try:
        if os.path.exists("data/perfil.json"):
            with open("data/perfil.json", "r", encoding="utf-8") as f:
                dados["perfil"] = json.load(f)
        if os.path.exists("data/produtos_financeiros.json"):
            with open("data/produtos_financeiros.json", "r", encoding="utf-8") as f:
                dados["produtos"] = json.load(f)
        if os.path.exists("data/transacoes.csv"):
            dados["transacoes"] = pd.read_csv("data/transacoes.csv")
        if os.path.exists("data/base-conhecimento.txt"):
            with open("data/base-conhecimento.txt", "r", encoding="utf-8") as f:
                dados["base_conhecimento"] = f.read()
    except Exception as e:
        st.error(f"Erro ao carregar dados locais: {e}")
    return dados

dados_app = carregar_dados_sistema()

# Sidebar de controle e identificação do usuário
with st.sidebar:
    st.header("⚙️ Painel de Controle TI")
    
    nome_usuario_input = st.text_input("Identificação do Colaborador:", value="Amanda Souza")
    
    if nome_usuario_input:
        st.success(f"Sessão ativa para: **{nome_usuario_input}**")
    
    st.markdown("---")
    st.subheader("📊 Métricas do Servidor")
    if "transacoes" in dados_app:
        st.metric(label="Chamados Registrados", value=len(dados_app["transacoes"]))
    if "produtos" in dados_app:
        st.metric(label="Softwares Monitorados", value=len(dados_app["produtos"].get("software_suportado", [])))
    
    st.markdown("---")
    filtro_rapido = st.selectbox(
        "Acesso Rápido a Manuais:",
        ["Selecione...", "Política de Senhas", "Guia de VPN", "Impressoras", "Chamados Tier 2"]
    )

# Área de Chat Inteligente
st.subheader("💬 Console de Atendimento Inteligente")

if "mensagens" not in st.session_state or st.session_state.get("ultimo_usuario") != nome_usuario_input:
    st.session_state.ultimo_usuario = nome_usuario_input
    st.session_state.mensagens = [
        {"role": "assistant", "content": f"Olá, **{nome_usuario_input}**! Sou o TechDesk AI. Como posso auxiliar nos procedimentos de infraestrutura ou suporte de TI hoje?"}
    ]

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta_usuario = st.chat_input("Digite sua dúvida técnica (ex: preciso de acesso a vpn, redefinir senha)...")

if filtro_rapido != "Selecione..." and not pergunta_usuario:
    if filtro_rapido == "Política de Senhas":
        pergunta_usuario = "senha"
    elif filtro_rapido == "Guia de VPN":
        pergunta_usuario = "vpn"
    elif filtro_rapido == "Impressoras":
        pergunta_usuario = "impressora"
    elif filtro_rapido == "Chamados Tier 2":
        pergunta_usuario = "chamado"

if pergunta_usuario:
    st.session_state.mensagens.append({"role": "user", "content": pergunta_usuario})
    with st.chat_message("user"):
        st.markdown(pergunta_usuario)

    with st.chat_message("assistant"):
        with st.spinner("Analisando base de conhecimento corporativa..."):
            p_lower = pergunta_usuario.lower()
            
            # Motor lógico integrado com as diretrizes do arquivo base-conhecimento.txt
            if any(term in p_lower for term in ["senha", "acesso", "login", "trocar", "bloqueada"]):
                resposta = (
                    f"📋 **[POLÍTICA DE SEGURANÇA E ACESSO]** {nome_usuario_input}, segue a diretriz oficial:\n\n"
                    "- **Requisitos:** Mínimo de 12 caracteres (maiúsculas, minúsculas, números e símbolos especiais).\n"
                    "- **Expiração:** Troca obrigatória a cada 90 dias.\n"
                    "- **Portal de Autoatendimento:** `https://portal.techcorp.internal/reset-password` (com MFA do Microsoft Authenticator).\n"
                    "- **Bloqueio:** Após 3 erros consecutivos, a conta bloqueia por 30 minutos."
                )
            elif any(term in p_lower for term in ["vpn", "globalprotect", "conexão", "rede remota", "certificado"]):
                resposta = (
                    f"🌐 **[INFRAESTRUTURA DE REDE E VPN]** {nome_usuario_input}, instruções oficiais:\n\n"
                    "- **Cliente Oficial:** GlobalProtect Palo Alto Networks (v6.0+).\n"
                    "- **Gateway:** `vpn.techcorp.internal` (via SSO + Azure AD + MFA).\n"
                    "- **Erros comuns:** Se houver erro de 'Certificado Inválido', sincronize a hora via NTP corporativo. Problemas de timeout indicam bloqueio nas portas UDP 4500 e 500."
                )
            elif any(term in p_lower for term in ["impressora", "imprimir", "spooler", "papel", "fila"]):
                resposta = (
                    f"🖨️ **[PARQUE DE IMPRESSÃO]** {nome_usuario_input}, diretrizes:\n\n"
                    "- **Rede Wi-Fi:** Conecte-se obrigatoriamente à `TechCorp-Office` (5GHz).\n"
                    "- **Correção de Spooler:** Abra o PowerShell como Administrador e execute:\n"
                    "```powershell\nRestart-Service -Name Spooler -Force\n```"
                )
            elif any(term in p_lower for term in ["chamado", "ticket", "suporte", "jira", "tier"]):
                resposta = (
                    f"🎫 **[GESTÃO DE CHAMADOS E SLA]** {nome_usuario_input}, canais e prioridades:\n\n"
                    "- **Portal de Chamados:** `https://jira.techcorp.internal/servicedesk`\n"
                    "- **SLA Crítico (Inatividade total):** Até 1 hora.\n"
                    "- **SLA Padrão:** Até 8 horas úteis.\n\n"
                    "**Seus tickets locais registrados:**\n"
                )
                if "transacoes" in dados_app:
                    df = dados_app["transacoes"]
                    for _, row in df.iterrows():
                        resposta += f"- **{row['id_chamado']}** ({row['categoria']}): *Status:* {row['status']}\n"
                else:
                    resposta += "Nenhum chamado pendente registrado na base local."
            else:
                resposta = (
                    f"⚠️ {nome_usuario_input}, não encontrei diretrizes exatas para '{pergunta_usuario}' na base local.\n\n"
                    "Por favor, abra um ticket no Jira Service Desk corporativo (`https://jira.techcorp.internal/servicedesk`) ou contate `suporte.ti@techcorp.internal` (SLA de até 8 horas úteis)."
                )
            
            st.markdown(resposta)
            st.session_state.mensagens.append({"role": "assistant", "content": resposta})

# Auditoria de Dados Locais e Base de Conhecimento
with st.expander("🔍 Visualizar Auditoria de Dados Locais (JSON / CSV / TXT)"):
    tab1, tab2, tab3 = st.tabs(["Base de Conhecimento", "Softwares Monitorados", "Logs de Chamados"])
    with tab1:
        if "base_conhecimento" in dados_app:
            st.text_area("Conteúdo do Arquivo base-conhecimento.txt", dados_app["base_conhecimento"], height=200)
    with tab2:
        if "produtos" in dados_app:
            st.json(dados_app["produtos"])
    with tab3:
        if "transacoes" in dados_app:
            st.dataframe(dados_app["transacoes"])