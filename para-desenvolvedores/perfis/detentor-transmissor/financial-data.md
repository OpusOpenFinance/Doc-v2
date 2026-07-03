---
layout: default
title: Conectores de Dados Financeiros
parent: "Detentor de Conta / Transmissor de Dados"
nav_order: 3
has_children: false
lang: "pt-br"
---

# Conectores de Dados Financeiros (Transmissor de Dados)

Os conectores de dados financeiros integram a plataforma com os sistemas de retaguarda para compartilhamento de dados cadastrais e transacionais dos clientes. São obrigatórios para o perfil Transmissor de Dados.

---

## APIs cobertas

O serviço `financial-data` da plataforma corresponde às seguintes APIs regulatórias do Open Finance Brasil:

- Dados Cadastrais (clientes PF e PJ)
- Cartão de Crédito
- Contas
- Empréstimos, Financiamentos, Adiantamento a Depositantes, Direitos Creditórios
- Investimentos: Renda Fixa Bancária, Renda Fixa Crédito, Renda Variável, Tesouro Direto, Fundos
- Câmbio

---

## Como funcionam as rotas

Cada endpoint regulatório mapeia para uma rota Camel específica. O conector deve implementar as rotas dos produtos que a instituição oferece.

Exemplo — rota para consulta de saldo de conta:

```xml
<route id="accountsGetAccountsAccountIdBalancesRoute">
    <from uri="direct:accountsGetAccountsAccountIdBalances"/>
    <setHeader name="CamelHttpMethod">
        <constant>GET</constant>
    </setHeader>
    <setBody><constant></constant></setBody>
    <toD uri="netty-http:{{core.host}}/api/contas/${header.accountId}/saldo?bridgeEndpoint=true&amp;throwExceptionOnFailure=false"/>
</route>
```

A lista completa de rotas por produto está na documentação técnica da plataforma — consulte a seção de [Compartilhamento de Dados](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/CamadaIntegra%C3%A7%C3%A3o.html).

---

## Variáveis de configuração suportadas

| Variável | Objetivo | Valor padrão |
|---|---|---|
| `camel.main.routes-include-pattern` | Localização dos arquivos de rota | — |
| `apis.validation.json-schema.enabled` | Valida request/response contra os schemas (impacta performance) | `false` |
| `apis.validation.openapi.enabled-request` | Valida request contra a especificação OFB | `true` |
| `apis.validation.openapi.enabled-response` | Valida response contra a especificação OFB (impacta performance) | `false` |

---

## Conectores de Dados Abertos

O serviço `open-data` da plataforma corresponde às APIs públicas (sem autenticação) — produtos e serviços, canais de atendimento, investimentos, câmbio, capitalização, previdência e seguros.

Para dados abertos, as rotas Camel também são implementadas da mesma forma, mas o conector acessa sistemas de catálogo de produtos da instituição em vez de dados transacionais do cliente.

Variáveis de configuração para open-data:

| Variável | Objetivo | Valor padrão |
|---|---|---|
| `camel.main.routes-include-pattern` | Localização dos arquivos de rota | — |
| `apis.validation.openapi.enabled-request` | Valida request contra a especificação OFB | `true` |
| `apis.validation.openapi.enabled-response` | Valida response contra a especificação OFB (impacta performance) | `false` |

A lista completa de rotas de dados abertos por API está em [Dados Abertos — Integração](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Dados_abertos.html).

---

## Referências

- [Connector Tester](../../ferramentas/connector-tester.html)
- [Boas práticas de conectores](boas-praticas.html)
- [Classe utilitária camelHelper](camel-helper.html)
