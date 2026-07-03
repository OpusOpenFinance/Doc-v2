---
layout: default
title: Perfis de participação
parent: "O que é o Open Finance Brasil"
nav_order: 1
has_children: true
lang: "pt-br"
---

# Perfis de Participação

As instituições financeiras participam do Open Finance Brasil exercendo um ou mais **perfis de participação**. Algumas instituições são obrigadas a exercer determinados perfis; todas podem, voluntariamente, exercer qualquer um.

O ecossistema se divide em dois grandes domínios — **dados** e **pagamentos** — e em cada um há uma parte ativa (quem inicia a ação) e uma parte passiva (quem responde):

| Domínio | Parte passiva | Parte ativa |
|---|---|---|
| **Dados** | Transmissora de Dados | Receptora de Dados |
| **Pagamentos** | Detentora de Conta | Iniciadora de Transação de Pagamento (ITP) |

O termo **TPP** (Third-Party Provider) é a nomenclatura técnica usada para as partes ativas — Receptor de Dados e ITP.

---

## Os cinco perfis

### Dados Abertos
Exposição de informações públicas da instituição (produtos, tarifas, canais de atendimento) sem necessidade de autenticação. É o perfil mais simples e obrigatório para a maioria das instituições.

→ [Ver perfil Dados Abertos](dados-abertos.html)

### Transmissor de Dados
A instituição compartilha dados cadastrais e transacionais dos seus clientes com outras instituições (Receptoras de Dados), mediante consentimento explícito do cliente.

O que é compartilhado: dados pessoais, contas, cartões de crédito, operações de crédito, investimentos, câmbio.

→ [Ver perfil Transmissor de Dados](transmissor.html)

### Detentor de Conta
A instituição recebe e processa pedidos de iniciação de pagamento enviados por ITPs. O cliente autoriza o pagamento nos canais da Detentora, e o ITP executa a transação.

Meios de pagamento atualmente disponíveis no Open Finance: **Pix** (imediato, agendado, recorrente e automático). Outros meios estão previstos para o futuro.

→ [Ver perfil Detentor de Conta](detentor.html)

### Receptor de Dados
A instituição solicita e recebe dados financeiros dos seus clientes junto a outras instituições (Transmissoras de Dados). Usa esses dados para oferecer serviços como comparação de produtos, análise de crédito ou gestão financeira pessoal.

→ [Ver perfil Receptor de Dados](receptor.html)

### Iniciador de Transação de Pagamento (ITP)
A instituição inicia pagamentos Pix em nome dos seus clientes junto às Detentoras de Conta, sem precisar ser a Detentora em si. O cliente autoriza o pagamento na Detentora, e o ITP executa e acompanha a transação.

→ [Ver perfil ITP](itp.html)

---

## Uma instituição pode exercer mais de um perfil

É comum — e muitas vezes obrigatório — que uma mesma instituição exerça múltiplos perfis simultaneamente. Um banco de médio porte, por exemplo, pode ser ao mesmo tempo Transmissor de Dados, Detentor de Conta e ITP.

A Plataforma Opus Open Finance cobre todos os perfis. O que muda entre eles são os módulos instalados, os conectores desenvolvidos e as certificações obtidas.

---

## Nesta seção

- [Dados Abertos](dados-abertos.html)
- [Transmissor de Dados](transmissor.html)
- [Detentor de Conta](detentor.html)
- [Receptor de Dados](receptor.html)
- [ITP — Iniciador de Transação de Pagamento](itp.html)
