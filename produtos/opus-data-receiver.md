---
layout: default
title: Opus Data Receiver
parent: Produtos
nav_order: 3
has_children: false
lang: "pt-br"
---

# Opus Data Receiver

O **Opus Data Receiver (ODR)** é um módulo complementar ao OpusTPP, voltado para instituições que precisam manter os dados financeiros dos seus clientes sempre atualizados — sem gerir manualmente consultas periódicas e consentimentos individuais.

---

## O problema que resolve

Quando uma Receptora de Dados obtém consentimento de um cliente para acessar seus dados em uma Transmissora, ela pode consultar esses dados durante toda a vigência do consentimento. Mas cada consulta precisa ser feita ativa e individualmente — e os dados retornam refletindo o momento da consulta, não um histórico contínuo.

Para instituições que precisam de dados sempre atualizados de muitos clientes em muitas instituições — como plataformas de gestão financeira pessoal ou modelos de análise de crédito — gerenciar isso diretamente é complexo, custoso e sujeito aos limites regulatórios de frequência de consultas.

O ODR resolve esse problema: a instituição cria os consentimentos e o ODR cuida de tudo o mais — quando buscar, como respeitar os limites do regulador, como consolidar dados de múltiplas fontes e como notificar eventos relevantes.

---

## O que o ODR faz

### Atualização automática e periódica

Utiliza um Scheduler interno para atualizar os dados dos clientes periodicamente, respeitando os limites operacionais definidos pela regulação do Open Finance Brasil. A frequência de atualização é gerenciada automaticamente — a instituição não precisa se preocupar com throttling ou limites por consentimento.

### Consolidação multi-instituição

Quando um cliente tem consentimentos em múltiplas Transmissoras, o ODR consolida todos os dados numa visão unificada. A Customer Data API retorna um extrato centralizado de todas as transações e posições do cliente nas diferentes instituições — como se fossem dados de uma única fonte.

### Fila de eventos

O ODR dispara eventos automaticamente quando algo relevante acontece. Os tipos de evento incluem:

**Eventos técnicos:**
- Consentimento expirado
- Consentimento revogado pelo usuário
- Falha na atualização de dados

**Eventos de negócio (configuráveis):**
- Novo contrato de empréstimo detectado em outra instituição
- Alteração significativa de saldo
- Outros padrões configuráveis pela instituição

Esses eventos permitem integração com sistemas internos (CRM, análise de crédito, notificações push) e podem disparar ações automatizadas — como incentivar o cliente a renovar um consentimento expirado.

---

## Arquitetura

O ODR é composto por dois serviços independentes instalados via Helm Chart:

**ODR-Core**: expõe a Customer Data API para consulta dos dados consolidados e processa as notificações de atualização. Depende do OpusTPP (oofc-core) para acessar os dados das Transmissoras.

**ODR-Scheduler**: gerencia os agendamentos de atualização de dados e executa as consultas periódicas respeitando os limites regulatórios. Comunica-se com o ODR-Core via Dapr (pub/sub interno).

A comunicação entre ODR-Core e ODR-Scheduler, assim como o envio de eventos externos aos notificadores, é feita via [Dapr](https://dapr.io/).

---

## Relação com o OpusTPP

O ODR é um módulo complementar ao OpusTPP — não funciona de forma independente. Ele usa o módulo de Receptor de Dados do OpusTPP para fazer as consultas às Transmissoras e precisa do oofc-pcm para os reportes à PCM.

A instituição que usa o ODR não precisa gerenciar consultas individuais às APIs das Transmissoras: ela cria os consentimentos via OpusTPP e consulta os dados consolidados via Customer Data API do ODR.

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Detalhar aqui os endpoints da Customer Data API: quais recursos consolida, formato da resposta, como filtrar por consentimento ou por usuário.

---

## Casos de uso

- **Plataforma de gestão financeira pessoal (PFM)**: o cliente conecta contas de diferentes bancos e vê um resumo unificado de saldo, transações e investimentos — atualizado automaticamente, sem precisar acionar a atualização manualmente.
- **Motor de análise de crédito**: a instituição mantém uma visão contínua e atualizada do perfil financeiro dos clientes para decisões de crédito com menor latência.
- **Alertas e notificações automáticas**: quando um novo contrato de empréstimo é detectado em outra instituição, a plataforma pode disparar automaticamente uma oferta de portabilidade de crédito.
- **Integração com CRM**: eventos de expiração de consentimento alimentam o CRM com gatilhos para campanhas de reengajamento.

---

## Referências

- [Instalação e configuração do ODR](../opusTPP/configuracao/index.html)
- [OpusTPP — Receptor de Dados](opustpp.html#receptor-de-dados-cadastrais-e-transacionais)
- [Checklist de implantação — Receptor de Dados](../implantacao/integracao/receptor/checklist.html)
