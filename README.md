# 💻 TechDesk AI — Assistente Inteligente de Suporte Corporativo

[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![Status](https://img.shields.io/badge/Status-Concluído-success.svg)]()

---

## 📋 Informações do Desafio & Bootcamp

* **Bootcamp:** Bootcamp Bradesco - GenAI, Dados & Cyber ​​, da DIO
* **Nome do Desafio:** Construindo um Assistente de IA Corporativo com Bases de Conhecimento e Python (TechDesk AI)
* **Objetivo do Projeto:** Desenvolver e estruturar uma aplicação sênior de atendimento automatizado de TI (*Tier 1*), aplicando governança anti-alucinação, persistência de dados locais (JSON/CSV/TXT), identificação dinâmica de colaboradores e uma interface web moderna em Streamlit para mitigar a sobrecarga de equipes técnicas.

---

## 🏗️ Arquitetura do Sistema

O projeto adota uma arquitetura modular inspirada em sistemas corporativos modernos:
- **Camada de Apresentação:** Interface web interativa construída em **Streamlit**, oferecendo painel lateral de controle, métricas em tempo real e console de chat.
- **Camada de Dados (RAG Local):** Repositório local estruturado contendo bases de conhecimento detalhadas (`base-conhecimento.txt`), perfis corporativos (`perfil.json`), catálogo de softwares (`produtos_financeiros.json`) e logs de chamados (`transacoes.csv`).
- **Motor de Decisão e Governança:** Algoritmo de correspondência semântica e filtragem por intenção natural para garantir a aderência estricta às políticas internas (*Zero-Hallucination Policy*).

---

## 📁 Estrutura do Repositório

```text
assistente_ti_ia/
│
├── data/
│   ├── base-conhecimento.txt       # Base textual de diretrizes de TI (v2.4)
│   ├── historico_atendimento.csv   # Histórico de interações simuladas
│   ├── perfil.json                 # Metadados de cargos e permissões do usuário
│   ├── produtos_financeiros.json   # Mapeamento de softwares e ferramentas monitoradas
│   └── transacoes.csv              # Logs e status de chamados abertos
│
├── docs/
│   └── documentacao-agente.md      # Documentação técnica oficial e governança
│
├── src/
│   └── app.py                      # Aplicação web principal em Streamlit
│
├── .gitignore                      # Arquivos ignorados pelo controle de versão
├── README.md                       # Documentação principal do projeto
└── requirements.txt                # Dependências e bibliotecas do projeto