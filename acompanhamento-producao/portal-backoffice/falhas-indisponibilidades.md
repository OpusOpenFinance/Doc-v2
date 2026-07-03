---
layout: default
title: Falhas e Indisponibilidades
parent: Portal Backoffice
grand_parent: Acompanhamento em Produção
nav_order: 1
lang: "pt-br"
---

# Falhas e Indisponibilidades

Esta seção do Portal Backoffice é onde a equipe de operações acompanha e registra eventos que afetam a disponibilidade dos endpoints regulatórios do Open Finance. Manter essas informações atualizadas é uma exigência regulatória — elas alimentam as APIs de status que os outros participantes e a governança consultam.

---

## Falhas

Uma **Falha** é uma indisponibilidade detectada automaticamente pelo sistema de monitoramento da plataforma. O serviço de Status monitora continuamente a disponibilidade dos endpoints com base na taxa de erros coletada pelo API Gateway e nas chamadas de health check. Quando a taxa de erro ultrapassa o limiar, o endpoint é classificado como em falha automaticamente.

As falhas podem ser:
- **Total**: todos os endpoints estão afetados
- **Parcial**: apenas um subconjunto de endpoints está afetado

### O que a equipe faz durante uma falha

Falhas são criadas e encerradas automaticamente pelo sistema — a equipe não precisa abri-las nem fechá-las. O que a equipe pode (e deve) fazer enquanto a falha está em andamento é **editá-la** para informar ao ecossistema quando o serviço deve ser restaurado e uma descrição do problema:

| Campo editável | Descrição |
|---|---|
| **Data/Hora Fim Programado** | Estimativa de quando o serviço voltará ao normal |
| **Descrição** | Texto descritivo da falha em andamento |

> Apenas falhas ativas (em andamento) podem ser editadas. Uma falha é encerrada automaticamente quando o serviço de Status detecta que o problema não está mais presente.

### Listagem de falhas

Todas as falhas — ativas e concluídas — são listadas e podem ser filtradas por:
- Data de detecção
- Data de fim da falha

---

## Indisponibilidades

Uma **Indisponibilidade** é uma janela de tempo programada em que o serviço estará parcial ou totalmente fora do ar — por exemplo, uma janela de manutenção. Diferentemente das falhas, indisponibilidades são criadas manualmente pela equipe antes de ocorrerem.

O cadastro prévio de indisponibilidades programadas é importante porque elas são contabilizadas separadamente das falhas sistêmicas no cálculo de SLA regulatório.

### Campos ao cadastrar uma indisponibilidade

| Campo | Descrição |
|---|---|
| **Data/Hora Início** | Quando a janela de indisponibilidade começa |
| **Data/Hora Fim** | Quando a janela de indisponibilidade termina |
| **Descrição** | Motivo da indisponibilidade (ex.: manutenção planejada do core bancário) |
| **É Parcial?** | Checkbox que define se é parcial (subconjunto de endpoints) ou total |
| **Endpoints afetados** | Lista de endpoints — obrigatória apenas para indisponibilidade parcial |

### Indisponibilidade Total

Não é necessário selecionar endpoints. A indisponibilidade cobre toda a instalação.

### Indisponibilidade Parcial

É necessário selecionar quais endpoints estarão indisponíveis. A lista de endpoints disponíveis para seleção corresponde aos endpoints regulatórios configurados na instalação.

### Gerenciamento

A listagem de indisponibilidades exibe todas as janelas cadastradas — passadas e futuras. É possível **adicionar**, **editar** e **apagar** indisponibilidades diretamente pela interface.

---

## Relação com os SLAs regulatórios

O Open Finance exige disponibilidade de 95% em 24 horas e 99,5% em 3 meses. As falhas sistêmicas e as indisponibilidades programadas entram em cálculos separados. O cadastro correto e tempestivo de indisponibilidades programadas evita que janelas planejadas sejam contabilizadas como falhas não previstas, o que penalizaria mais o SLA da instituição.
