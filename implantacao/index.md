---
layout: default
title: Implantação
parent: "Opus Open Finance"
nav_order: 3
has_children: true
lang: "pt-br"
---

# Implantação

Esta seção é o guia central de implantação da Plataforma Opus Open Finance. Ela está organizada por **perfil de participação**, porque o que cada instituição precisa fazer depende diretamente do papel que ela ocupa no ecossistema do Open Finance Brasil.

> Um Delivery Manager da Opus é designado para acompanhar todo o processo de implantação. As etapas descritas aqui refletem o que a instituição precisa entregar — a Opus cuida das etapas técnicas de configuração e certificação.

---

## Por onde começar

Antes de mergulhar nas etapas específicas do seu perfil, duas atividades são comuns a todos:

**1. Definir o modelo de implantação**
> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Descrever aqui as diferenças entre SaaS e On Premises, o que cada modelo implica para a instituição e como escolher.

**2. Obter os certificados digitais**
Todos os perfis precisam de certificados digitais. Os tipos variam conforme o perfil — veja a página [Certificados Digitais](certificados/certificados.html) para entender quais você precisa.

---

## Checklists por perfil

Selecione o perfil da sua instituição para ver o checklist completo de implantação:

| Perfil | O que faz no Open Finance |
|---|---|
| [**Detentor de Conta / Transmissor de Dados**](integracao/detentor-transmissor/checklist.html) | Recebe pedidos de pagamento e/ou compartilha dados de clientes com outras instituições |
| [**Iniciador de Transação de Pagamento (ITP)**](integracao/itp/checklist.html) | Inicia pagamentos em nome de clientes em outras instituições |
| [**Receptor de Dados**](integracao/receptor/checklist.html) | Recebe e consolida dados financeiros de clientes de outras instituições |

> Uma mesma instituição pode atuar em mais de um perfil. Nesse caso, consulte os checklists de cada perfil separadamente — há etapas e certificados específicos para cada um.

---

## Tópicos transversais

Páginas que se aplicam a múltiplos perfis e são referenciadas nos checklists:

- [Certificados Digitais](certificados/certificados.html) — quais certificados cada perfil precisa e como obtê-los
- [Diretório de Participantes — Homologação](diretorio-hml/diretorio-hml.html) — como criar conta, configurar e operar no sandbox
- [Interface de Usuário](interface-usuario/interface-usuario.html) — opções de jornada de consentimento (Webview, app próprio, Internet Banking, Handoff)
- [Camada de Integração](camada-integracao/camada-integracao.html) — como conectar a Plataforma aos sistemas de retaguarda da instituição
