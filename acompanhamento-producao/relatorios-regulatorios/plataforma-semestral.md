---
layout: default
title: Relatório Semestral — Plataforma
parent: Relatórios Regulatórios
grand_parent: Acompanhamento em Produção
nav_order: 1
lang: "pt-br"
---

# Relatório Semestral de Disponibilidade e Volume — Plataforma

**Perfil:** Detentor de Conta / Transmissor de Dados
**Banco de execução:** banco de dados da Plataforma (tabela `public.report`)

O relatório semestral consolida, por mês e por endpoint, a quantidade de chamadas de API recebidas e a disponibilidade média. É exigido pelo Open Finance Brasil nos dois semestres do ano.

---

## Parâmetros

Todos os scripts usam os mesmos parâmetros de entrada:

```sql
-- Formato: YYYY-MM-DD
@set initial_date = '2024-01-01 00:00:00.000 -0300'
@set final_date   = '2024-06-30 23:59:59.999 -0300'
```

Para os scripts de disponibilidade, usar apenas a data (sem hora):

```sql
@set initial_date = '2024-01-01'
@set final_date   = '2024-06-30'
```

O parâmetro `endpoints_services` define quais endpoints serão consultados — um `array[string]` com os paths dos serviços da instituição.

---

## Scripts por fase

### Fase 1 — Dados Abertos

```sql
@set endpoints_services = array [
  '/channels/v2/banking-agents',
  '/channels/v2/branches',
  '/channels/v2/electronic-channels',
  '/channels/v2/phone-channels',
  '/channels/v2/shared-automated-teller-machines',
  '/opendata-accounts/v1/business-accounts',
  '/opendata-accounts/v1/personal-accounts',
  '/opendata-creditcards/v1/business-credit-cards',
  '/opendata-creditcards/v1/personal-credit-cards',
  '/opendata-financings/v1/business-financings',
  '/opendata-financings/v1/personal-financings',
  '/opendata-invoicefinancings/v1/business-invoice-financings',
  '/opendata-invoicefinancings/v1/personal-invoice-financings',
  '/opendata-loans/v1/business-loans',
  '/opendata-loans/v1/personal-loans',
  '/opendata-unarranged/v1/business-unarranged-account-overdraft',
  '/opendata-unarranged/v1/personal-unarranged-account-overdraft'
]
```

### Fase 2 — Consentimento, Recursos e Dados Cadastrais

```sql
@set endpoints_services = array [
  '/consents/v3/consents',
  '/consents/v3/consents/{consentId}',
  '/resources/v3/resources',
  '/customers/v2/business/financial-relations',
  '/customers/v2/business/identifications',
  '/customers/v2/business/qualifications',
  '/customers/v2/personal/financial-relations',
  '/customers/v2/personal/identifications',
  '/customers/v2/personal/qualifications'
]
```

### Fase 2 — Dados Transacionais

```sql
@set endpoints_services = array [
  '/credit-cards-accounts/v2/accounts',
  '/credit-cards-accounts/v2/accounts/{creditCardAccountId}',
  '/credit-cards-accounts/v2/accounts/{creditCardAccountId}/limits',
  '/credit-cards-accounts/v2/accounts/{creditCardAccountId}/transactions',
  '/credit-cards-accounts/v2/accounts/{creditCardAccountId}/bills',
  '/credit-cards-accounts/v2/accounts/{creditCardAccountId}/bills/{billId}/transactions',
  '/credit-cards-accounts/v2/accounts/{creditCardAccountId}/transactions-current',
  '/accounts/v2/accounts',
  '/accounts/v2/accounts/{accountId}',
  '/accounts/v2/accounts/{accountId}/balances',
  '/accounts/v2/accounts/{accountId}/transactions',
  '/accounts/v2/accounts/{accountId}/transactions-current',
  '/accounts/v2/accounts/{accountId}/overdraft-limits',
  '/loans/v2/contracts',
  '/loans/v2/contracts/{contractId}',
  '/loans/v2/contracts/{contractId}/warranties',
  '/loans/v2/contracts/{contractId}/payments',
  '/loans/v2/contracts/{contractId}/scheduled-instalments',
  '/financings/v2/contracts',
  '/financings/v2/contracts/{contractId}',
  '/unarranged-accounts-overdraft/v2/contracts',
  '/invoice-financings/v2/contracts'
]
```

### Fase 3 — Detentor de Conta (Pagamentos)

```sql
@set endpoints_services = array [
  '/payments/v4/consents',
  '/payments/v4/consents/{consentId}',
  '/payments/v4/pix/payments',
  '/payments/v4/pix/payments/{paymentId}',
  '/payments/v4/pix/payments/consents/{consentId}',
  '/automatic-payments/v1/recurring-consents',
  '/automatic-payments/v1/recurring-consents/{recurringConsentId}',
  '/automatic-payments/v2/recurring-consents',
  '/automatic-payments/v2/recurring-consents/{recurringConsentId}',
  '/automatic-payments/v1/pix/recurring-payments',
  '/automatic-payments/v1/pix/recurring-payments/{recurringPaymentId}',
  '/automatic-payments/v2/pix/recurring-payments',
  '/automatic-payments/v2/pix/recurring-payments/{recurringPaymentId}'
]
```

### Fase 4A — Dados Abertos complementares

```sql
@set endpoints_services = array [
  '/opendata-capitalization/v1/bonds',
  '/opendata-investments/v1/funds',
  '/opendata-investments/v1/bank-fixed-incomes',
  '/opendata-investments/v1/credit-fixed-incomes',
  '/opendata-investments/v1/variable-incomes',
  '/opendata-investments/v1/treasure-titles',
  '/opendata-exchange/v1/online-rates',
  '/opendata-exchange/v1/vet-values',
  '/opendata-acquiring-services/v1/personals',
  '/opendata-acquiring-services/v1/businesses',
  '/opendata-pension/v1/risk-coverages',
  '/opendata-pension/v1/survival-coverages',
  '/opendata-insurance/v1/personals',
  '/opendata-insurance/v1/automotives',
  '/opendata-insurance/v1/homes'
]
```

### Fase 4B — Investimentos

```sql
@set endpoints_services = array [
  '/bank-fixed-incomes/v1/investments',
  '/bank-fixed-incomes/v1/investments/{investmentId}',
  '/bank-fixed-incomes/v1/investments/{investmentId}/balances',
  '/bank-fixed-incomes/v1/investments/{investmentId}/transactions',
  '/credit-fixed-incomes/v1/investments',
  '/variable-incomes/v1/investments',
  '/treasure-titles/v1/investments',
  '/funds/v1/investments'
]
```

### Fase 4B — Câmbio

```sql
@set endpoints_services = array [
  '/exchanges/v1/operations',
  '/exchanges/v1/operations/{operationId}',
  '/exchanges/v1/operations/{operationId}/events'
]
```

---

## Múltiplas marcas

Para instituições com mais de uma marca, use os scripts com prefixo `organization_` que consolidam os dados de todas as bases. Requer a extensão `dblink` instalada:

```sql
CREATE EXTENSION IF NOT EXISTS "dblink";
```

A string de conexão para as bases secundárias deve ser formatada como:

```
host={db_target_host} dbname={db_target_dbname} user={db_target_user} password={db_target_password}
```
