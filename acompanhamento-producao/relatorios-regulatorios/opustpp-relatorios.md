---
layout: default
title: Relatórios — OpusTPP
parent: Relatórios Regulatórios
grand_parent: Acompanhamento em Produção
nav_order: 3
lang: "pt-br"
---

# Relatórios Regulatórios — OpusTPP

Esta página cobre os relatórios obrigatórios para os perfis de **Receptor de Dados** e **Iniciador de Transação de Pagamento (ITP)** operados via OpusTPP.

---

## Relatório Semestral — Receptor de Dados

**Banco:** `PCM` (banco de dados do PCM Service)

Extrai a quantidade de chamadas de API por mês para os endpoints de consentimento e resources, na perspectiva do receptor.

### Consentimentos — Recepção

```sql
@set initial_date = '2024-01-01 00:00:00.000 -0300'
@set final_date   = '2024-06-30 23:59:59.999 -0300'

WITH result_tab AS (
  WITH endpoints_table AS (
    SELECT date_trunc('month', created_at, 'America/Sao_Paulo') AS ano_mes,
           (event_data->>'endpoint')::text AS endpoint
    FROM public.report
    WHERE event_role = 'CLIENT'
      AND created_at BETWEEN :initial_date AND :final_date
      AND (event_data->>'endpoint')::text NOT IN ('/register', '/token')
  )
  SELECT TO_CHAR(ano_mes, 'yyyy-MM') AS ano_mes,
         COUNT(1) AS qtd_chamadas
  FROM endpoints_table
  WHERE endpoint LIKE '/open-banking/consents%'
  GROUP BY TO_CHAR(ano_mes, 'yyyy-MM')
  ORDER BY TO_CHAR(ano_mes, 'yyyy-MM')
)
SELECT * FROM result_tab;
```

### Resources — Recepção

Mesma query, alterando o filtro do `WHERE`:

```sql
  WHERE endpoint LIKE '/open-banking/resources%'
```

---

## Relatório de Interoperabilidade — Fase 2 (Receptor de Dados / ITP)

**Banco:** `OOD4TPP`

O relatório cobre consentimentos receptados, consumo de consentimentos e estoque ativo.

### Consentimentos Receptados

Na primeira execução, criar a função `consent_receptor` com o script fornecido pela Opus. Depois:

```sql
-- Todos os participantes:
SELECT * FROM consent_receptor('2024-01-02', '2024-01-08');

-- Filtrado por organização:
SELECT * FROM consent_receptor('2024-01-02', '2024-01-08', '27a20310-756e-43b8-a43c-6927be86b99e');
```

### Consumo de Consentimentos

Na primeira execução, criar a função `consent_consume`. Depois:

```sql
SELECT * FROM consent_consume('2024-01-02', '2024-01-08');
```

### Estoque — Clientes Ativos

Na primeira execução, criar a função `consent_stock_clients`. Depois:

```sql
-- Data de corte (data fim do período):
SELECT * FROM consent_stock_clients('2024-01-08');

-- Filtrado por organização:
SELECT * FROM consent_stock_clients('2024-01-08', '27a20310-756e-43b8-a43c-6927be86b99e');
```

### Estoque — Consentimentos Ativos

Na primeira execução, criar a função `consent_stock`. Depois:

```sql
SELECT * FROM consent_stock('2024-01-08');
```

---

## Relatório Semanal — Fase 3 (ITP)

**Banco:** `PCM`

Extrai o volume de iniciações de pagamento por ITP no período.

Na primeira execução, criar a função `payment_initiator` com o script fornecido pela Opus. Depois:

```sql
-- Todos os ITPs:
SELECT * FROM payment_initiator('2024-01-02', '2024-01-08');

-- Filtrado por ITP específico:
SELECT * FROM payment_initiator('2024-01-02', '2024-01-08', '27a20310-756e-43b8-a43c-6927be86b99e');
```

---

## Boas práticas

- Use `CREATE OR REPLACE FUNCTION` ao criar as funções para garantir idempotência (pode ser executado múltiplas vezes sem erro)
- Execute em réplicas de leitura quando disponível
- Os scripts são uma base de extração — a formatação final e o envio ao regulador são responsabilidade da instituição
