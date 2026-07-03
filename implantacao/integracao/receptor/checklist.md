---
layout: default
title: "Checklist: Receptor de Dados"
parent: Implantação
nav_order: 5
has_children: false
lang: "pt-br"
---

# Checklist de Implantação — Receptor de Dados

Este checklist cobre as etapas para implantar o **OpusTPP** no perfil de **Receptor de Dados** — a instituição que solicita e consolida dados financeiros dos seus clientes junto às Transmissoras de Dados.

> O Delivery Manager da Opus acompanha todo o processo. As etapas marcadas com **🔧 Opus** são conduzidas pelo time técnico da Opus; as marcadas com **🏦 Instituição** requerem ação direta da instituição.

---

## Etapa 1 — Kickoff e planejamento

- [ ] 🔧 Opus — Apresentação do plano de projeto e cronograma
- [ ] 🔧 Opus + 🏦 Instituição — Definição das equipes envolvidas
- [ ] 🏦 Instituição — Decisão sobre o [modelo de implantação](../index.html) *(SaaS ou On Premises)*
- [ ] 🏦 Instituição — Definição se será utilizado o **Opus Data Receiver (ODR)** para atualização automática de dados

---

## Etapa 2 — Configuração de ambientes

- [ ] 🔧 Opus — Provisionamento dos ambientes de desenvolvimento, homologação e produção
- [ ] 🔧 Opus — Configuração do OpusTPP nos ambientes
- [ ] 🔧 Opus + 🏦 Instituição — Cadastro no Diretório de Participantes (sandbox) → [ver guia](../diretorio-hml/diretorio-hml.html)
  - Criação da organização
  - Criação do Software Statement com papel `DADOS`
  - Definição das redirect URIs

---

## Etapa 3 — Certificados digitais

- [ ] 🏦 Instituição — Obtenção do certificado **BRCAC** (transporte mTLS) → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🏦 Instituição — Obtenção do certificado **BRSEAL** (assinatura) → [ver Certificados Digitais](../certificados/certificados.html)

> Para Receptor de Dados, o certificado EV e o certificado de servidor mTLS são necessários apenas se a instituição expuser páginas web para o usuário final.

---

## Etapa 4 — Certificação de segurança OpenID

- [ ] 🔧 Opus — Execução dos testes de conformidade RP no certificador OpenID
- [ ] 🔧 Opus + 🏦 Instituição — Pagamento da taxa de certificação
- [ ] 🔧 Opus — Publicação da certificação

Perfil de certificação obrigatório para este perfil: **Relying Party (RP)**

---

## Etapa 5 — Interface do aplicativo (redirecionamento)

O fluxo de consentimento para Receptor de Dados também exige redirecionamento para a Transmissora de Dados.

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
  - Criação de consentimento de dados (`POST /opus-open-finance/consents/v1/consents`)
  - Definição das permissões conforme os [agrupamentos obrigatórios](../../opusTPP/conceitos/permissoesOpenFinance.html)
  - Consumo dos endpoints de dados via proxy
- [ ] 🔧 Opus + 🏦 Instituição — Testes contra o [Raidiam Mockbank](../../opusTPP/ferramentasAuxiliares/mockbank.html)

**Se for utilizar o Opus Data Receiver:**
- [ ] 🔧 Opus — Configuração do ODR (odr-core + odr-scheduler)
- [ ] 🏦 Instituição — Integração com a Customer Data API do ODR para consulta de dados consolidados
- [ ] 🏦 Instituição — Configuração de notificações de eventos (expiração de consentimento, novos contratos, etc.)

---

## Etapa 7 — Certificação funcional

- [ ] 🔧 Opus + 🏦 Instituição — Execução dos testes funcionais de Receptor de Dados no certificador da governança
- [ ] 🔧 Opus + 🏦 Instituição — Resolução de eventuais não-conformidades

---

## Etapa 8 — Go-Live

- [ ] 🔧 Opus — Configuração do Diretório de Participantes de **produção**
- [ ] 🏦 Instituição — Aquisição e cadastro dos certificados de produção
- [ ] 🔧 Opus — Go-Live com início do monitoramento
- [ ] 🔧 Opus — Início do envio dos relatórios regulatórios ao BACEN

---

## Referências

- [Perfil Receptor de Dados — Open Finance Brasil](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OFB-Receptor.html)
- [OpusTPP — Documentação](../../opusTPP/index.html)
- [Recepção de Dados — OpusTPP](../../opusTPP/funcionamento/recepcaoDeDados.html)
- [Permissões e Agrupamentos — Open Finance](../../opusTPP/conceitos/permissoesOpenFinance.html)
