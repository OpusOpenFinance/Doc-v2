---
layout: default
title: Plataforma de Coleta de Métricas (PCM)
parent: "O que é o Open Finance Brasil"
nav_order: 3
has_children: false
lang: "pt-br"
---

# Plataforma de Coleta de Métricas (PCM)

A **Plataforma de Coleta de Métricas** é um requisito regulatório obrigatório do Open Finance Brasil. Toda instituição participante precisa reportar à estrutura de governança métricas sobre todas as chamadas de API que realiza ou recebe.

---

## O que é a PCM

A PCM é o sistema central da governança do Open Finance que consolida dados de uso do ecossistema. Cada instituição participante envia reportes periódicos contendo informações como:

- Endpoint acessado
- Data e hora do evento
- Resultado recebido (sucesso ou erro)
- Tempo de resposta

Esses dados permitem que a governança monitore a saúde do ecossistema, identifique problemas de disponibilidade e audite o cumprimento dos requisitos não funcionais.

---

## Quem precisa reportar

Todas as partes envolvidas em qualquer operação precisam enviar reportes — tanto a parte ativa quanto a passiva. Se um ITP inicia um pagamento numa Detentora, **ambas** precisam reportar a operação independentemente.

---

## Como a Plataforma Opus lida com a PCM

O envio de métricas à PCM é totalmente automático na Plataforma Opus Open Finance. O módulo **PCM Service** — obrigatório em todas as instalações — captura automaticamente todas as chamadas de API que passam pela plataforma e as envia dentro dos SLAs de tempestividade exigidos pelo regulador.

A instituição não precisa implementar nenhuma lógica própria de reporte. Uma vez configurado e inicializado, o PCM Service cuida de tudo — incluindo o armazenamento temporário de reportes em caso de indisponibilidade do sistema central.

Para detalhes de instalação e configuração do módulo, consulte [PCM Service — Configuração](../../opusTPP/configuracao/pcmService.html).

---

## Referência

- [PCM — documentação da plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PCM/OFB-PCM.html)
- [Manual de Integração da PCM — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/37945515/Manual+de+Integra+o)
