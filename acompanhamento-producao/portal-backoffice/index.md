---
layout: default
title: Portal Backoffice
parent: Acompanhamento em Produção
nav_order: 1
has_children: true
lang: "pt-br"
---

# Portal Backoffice

O Portal Backoffice da Plataforma Opus Open Finance é a interface administrativa para as equipes de operações, suporte e compliance da instituição. Ele centraliza as atividades que precisam acontecer no dia a dia para manter a conformidade com os requisitos regulatórios de disponibilidade.

---

## O que o Portal oferece

- **[Falhas e Indisponibilidades](falhas-indisponibilidades.html)** — visualização de falhas detectadas automaticamente e cadastro de janelas de manutenção programada
- **[APIs de Gestão de Consentimentos](apis-consentimentos.html)** — consulta, revogação e gerenciamento de consentimentos e pagamentos via API
- **[Customização Visual](customizacao.html)** — configuração de identidade visual do portal (logo, cores, título)
- **[Autenticação via Federation](federation.html)** — integração com o Identity Provider da instituição para login institucional

---

## Autenticação no Portal

O acesso ao portal é feito com o login institucional da organização, via mecanismo de **Federation** com o Identity Provider (IDP) já utilizado pela instituição. Isso significa que os usuários não precisam de credenciais separadas — usam o mesmo login que já utilizam em outros sistemas internos.

Detalhes de configuração em [Autenticação via Federation](federation.html).
