---
layout: default
title: "Visão cliente: o que preciso disponibilizar?"
parent: Introdução
nav_order: 2
has_children: false
lang: "pt-br"
---

# Visão cliente: o que preciso disponibilizar?

Esta página responde a pergunta mais prática de quem está chegando ao Open Finance pela primeira vez: **o que concretamente minha instituição precisa entregar?**

A resposta depende dos perfis que sua instituição vai exercer. Veja abaixo o resumo por perfil — sem a complexidade técnica, apenas o escopo do que precisa ser construído ou configurado.

---

## Detentor de Conta

Você é Detentor de Conta se sua instituição **custodia contas** (corrente, poupança, pagamento pré-paga) e precisa receber pedidos de pagamento Pix iniciados por outras instituições.

**O que você precisa disponibilizar:**

- **Telas de consentimento de pagamento** integradas ao seu app mobile e/ou Internet Banking, seguindo o Guia de UX do Open Finance Brasil
- **Conectores de pagamento**: integração entre a plataforma e o seu sistema de Pix (criação de pagamento, consulta de status, cancelamento de agendamento)
- **Conector de discovery**: retorna quais contas do cliente podem receber o pagamento
- **Certificações**: segurança OpenID (perfil OP) e funcional
- **Certificados digitais**: BRCAC, BRSEAL, EV e MTLS

> Se sua instituição for **app-only** (sem Internet Banking), também é obrigatório implementar o fluxo de **Handoff** com QR Code para usuários em desktop.

---

## Transmissor de Dados

Você é Transmissor de Dados se sua instituição precisa **compartilhar os dados financeiros dos seus clientes** com outras instituições autorizadas pelos próprios clientes.

**O que você precisa disponibilizar:**

- **Telas de consentimento de dados** integradas ao seu app e/ou Internet Banking
- **Conectores de dados**: integração entre a plataforma e seus sistemas para cada categoria de dado que você vai compartilhar (dados cadastrais, contas, cartões, crédito, investimentos, câmbio)
- **Conector de discovery**: retorna quais produtos do cliente estão disponíveis para compartilhamento
- **Certificações**: segurança OpenID (perfil OP) e funcional
- **Certificados digitais**: BRCAC, BRSEAL, EV e MTLS

> Detentor de Conta e Transmissor de Dados geralmente são implantados juntos — eles compartilham a maior parte da infraestrutura, telas e certificações.

---

## Iniciador de Transação de Pagamento (ITP)

Você é ITP se sua instituição quer **iniciar pagamentos Pix** em nome dos seus clientes em outras instituições, sem ser a Detentora em si.

**O que você precisa disponibilizar:**

- **Integração do app** com o fluxo de redirecionamento: seu aplicativo precisa saber interceptar o retorno do fluxo de autorização de consentimento (Android App Links / iOS Universal Links)
- **Integração com as APIs do OpusTPP**: listagem de participantes, criação de consentimento, iniciação de pagamento, consulta de status
- **Configuração de webhook**: para receber notificações de mudança de status de pagamentos
- **Certificações**: segurança OpenID (perfil RP) e funcional
- **Certificados digitais**: BRCAC e BRSEAL

> O Opus TPP (middleware de ITP) cuida de toda a complexidade de segurança e autenticação com as Detentoras. Sua instituição só precisa integrar com a API REST do OpusTPP.

---

## Receptor de Dados

Você é Receptor de Dados se sua instituição quer **receber e usar dados financeiros dos seus clientes** de outras instituições para oferecer serviços como análise de crédito, gestão financeira pessoal ou comparação de produtos.

**O que você precisa disponibilizar:**

- **Integração do app** com o fluxo de redirecionamento (mesma lógica do ITP)
- **Integração com as APIs do OpusTPP**: listagem de participantes, criação de consentimento com as permissões certas, consumo dos endpoints de dados via proxy
- **Definição das permissões**: escolher quais categorias de dados sua aplicação vai solicitar (ver tabela de permissões e agrupamentos obrigatórios)
- **Certificações**: segurança OpenID (perfil RP) e funcional
- **Certificados digitais**: BRCAC e BRSEAL

> Se quiser automatizar a atualização periódica dos dados dos clientes, o **Opus Data Receiver (ODR)** faz isso transparentemente — sua aplicação consome apenas a API consolidada, sem precisar gerenciar consentimentos e chamadas individuais.

---

## Resumo por perfil

| O que precisa | Det. de Conta | Transm. Dados | ITP | Receptor |
|---|:---:|:---:|:---:|:---:|
| Telas de consentimento no app/web | ✅ | ✅ | — | — |
| Conectores para sistemas de retaguarda | ✅ | ✅ | — | — |
| Integração app com redirecionamento | — | — | ✅ | ✅ |
| Integração com API do OpusTPP | — | — | ✅ | ✅ |
| Certificado EV + MTLS | ✅ | ✅ | ⚠️ | ⚠️ |
| Certificado BRCAC + BRSEAL | ✅ | ✅ | ✅ | ✅ |
| Certificação OpenID OP | ✅ | ✅ | — | — |
| Certificação OpenID RP | — | — | ✅ | ✅ |
| Certificação funcional | ✅ | ✅ | ✅ | ✅ |

> ⚠️ EV e MTLS são necessários para ITP e Receptor apenas se houver front-end web exposto ao usuário final.

---

## Próximos passos

Identificou seu perfil? Vá direto para o checklist de implantação:

- [Checklist: Detentor de Conta / Transmissor de Dados](../../implantacao/integracao/detentor-transmissor/checklist.html)
- [Checklist: ITP](../../implantacao/integracao/itp/checklist.html)
- [Checklist: Receptor de Dados](../../implantacao/integracao/receptor/checklist.html)
