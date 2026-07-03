---
layout: default
title: Portabilidade de Crédito
parent: Para Desenvolvedores
nav_order: 4
has_children: false
lang: "pt-br"
---

# Desenvolvimento — Portabilidade de Crédito

A Portabilidade de Crédito é um fluxo regulatório do Open Finance Brasil que permite ao cliente transferir operações de crédito de uma instituição para outra. A plataforma implementa as APIs de Portabilidade de Crédito Pessoal Clean.

---

## Conectores necessários

O serviço de portabilidade de crédito segue o mesmo modelo de desenvolvimento dos demais conectores Camel. A instituição implementa rotas que recebem os dados da plataforma e executam as operações nos sistemas de crédito internos.

As variáveis de configuração suportadas são as mesmas dos outros serviços:

| Variável | Objetivo | Valor padrão |
|---|---|---|
| `camel.main.routes-include-pattern` | Localização dos arquivos de rota | — |
| `apis.validation.json-schema.enabled` | Valida request/response contra schemas (impacta performance) | `false` |
| `apis.validation.openapi.enabled-request` | Valida request contra a especificação OFB | `true` |
| `apis.validation.openapi.enabled-response` | Valida response contra a especificação OFB (impacta performance) | `false` |

---

## Rotas disponíveis

> ⚠️ *[PLACEHOLDER — a lista completa de rotas Camel para portabilidade de crédito está disponível na documentação técnica da plataforma. Adicionar aqui a tabela de rotas quando a página de Portabilidade de Crédito do GitPages estiver acessível.]*

Consulte a documentação técnica em [Portabilidade de Crédito — Integração](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Portabilidade_Credito.html).

---

## Referências

- [Portabilidade de Crédito — Integração da Plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Portabilidade_Credito.html)
- [Connector Tester](../ferramentas/connector-tester.html)
- [Componentes Camel suportados](detentor-transmissor/componentes.html)
