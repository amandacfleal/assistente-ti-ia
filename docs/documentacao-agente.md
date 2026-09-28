# Documentação Oficial de Arquitetura: TechDesk AI

## 1. Visão Geral do Projeto
O **TechDesk AI** é um agente inteligente conceitual projetado para atuar na primeira linha de atendimento (Tier 1) de suporte corporativo de TI. O objetivo principal é mitigar a saturação da equipe de engenharia humana através da automação de respostas para dúvidas frequentes de infraestrutura, acessos e políticas de segurança.

## 2. Arquitetura do Sistema
- **Camada de Apresentação:** Interface CLI em Python orientada a interações em tempo real.
- **Camada de Dados:** Repositório local em texto estruturado (`data/base-conhecimento.txt`) simulando uma Vector Database ou Knowledge Base RAG (Retrieval-Augmented Generation).
- **Motor de Decisão:** Algoritmo de filtragem e correspondência semântica baseada em termos-chave para evitar alucinações e garantir o alinhamento com as normas da empresa.

## 3. Diretrizes de Comportamento e Governança
- **Zero-Hallucination Policy:** O agente está estritamente proibido de inventar links, políticas de segurança ou comandos de sistema que não estejam explicitamente declarados na base de conhecimento.
- **Escalonamento Automático:** Caso a consulta do usuário fuja do escopo pré-definido, o sistema direciona automaticamente para os canais oficiais de abertura de tickets (Jira / E-mail).