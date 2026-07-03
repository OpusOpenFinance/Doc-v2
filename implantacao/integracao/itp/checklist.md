---
layout: default
title: "Checklist: Iniciador de Transação de Pagamento (ITP)"
parent: Implantação
nav_order: 4
has_children: false
lang: "pt-br"
---

# Checklist de Implantação — Iniciador de Transação de Pagamento (ITP)

Este checklist cobre as etapas para implantar o **OpusTPP** no perfil de **Iniciador de Transação de Pagamento (ITP)** — a instituição que inicia pagamentos Pix em nome dos seus clientes junto às Detentoras de Conta.

> O Delivery Manager da Opus acompanha todo o processo. As etapas marcadas com **🔧 Opus** são conduzidas pelo time técnico da Opus; as marcadas com **🏦 Instituição** requerem ação direta da instituição.

---

## Etapa 1 — Kickoff e planejamento

- [ ] 🔧 Opus — Apresentação do plano de projeto e cronograma
- [ ] 🔧 Opus + 🏦 Instituição — Definição das equipes envolvidas
- [ ] 🏦 Instituição — Decisão sobre o [modelo de implantação](../index.html) *(SaaS ou On Premises)*

---

## Etapa 2 — Configuração de ambientes

- [ ] 🔧 Opus — Provisionamento dos ambientes de desenvolvimento, homologação e produção
- [ ] 🔧 Opus — Configuração do OpusTPP nos ambientes
- [ ] 🔧 Opus + 🏦 Instituição — Cadastro no Diretório de Participantes (sandbox) → [ver guia](../diretorio-hml/diretorio-hml.html)
  - Criação da organização
  - Criação do Software Statement com papéis `PAGTO` e `DADOS`
  - Definição das redirect URIs

---

## Etapa 3 — Certificados digitais

- [ ] 🏦 Instituição — Obtenção do certificado **BRCAC** (transporte mTLS) → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🏦 Instituição — Obtenção do certificado **BRSEAL** (assinatura) → [ver Certificados Digitais](../certificados/certificados.html)

> Para ITP, o certificado EV e o certificado de servidor mTLS são necessários apenas se a instituição expuser páginas web para o usuário final. Em soluções 100% via API, apenas BRCAC e BRSEAL são obrigatórios.

---

## Etapa 4 — Certificação de segurança OpenID

A certificação RP (Relying Party) valida que a aplicação ITP está em conformidade com o perfil FAPI-BR como cliente. **A Opus conduz o processo.**

- [ ] 🔧 Opus — Execução dos testes de conformidade RP no certificador OpenID
- [ ] 🔧 Opus + 🏦 Instituição — Pagamento da taxa de certificação
- [ ] 🔧 Opus — Publicação da certificação

Perfil de certificação obrigatório para este perfil: **Relying Party (RP)**

Para detalhes do processo de envio, consulte o [Guia de Certificação de Conformidade](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/155910145).

---

## Etapa 5 — Interface do aplicativo (redirecionamento)

O fluxo de consentimento para ITP exige que o aplicativo da instituição saiba interceptar e processar o retorno do fluxo OIDC após o usuário autorizar na Detentora de Conta.

- [ ] 🏦 Instituição — Implementação do redirecionamento App-to-App → [ver documentação OpusTPP](../../opusTPP/funcionamento/redirecionamento.html)
  - Configuração de Android App Links
  - Configuração de iOS Universal Links
  - Implementação do endpoint `authorization-result`
- [ ] 🏦 Instituição — Implementação do fallback via redirect web (obrigatório mesmo para soluções 100% mobile)
- [ ] 🔧 Opus + 🏦 Instituição — Testes do fluxo de redirecionamento end-to-end

---

## Etapa 6 — Integração com o OpusTPP

- [ ] 🏦 Instituição — Integração do sistema da instituição com as APIs do OpusTPP:
  - Listagem de participantes (`GET /opus-open-finance/participants`)
  - Criação de consentimento de pagamento (`POST /opus-open-finance/payments/v1/consents`)
  - Iniciação de pagamento Pix (`POST /proxy/open-banking/payments/v5/pix/payments`)
  - Consulta de status do pagamento
- [ ] 🏦 Instituição — Configuração de webhook para recebimento de notificações de status → [ver documentação](../../opusTPP/funcionamento/webhooks.html)
- [ ] 🔧 Opus + 🏦 Instituição — Testes contra o [Raidiam Mockbank](../../opusTPP/ferramentasAuxiliares/mockbank.html)

---

## Etapa 7 — Certificação funcional

- [ ] 🔧 Opus + 🏦 Instituição — Execução dos testes funcionais de ITP no certificador da governança
- [ ] 🔧 Opus + 🏦 Instituição — Resolução de eventuais não-conformidades

Para informações sobre os planos de teste disponíveis: [Onboarding ITP](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OnboardingITP.html)

---

## Etapa 8 — Go-Live

- [ ] 🔧 Opus — Configuração do Diretório de Participantes de **produção**
- [ ] 🏦 Instituição — Aquisição e cadastro dos certificados de produção
- [ ] 🔧 Opus — Go-Live com início do monitoramento
- [ ] 🔧 Opus — Início do envio dos relatórios regulatórios ao BACEN

---

## Referências

- [Perfil ITP — Open Finance Brasil](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OFB-ITP.html)
- [Onboarding ITP](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OnboardingITP.html)
- [OpusTPP — Documentação](../../opusTPP/index.html)
- [Iniciação de Pagamento — OpusTPP](../../opusTPP/funcionamento/iniciacaoDePagamento.html)
