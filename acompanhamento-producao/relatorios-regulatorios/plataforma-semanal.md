---
layout: default
title: Relatórios Semanais — Plataforma
parent: Relatórios Regulatórios
grand_parent: Acompanhamento em Produção
nav_order: 2
lang: "pt-br"
---

# Relatórios Semanais — Plataforma (Detentor de Conta)

Esta página cobre os três relatórios semanais exigidos para o perfil Detentor de Conta.

---

## Relatório Semanal de Disponibilidade

**Banco:** banco de dados da Plataforma
**O que extrai:** quantidade de chamadas recebidas por agrupamento de APIs e disponibilidade média no período

### Parâmetros

```sql
@set initial_date = '2024-01-01'   -- formato YYYY-MM-DD
@set final_date   = '2024-01-07'
```

O parâmetro `endpoints_services` segue o mesmo formato de array do relatório semestral. Os agrupamentos por fase estão listados na página do [Relatório Semestral](plataforma-semestral.html).

---

## Relatório de Interoperabilidade — Fase 3 (Detentor)

**Objetivo:** acompanhar o funil completo do fluxo de pagamento — desde a criação do consentimento até os pagamentos efetivados.

O relatório é composto por quatro seções, cada uma executada em um banco diferente:

### Seção 1 — Consentimentos Gerados

**Banco:** `OOB-Consent`

Na primeira execução, criar as funções auxiliares:
```sql
-- Pré-requisito: criar a function get_conglomerate_name
-- Depois criar a função principal:
SELECT * FROM payment_consent_count('<data_inicio>', '<data_fim>', false);
-- O terceiro parâmetro: false = todos os pagamentos | true = apenas pagamentos automáticos
```

Exemplo:
```sql
SELECT * FROM payment_consent_count('2024-01-02', '2024-01-08', false);
```

### Seção 2 — Autenticação e Redirecionamento

**Banco:** `OOB-Authorization-Server`

Requer a criação de três funções auxiliares (`decode_base64url`, `get_consent_product_flow`, `payment_consent_extract_authorization_data`):

```sql
SELECT * FROM payment_consent_extract_authorization_data('2024-01-02', '2024-01-08', false);
```

### Seção 3 — Conclusão da Autenticação e Autorização

**Banco:** `OOB-Consent`

```sql
SELECT * FROM payment_consent_client_authorization('2024-01-02', '2024-01-08', false);
```

### Seção 4 — Pagamentos Recebidos e IDs Gerados

**Banco:** `OOB-Consent`

```sql
SELECT * FROM payment_consent_payment_id('2024-01-02', '2024-01-08', false);
```

> Após cada execução, consulte o **ParentOrganization Reference** do Iniciador conforme descrito nos scripts auxiliares fornecidos pela Opus.

---

## Relatório de Requisitos Não Funcionais

**Objetivo:** verificar conformidade com os SLAs de tempo de resposta e disponibilidade exigidos pelo regulador para pagamentos.

### Tempo de Resposta

**Banco:** `PCM`

O parâmetro `data_fim` é a **sexta-feira anterior** à emissão do relatório:

```sql
SELECT * FROM payments_response_time('2024-01-12');
```

> **Atenção:** desconsiderar o campo `data_metrica` no resultado — é enviado apenas para referência interna.

O cálculo considera a diferença de tempo entre a chegada da requisição e a resposta na camada do gateway (Kong). São excluídas chamadas com HTTP Code 423, 429 e 529.

### Disponibilidade

**Banco:** `OOB-Status`

```sql
SELECT * FROM status_function_availability('2024-01-12');
```

O cálculo considera os intervalos de instabilidade em segundos, com base em erros HTTP 5XX e health checks. As fórmulas aplicadas são:

**Últimos três meses (90 dias):**
```
(777600 - <total de indisponibilidade em segundos>) / 777600
```

**Diário:**
```
(86400 - <total de indisponibilidade em segundos>) / 86400
```

**Para múltiplas marcas:** use os scripts com prefixo `organization_` — requerem a extensão `dblink` e uma string de conexão para as bases das outras marcas.
