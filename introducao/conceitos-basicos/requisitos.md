---
layout: default
title: Requisitos (limites)
parent: "O que é o Open Finance Brasil"
nav_order: 4
has_children: false
lang: "pt-br"
---

# Requisitos Não Funcionais (Limites)

O Open Finance Brasil define requisitos não funcionais obrigatórios que toda instituição participante precisa cumprir. Eles estabelecem os níveis mínimos de disponibilidade, desempenho e capacidade que as APIs regulatórias precisam atender.

---

## Disponibilidade

As APIs regulatórias precisam estar disponíveis:

- **95%** do tempo a cada período de 24 horas
- **99,5%** do tempo a cada período de 3 meses

Indisponibilidades — sejam por falha sistêmica ou manutenção programada — precisam ser registradas e reportadas à estrutura de governança. O Portal Backoffice da Plataforma Opus Open Finance oferece a interface para cadastro de indisponibilidades programadas e o dashboard de acompanhamento de falhas detectadas automaticamente.

---

## Desempenho (tempo de resposta)

As APIs precisam responder dentro de limites de tempo definidos por tipo de operação. As especificações exatas variam por endpoint e são publicadas nas normas regulatórias.

> Para os valores atualizados de SLA por endpoint, consulte as [especificações de Requisitos Não Funcionais do Open Finance Brasil](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/OFB-RequisitosNF.html).

---

## Capacidade (rate limits)

Existem limites de volume de requisições que cada instituição pode receber ou realizar em determinados períodos. Esses limites buscam garantir a estabilidade do ecossistema como um todo.

---

## Como a Plataforma Opus lida com esses requisitos

A Plataforma Opus Open Finance foi projetada para cumprir todos os requisitos não funcionais regulatórios:

- A **arquitetura em microsserviços com Kubernetes** permite escalabilidade horizontal automática para suportar picos de carga
- O **autoscaling** está disponível em todos os módulos e é altamente recomendado para produção
- O módulo de **status (health check)** implementa as APIs regulatórias de disponibilidade e contabiliza todas as chamadas para os cálculos obrigatórios de disponibilidade
- O **Portal Backoffice** oferece interface para registro de indisponibilidades programadas e visualização de falhas detectadas

---

## Referência

- [Requisitos Não Funcionais — documentação da plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/OFB-RequisitosNF.html)
- [Portal do desenvolvedor — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/overview)
