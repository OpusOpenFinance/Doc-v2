---
layout: default
title: "Checklist: Detentor de Conta / Transmissor de Dados"
parent: Implantação
nav_order: 3
has_children: false
lang: "pt-br"
---

# Checklist de Implantação — Detentor de Conta / Transmissor de Dados

Este checklist cobre as etapas necessárias para implantar a Plataforma Opus Open Finance nos perfis de **Detentor de Conta** (recebe pedidos de pagamento de ITPs) e **Transmissor de Dados** (compartilha dados cadastrais e transacionais dos clientes com Receptores de Dados). Esses dois perfis frequentemente são implantados juntos, pois compartilham grande parte da infraestrutura.

> O Delivery Manager da Opus acompanha todo o processo. As etapas marcadas com **🔧 Opus** são conduzidas pelo time técnico da Opus; as marcadas com **🏦 Instituição** requerem ação direta da instituição.

---

## Etapa 1 — Kickoff e planejamento

- [ ] 🔧 Opus — Apresentação do plano de projeto e cronograma
- [ ] 🔧 Opus + 🏦 Instituição — Definição das equipes envolvidas
- [ ] 🏦 Instituição — Decisão sobre o [modelo de implantação](../index.html) *(SaaS ou On Premises)*

---

## Etapa 2 — Configuração de ambientes

- [ ] 🔧 Opus — Provisionamento dos ambientes de desenvolvimento, homologação e produção
- [ ] 🔧 Opus — Configuração da Plataforma nos ambientes
- [ ] 🔧 Opus + 🏦 Instituição — Configuração do sandbox do Diretório de Participantes → [ver guia](../diretorio-hml/diretorio-hml.html)

---

## Etapa 3 — Certificados digitais

- [ ] 🏦 Instituição — Obtenção do certificado **BRCAC** (transporte mTLS) → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🏦 Instituição — Obtenção do certificado **BRSEAL** (assinatura) → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🏦 Instituição — Obtenção do certificado **EV** para endpoints com front-end de usuário → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🏦 Instituição — Obtenção do certificado **MTLS** de servidor ICP-Brasil → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🏦 Instituição — Definição dos FQDNs (domínios) para o Authorization Server e Resource Server → [ver Certificados Digitais](../certificados/certificados.html#domínios-e-endpoints-associados)

---

## Etapa 4 — Certificação de segurança OpenID

A certificação de segurança é a validação de que o Authorization Server da plataforma está em conformidade com o perfil FAPI-BR exigido pelo Open Finance Brasil. **A Opus conduz todo o processo de certificação de segurança.**

- [ ] 🔧 Opus — Execução dos testes de conformidade de segurança (DCR + FAPI)
- [ ] 🔧 Opus — Preparação dos artefatos de certificação (formulários OpenID)
- [ ] 🔧 Opus + 🏦 Instituição — Pagamento da taxa de certificação junto à OpenID Foundation
- [ ] 🔧 Opus — Publicação da certificação no [site oficial da OpenID](https://openid.net/certification/#FAPI_OPs)

Perfil de certificação obrigatório para este perfil: **OpenID Provider (OP)**

---

## Etapa 5 — Interface de usuário (jornada de consentimento)

A jornada de consentimento é a experiência que o cliente final da instituição vivencia ao autorizar o compartilhamento de dados ou uma iniciação de pagamento. Ela precisa estar integrada nos canais da instituição.

- [ ] 🏦 Instituição — Escolha da estratégia de interface → [ver Interface de Usuário](../interface-usuario/interface-usuario.html)
  - App mobile próprio
  - Internet Banking (web)
  - Handoff (QR Code para instituições app-only)
  - Webview fornecida pela Opus
- [ ] 🏦 Instituição — Desenvolvimento ou customização das telas de consentimento, seguindo o [Guia de Experiência do Usuário do Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378535/Guia+de+Experi+ncia+do+Usu+rio)
- [ ] 🏦 Instituição — Integração das telas com o Authorization Server da plataforma → [ver Interface de Usuário](../interface-usuario/interface-usuario.html)
- [ ] 🔧 Opus + 🏦 Instituição — Testes da jornada de consentimento end-to-end

---

## Etapa 6 — Camada de integração (conectores)

A camada de integração conecta a Plataforma Opus aos sistemas de retaguarda da instituição. É aqui que fica o trabalho mais significativo de desenvolvimento do lado da instituição.

- [ ] 🏦 Instituição — Entendimento do modelo de conectores → [ver Camada de Integração](../camada-integracao/camada-integracao.html)
- [ ] 🏦 Instituição — Desenvolvimento dos conectores conforme o perfil:

**Para Detentor de Conta:**
- [ ] Conector de **discovery de recursos** (contas, cartões vinculados ao cliente) → [ver documentação](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/consent/Discovery-Recursos.html)
- [ ] Conector de **iniciação de pagamento Pix** (criação e consulta de status)
- [ ] Conector de **cancelamento de agendamento Pix** (para pagamentos agendados)

**Para Transmissor de Dados:**
- [ ] Conector de **discovery de recursos** → [ver documentação](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/consent/Discovery-Recursos.html)
- [ ] Conectores de **dados abertos** (produtos e serviços da instituição) → [ver documentação](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Dados_abertos.html)
- [ ] Conectores de **dados cadastrais** (clientes PF e PJ)
- [ ] Conectores de **dados transacionais** (contas, cartões, investimentos, crédito)

- [ ] 🔧 Opus + 🏦 Instituição — Testes dos conectores com a ferramenta Connector Tester

---

## Etapa 7 — Certificação funcional

Os testes funcionais validam que as APIs regulatórias estão respondendo conforme as especificações do Open Finance Brasil.

- [ ] 🔧 Opus + 🏦 Instituição — Execução dos planos de teste funcionais no certificador da governança
- [ ] 🔧 Opus + 🏦 Instituição — Resolução de eventuais não-conformidades identificadas

Os planos de teste obrigatórios variam conforme os produtos oferecidos pela instituição. Acompanhe as execuções publicadas em: [https://web.conformance.directory.openbankingbrasil.org.br/plans.html?public=true](https://web.conformance.directory.openbankingbrasil.org.br/plans.html?public=true)

---

## Etapa 8 — Migração de consentimentos

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Esta etapa é necessária apenas para instituições que já participam do Open Finance com outra solução. Descrever aqui o processo de migração de consentimentos e DCRs existentes para a Plataforma Opus.

---

## Etapa 9 — Configurações finais e Go-Live

- [ ] 🔧 Opus + 🏦 Instituição — Testes da jornada completa com conectores e telas integrados
- [ ] 🔧 Opus — Configuração do Diretório de Participantes de **produção**
- [ ] 🏦 Instituição — Aquisição e cadastro dos certificados digitais de **produção** → [ver Certificados Digitais](../certificados/certificados.html)
- [ ] 🔧 Opus — Go-Live com início do monitoramento
- [ ] 🔧 Opus — Início do envio dos relatórios regulatórios ao BACEN

---

## Referências

- [Roadmap de Implantação completo](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Implanta%C3%A7%C3%A3o/OOF-Implanta%C3%A7%C3%A3o.html)
- [Perfil Detentor de Conta — Open Finance Brasil](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OFB-Detentor.html)
- [Perfil Transmissor de Dados — Open Finance Brasil](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OFB-Transmissor.html)
- [Integração da Plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/OOF-Integra%C3%A7%C3%A3o.html)
