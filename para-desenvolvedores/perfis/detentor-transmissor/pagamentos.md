---
layout: default
title: Conectores de Pagamento
parent: "Detentor de Conta / Transmissor de Dados"
nav_order: 2
has_children: false
lang: "pt-br"
---

# Conectores de Pagamento (Detentor de Conta)

Os conectores de pagamento integram a Plataforma Opus Open Finance com o sistema Pix da instituição. Eles são obrigatórios para o perfil Detentor de Conta.

---

## Rotas disponíveis por versão

A plataforma suporta múltiplas versões simultâneas das APIs de pagamento. O conector deve implementar as rotas das versões que a instituição quer suportar.

### Pix

| Método | Versão | Endpoint | Rota Camel |
|---|---|---|---|
| POST | v1 | `/pix/payments` | `direct:paymentsPostPixPayments` |
| GET | v1 | `/pix/payments/{paymentId}` | `direct:paymentsGetPixPaymentsPaymentId` |
| POST | v2 | `/pix/payments` | `direct:paymentsPostPixPayments_v2` |
| GET | v2 | `/pix/payments/{paymentId}` | `direct:paymentsGetPixPaymentsPaymentId_v2` |
| PATCH | v2 | `/pix/payments/{paymentId}` | `direct:paymentsPatchPixPaymentsPaymentId_v2` |
| POST | v3 | `/pix/payments` | `direct:paymentsPostPixPayments_v3` |
| GET | v3 | `/pix/payments/{paymentId}` | `direct:paymentsGetPixPaymentsPaymentId_v3` |
| PATCH | v3 | `/pix/payments/{paymentId}` | `direct:paymentsPatchPixPaymentsPaymentId_v3` |

Exemplo de rota mínima para criação de pagamento Pix v3:

```xml
<routes xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns="http://camel.apache.org/schema/spring"
        xsi:schemaLocation="http://camel.apache.org/schema/spring
            http://camel.apache.org/schema/spring/camel-spring.xsd">

    <route id="paymentsPostPixPayments_v3Route">
        <from uri="direct:paymentsPostPixPayments_v3"/>
        <setHeader name="CamelHttpMethod">
            <constant>POST</constant>
        </setHeader>
        <toD uri="netty-http:{{pix.host}}/api/pix/payments?bridgeEndpoint=true&amp;throwExceptionOnFailure=false"/>
    </route>

</routes>
```

---

## Variáveis de configuração suportadas

| Variável | Objetivo | Valor padrão |
|---|---|---|
| `camel.main.routes-include-pattern` | Localização dos arquivos de rota | — |
| `apis.validation.json-schema.enabled` | Valida request/response contra os schemas definidos (impacta performance) | `false` |
| `apis.validation.openapi.enabled-request` | Valida request contra a especificação OFB | `true` |
| `apis.validation.openapi.enabled-response` | Valida response contra a especificação OFB (impacta performance) | `false` |
| `cnpjInitiatorValidation.directoryRolesUrl` | URL do Diretório de Participantes para validação do CNPJ do iniciador | `https://data.directory.openbankingbrasil.org.br/roles` |
| `quarkus.cache.caffeine.directory.expire-after-write` | TTL do cache da consulta ao Diretório | `5M` |

---

## Validações e cenários

Para os cenários de pagamento suportados e as validações que a plataforma e o conector devem realizar, consulte:

- [Validações de Pagamentos](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/validacoes-pagamentos/Validacoes-Pagamentos.html)
- [Cenários de Pagamentos](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/cenarios-pagamentos/Cenarios-Pagamentos.html)

---

## Referências

- [Connector Tester](../../ferramentas/connector-tester.html) — para testar os conectores de pagamento isoladamente
- [Boas práticas de conectores](boas-praticas.html)
