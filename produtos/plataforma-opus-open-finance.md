---
layout: default
title: Plataforma Opus Open Finance
parent: Produtos
nav_order: 1
has_children: false
lang: "pt-br"
---

# Plataforma Opus Open Finance

A **Plataforma Opus Open Finance** é a solução para instituições financeiras que atuam como **Detentoras de Conta**, **Transmissoras de Dados** ou ambas no ecossistema do Open Finance Brasil.

Ela funciona como um middleware entre o ecossistema regulatório e os sistemas de retaguarda da instituição: recebe as requisições dos participantes do Open Finance, valida segurança e conformidade, e aciona os sistemas internos da instituição através de conectores — sem exigir modificações nos sistemas existentes.

---

## O que a plataforma faz

### Gestão de consentimentos

Gerencia o ciclo de vida completo dos consentimentos criados na interação com Iniciadores de Pagamento e Receptores de Dados — criação, revogação e controle de expiração. Também controla os consentimentos obtidos pela própria instituição.

Expõe uma API independente que permite à instituição criar aplicações internas para consulta, exibição e revogação de consentimentos nos canais de atendimento ao cliente. A revogação de consentimentos pelos clientes é uma exigência das normas regulatórias do Open Finance Brasil.

### Servidor de autorização (FAPI-BR)

Implementa os perfis obrigatórios de segurança exigidos pelo Open Finance Brasil, incluindo o padrão FAPI-BR (Financial-grade API), DCR (Dynamic Client Registration) e DCM (Dynamic Client Management). É o componente responsável pelo registro dos TPPs que acessam as APIs da instituição, incluindo a validação de certificados criptográficos utilizados nas requisições subsequentes. Devidamente certificado pela OpenID Foundation.

### Módulo Detentor de Conta

Trata os pedidos de pagamento recebidos de Iniciadores de Transação de Pagamento. O fluxo envolve a criação de consentimento após autenticação e confirmação pelo cliente, a validação do consentimento enviado pelo iniciador, e o tratamento do pagamento até sua efetivação — com webhook de confirmação. Integra-se ao sistema de Pix da instituição via conector.

Funcionalidades disponíveis atualmente: Pix imediato, Pix agendado, recorrência de pagamentos agendados e transferências inteligentes (sweeping accounts). Funcionalidades previstas: pagamentos em lote, pagamento sem redirecionamento, Pix Automático e Pix por aproximação.

### Módulo Transmissor de Dados

Trata os pedidos de compartilhamento de dados cadastrais e transacionais dos clientes. Para cada requisição recebida, valida a instituição requisitante (incluindo assinaturas criptográficas), a validade do consentimento e se as permissões incluem os dados solicitados. Os conectores com os sistemas de retaguarda só são acionados quando todas as validações são aprovadas.

Dados compartilháveis: dados cadastrais (PF e PJ), contas, cartões de crédito, operações de crédito (empréstimos, financiamentos, adiantamentos, direitos creditórios), investimentos (renda fixa bancária, renda fixa crédito, renda variável, fundos, tesouro direto) e câmbio.

### Gestão multimarcas

Para instituições com múltiplas marcas, a plataforma suporta nativamente a convivência de diferentes marcas em uma mesma instalação Kubernetes, com compartilhamento de microsserviços essenciais — gerando economia de infraestrutura e menor complexidade operacional.

### Plataforma de Coleta de Métricas (PCM)

Componente obrigatório que coleta e envia automaticamente os reportes de uso para a estrutura de governança do Open Finance Brasil. Executa de forma transparente, agrupando reportes para minimizar impacto de desempenho e gerenciando indisponibilidades temporárias da PCM central.

### Conectores (camada de integração)

A integração com os sistemas de retaguarda é feita através de conectores — adaptadores que isolam a complexidade da plataforma e garantem padronização. Os conectores recebem objetos no formato interno da plataforma, fazem as chamadas necessárias aos sistemas legados e retornam respostas no formato esperado. Desenvolvidos caso a caso, permitem que a plataforma opere sem necessidade de modificar os sistemas existentes.

### Status e health check

Implementa as APIs regulatórias de status dos serviços e contabiliza todas as chamadas para os cálculos de disponibilidade exigidos pela governança. Informa sobre a disponibilidade momentânea de cada endpoint regulatório: disponível, com falha parcial, em manutenção programada ou indisponível.

### Fila de eventos

Gera notificações para eventos técnicos e de negócio: erros HTTP, revogação de consentimentos, novos registros DCR, etc. As notificações são organizadas por tópicos e podem ser assinadas por aplicações externas (CRM, análise de crédito, etc.). Suporta qualquer plataforma de mensageria compatível com Dapr.

### Portal Backoffice

Interface para operações administrativas: cadastro de indisponibilidades programadas (para cumprimento dos SLAs regulatórios), dashboard de falhas detectadas automaticamente, e autenticação via Federation com o Identity Provider da instituição.

---

## Ferramentas incluídas

### Tela de Handoff White-label

Para instituições app-only (sem Internet Banking), implementa o fluxo de handoff obrigatório: exibe um QR Code para usuários em desktop que pode ser lido com qualquer app, direcionando o usuário para o app da instituição. Customizável com imagens, cores, textos e links para as lojas de aplicativos.

### Aplicativo móvel com telas de autorização

Exemplos de design e código-fonte das telas obrigatórias da jornada de consentimento, com integração completa à plataforma — ponto de partida para o desenvolvimento das telas da instituição.

### Connector Tester

Simula chamadas do ecossistema Open Finance e permite que os conectores desenvolvidos pela instituição sejam exercitados e testados de forma isolada, antes de conectar ao ambiente real.

### TPP Quick Simulator

Implementa as funcionalidades de um ITP ou Receptor de Dados e executa os fluxos completos de criação e utilização de consentimentos. Útil para testes, diagnóstico e demonstração de funcionalidades de Detentoras e Transmissoras.

---

## Arquitetura

A plataforma é baseada em microsserviços, projetada para Kubernetes com suporte a escalabilidade horizontal automática (autoscaling por CPU e memória em todos os módulos). Distribuída via Helm Charts. Opera em produção em ambientes Kubernetes gerenciados (Google GKE, AWS EKS, Azure AKS) e em clusters gerenciados manualmente.

Inclui suporte nativo a Dapr, Grafana e Prometheus. Para gestão de logs, integra-se com Elastic Stack, Datadog, Loki ou qualquer ferramenta compatível com Kubernetes. Todos os dados em repouso são criptografados; dados sensíveis de clientes são anonimizados dinamicamente nos logs, em conformidade com a LGPD.

---

## Referências

- [Arquitetura da Plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Arquitetura/OOF-Arquitetura.html)
- [Integração da Plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/OOF-Integra%C3%A7%C3%A3o.html)
- [Implantação](../implantacao/integracao/detentor-transmissor/checklist.html)
