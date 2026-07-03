---
layout: default
title: Relatórios Regulatórios
parent: Acompanhamento em Produção
nav_order: 2
has_children: true
lang: "pt-br"
---

# Relatórios Regulatórios

O Banco Central exige que todas as instituições participantes do Open Finance enviem periodicamente relatórios sobre a saúde e a utilização dos seus serviços. A Opus fornece scripts SQL que ajudam na extração dos dados necessários para cada relatório.

> **Responsabilidade da instituição:** executar os scripts, formatar os dados no padrão e no período exigidos pelo OFB, e enviar os relatórios dentro dos prazos regulatórios. Os scripts são uma base de extração — ajustes podem ser necessários conforme alterações regulatórias.

---

## Calendário de relatórios

| Relatório | Periodicidade | Perfil | Scripts disponíveis |
|---|---|---|---|
| [Semestral de Disponibilidade e Volume](plataforma-semestral.html) | Semestral | Detentor / Transmissor | ✅ |
| [Semanal de Disponibilidade](plataforma-semanal.html) | Semanal | Detentor / Transmissor | ✅ |
| [Interoperabilidade — Fase 3 (Detentor)](plataforma-interoperabilidade.html) | Semanal | Detentor de Conta | ✅ |
| [Requisitos Não Funcionais (Detentor)](plataforma-rnf.html) | Semanal | Detentor de Conta | ✅ |
| [Semestral — Receptor de Dados](opustpp-semestral.html) | Semestral | Receptor de Dados | ✅ |
| [Interoperabilidade — Fase 2 (Receptor)](opustpp-interoperabilidade.html) | Semanal | Receptor de Dados / ITP | ✅ |
| [Semanal — Fase 3 (ITP)](opustpp-semanal-itp.html) | Semanal | ITP | ✅ |

---

## Como usar os scripts

Todos os scripts seguem o mesmo padrão:

1. Criar as funções SQL necessárias no banco indicado (na primeira execução — use `CREATE OR REPLACE FUNCTION` para idempotência)
2. Chamar a função com os parâmetros de data no formato `yyyy-MM-dd`
3. Formatar o resultado conforme exigido pelo Open Finance Brasil

**Boas práticas operacionais:**
- Execute os scripts em réplicas de leitura quando disponível, para evitar impacto no banco principal
- Para instituições com múltiplas marcas, use os scripts com prefixo `organization_` que consolidam dados de todas as bases
- Aumente o `statement_timeout` do PostgreSQL durante a execução em bases de grande volume
