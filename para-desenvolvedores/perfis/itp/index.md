---
layout: default
title: Iniciador de Transação de Pagamento (ITP)
parent: Para Desenvolvedores
nav_order: 3
has_children: false
lang: "pt-br"
---

# Desenvolvimento — Iniciador de Transação de Pagamento (ITP)

Para o perfil de ITP, **não é necessário desenvolver conectores**. A integração é feita diretamente com as APIs REST do OpusTPP.

O OpusTPP gerencia automaticamente DCR em todas as Detentoras de Conta, os tokens de acesso por instituição, as assinaturas regulatórias e o envio de reportes à PCM.

---

## O que desenvolver

### Integração com a API do OpusTPP

| Etapa | Endpoint |
|---|---|
| Listar Detentoras disponíveis | `GET /opus-open-finance/participants` |
| Criar consentimento de pagamento | `POST /opus-open-finance/payments/v1/consents` |
| Retornar resultado da autorização | `POST /opus-open-finance/authorization-result` |
| Criar pagamento Pix | `POST /proxy/open-banking/payments/v5/pix/payments` |
| Consultar status do pagamento | `GET /proxy/open-banking/payments/v5/pix/payments/{paymentId}` |

Para pagamentos automáticos (Pix Automático / Transferências Inteligentes), use os endpoints de `recurring-consents` e `recurring-payments`. Para pagamento sem redirecionamento (FIDO2), use os endpoints de `enrollments`.

Consulte a documentação completa em [Iniciação de Pagamento — OpusTPP](../../opusTPP/funcionamento/iniciacaoDePagamento.html).

### Redirecionamento mobile

Se a aplicação for mobile, configure Android App Links e iOS Universal Links para interceptar as URLs de retorno do fluxo de autorização do consentimento. A URL a interceptar é:

```
https://<OOC-FQDN>/opus-open-finance/payments/redirect-uri
```

Mesmo em soluções 100% mobile, a **rota de redirect web é obrigatória** como fallback. Consulte [Redirecionamento App-to-App](../../opusTPP/funcionamento/redirecionamento.html).

### Recebimento de webhooks

Configure a URL de webhook para receber notificações de mudança de status de pagamentos e consentimentos. O processamento é assíncrono — as notificações chegam apenas com o timestamp da atualização, sem o novo status. É necessário consultar o status após receber a notificação. Consulte [Webhooks de Pagamentos](../../opusTPP/funcionamento/webhooks.html).

---

## Referências

- [Iniciação de Pagamento — OpusTPP](../../opusTPP/funcionamento/iniciacaoDePagamento.html)
- [Pagamento Automático — OpusTPP](../../opusTPP/funcionamento/pagamentoAutomatico.html)
- [Vínculo de Dispositivo — OpusTPP](../../opusTPP/funcionamento/vinculoDeDispositivo.html)
- [Webhooks de Pagamentos](../../opusTPP/funcionamento/webhooks.html)
- [Redirecionamento App-to-App](../../opusTPP/funcionamento/redirecionamento.html)
- [Mockbank — testes em homologação](../../opusTPP/ferramentasAuxiliares/mockbank.html)
- [Checklist de implantação — ITP](../../implantacao/integracao/itp/checklist.html)
