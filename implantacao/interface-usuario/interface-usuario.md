---
layout: default
title: Interface de Usuário
parent: Implantação
nav_order: 6
has_children: false
lang: "pt-br"
---

# Interface de Usuário — Jornada de Consentimento

A **jornada de consentimento** é a experiência que o cliente final da instituição vivencia ao autorizar o compartilhamento de dados ou uma iniciação de pagamento. É um dos momentos mais críticos da implantação: ela precisa estar integrada nos canais da instituição e seguir o [Guia de Experiência do Usuário do Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378535/Guia+de+Experi+ncia+do+Usu+rio).

Esta página apresenta as quatro estratégias possíveis e o que cada uma exige da instituição.

---

## As quatro estratégias

### App próprio (Mobile Banking)

A jornada de consentimento acontece dentro do **aplicativo mobile da instituição**. É a melhor experiência para o cliente, pois ele já conhece o app e não precisa sair dele.

**Como funciona:** o aplicativo intercepta as URLs do fluxo de autorização via **Android App Links** (Android) ou **Universal Links** (iOS), processa o consentimento internamente e retorna ao fluxo do TPP ao final.

**O que a instituição precisa desenvolver:**
- Telas de autenticação, seleção e confirmação de recursos consentidos
- Lógica de interceptação das URLs do Authorization Server:
  - `https://<FQDN-open-banking>/auth/auth` (fluxo no mesmo dispositivo)
  - `https://<FQDN-open-banking>/auth/handoff/{id}` (fluxo iniciado em outro dispositivo)
- Integração com a API do Authorization Server (loop de comandos)

A integração com o AS acontece via uma sequência de comandos em formato REST. O app faz um `GET` na URL interceptada com o header `Accept: application/json` — isso sinaliza ao AS que a chamada vem do app, e o AS passa a responder como uma API REST em vez de redirecionar para o browser.

> Documentação técnica detalhada: [Mobile Banking](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Jornada-de-Ux/consentimento/app2as/OOF-App-M%C3%B3vel.html)

---

### Internet Banking (Web)

A jornada acontece na **página web da instituição** (Internet Banking). O usuário é redirecionado para a página de login da instituição e depois para as telas de consentimento.

**Como funciona:** o AS redireciona o browser do usuário para a URL de autenticação configurada na instituição. A comunicação entre a página web e o AS acontece via loop de comandos, com a instituição podendo usar as telas padrão da Opus ou suas próprias telas customizadas.

**O que a instituição precisa desenvolver:**
- Página de login integrada com o AS via federation ou redirect
- Telas de seleção e confirmação de consentimento (ou uso das telas padrão da Opus)
- Tratamento do identificador de sessão passado pelo AS na URL

A URL de autenticação customizada pode receber o identificador de sessão de três formas — query string, fragment ou URL path. O formato **fragment** é recomendado pois remove o identificador do histórico de navegação.

> Documentação técnica detalhada: [Internet Banking](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Jornada-de-Ux/consentimento/web2as/OOF-Internet-Banking.html)

---

### Handoff (QR Code)

Obrigatório para instituições **app-only** — aquelas que só possuem canal mobile e não têm Internet Banking. Quando o usuário está num desktop (no site do TPP, por exemplo) e precisa autorizar o consentimento, o AS exibe um QR Code que o usuário escaneia com o app da instituição.

**Como funciona:** o AS exibe um QR Code contendo a URL `https://<FQDN-open-banking>/auth/handoff/{id}`. O usuário escaneia com qualquer app de leitura de QR Code (inclusive o próprio app da instituição) e é redirecionado para o app, que intercepta a URL e processa o consentimento normalmente.

**O que a instituição precisa desenvolver:**
- Mesma integração do app (interceptação de URL + loop de comandos)
- Garantir que a URL de handoff também é interceptada pelo app

> Documentação técnica detalhada: [Handoff](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Jornada-de-Ux/consentimento/app2as-handoff/OFB-Handoff.html)

---

### Webview fornecida pela Opus

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Descrever aqui as opções de Webview disponibilizadas pela Opus: o que está incluso, como é a customização (cores, logos, textos), e em que cenários é recomendada em vez do desenvolvimento próprio.

---

## Qual estratégia escolher

| Situação da instituição | Estratégia recomendada |
|---|---|
| Tem app mobile próprio | App próprio (Mobile Banking) |
| Tem Internet Banking sem app | Internet Banking (Web) |
| Tem app mobile mas não tem Internet Banking | App próprio + Handoff |
| Tem app e Internet Banking | App próprio + Internet Banking |
| Quer solução rápida sem desenvolvimento de telas | Webview da Opus |

> As estratégias não são exclusivas — a maioria das instituições implementa app + web para cobrir todos os cenários de uso dos seus clientes.

---

## Requisito regulatório de UX

Independentemente da estratégia escolhida, as telas de consentimento precisam seguir o **Guia de Experiência do Usuário do Open Finance Brasil**, que define padrões de clareza, linguagem e fluxo de interação obrigatórios.

- [Guia de Experiência do Usuário — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378535/Guia+de+Experi+ncia+do+Usu+rio)
- [Jornada de Consentimento — conceito](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/JornadaConsentimento/OFB-JornadaConsentimento.html)
