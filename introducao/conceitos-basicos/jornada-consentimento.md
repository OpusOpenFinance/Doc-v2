---
layout: default
title: Jornada de Consentimento
parent: "O que é o Open Finance Brasil"
nav_order: 2
has_children: false
lang: "pt-br"
---

# Jornada de Consentimento

O **consentimento** é o coração do Open Finance. Nenhum dado é compartilhado e nenhum pagamento é iniciado sem que o cliente autorize explicitamente — e essa autorização tem regras rígidas definidas pelo regulador para garantir que o cliente entende o que está aprovando.

---

## O que é consentimento no Open Finance

Consentimento é a autorização que o cliente concede para que uma instituição acesse seus dados ou inicie pagamentos em seu nome junto a outra instituição. Ele é sempre:

- **Explícito**: o cliente precisa aprovar ativamente, nunca por omissão
- **Informado**: o cliente vê claramente quais dados ou operações estão sendo autorizados
- **Revogável**: o cliente pode cancelar a qualquer momento, nos canais da Detentora ou Transmissora
- **Temporário**: tem prazo de validade (até 12 meses para dados; pagamentos têm regras específicas por tipo)

---

## Como a jornada funciona

A jornada de consentimento é o fluxo técnico e de experiência pelo qual o cliente passa para conceder ou revogar uma autorização. Ela tem quatro momentos principais:

**1. Solicitação** — A instituição ativa (ITP ou Receptor de Dados) cria uma intenção de consentimento e redireciona o cliente para os canais da instituição passiva (Detentora ou Transmissora).

**2. Autenticação** — O cliente se autentica nos canais da instituição passiva com suas credenciais habituais.

**3. Confirmação** — O cliente visualiza exatamente o que está sendo solicitado (quais dados, por quanto tempo, para qual finalidade) e confirma ou rejeita.

**4. Retorno** — O cliente é redirecionado de volta à aplicação da instituição ativa com o resultado da autorização.

---

## Do ponto de vista da Detentora / Transmissora

Para a instituição passiva — que recebe o pedido de consentimento — a jornada precisa estar integrada nos seus canais de atendimento. Isso significa que o aplicativo mobile, o Internet Banking ou ambos precisam ser capazes de receber o fluxo, autenticar o cliente e apresentar as telas de confirmação.

O [Guia de Experiência do Usuário do Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378535/Guia+de+Experi+ncia+do+Usu+rio) define os padrões obrigatórios de linguagem, clareza e fluxo que essas telas precisam seguir.

As opções de integração nos canais da instituição estão descritas em [Interface de Usuário](../../implantacao/interface-usuario/interface-usuario.html).

---

## Do ponto de vista do ITP / Receptor de Dados

Para a instituição ativa — que inicia o pedido de consentimento — a jornada precisa estar integrada na sua aplicação, que precisa ser capaz de redirecionar o cliente e receber de volta o resultado da autorização.

Os detalhes técnicos desse fluxo estão em [Redirecionamento App-to-App](../../opusTPP/funcionamento/redirecionamento.html).

---

## Referência

- [Guia de Experiência do Usuário — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378535/Guia+de+Experi+ncia+do+Usu+rio)
- [Jornada de Consentimento — documentação técnica da plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/JornadaConsentimento/OFB-JornadaConsentimento.html)
