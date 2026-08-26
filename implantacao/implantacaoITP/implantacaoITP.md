---
title: "Implantação ITP"
summary: "Página em construção."
---

# Detalhamento das Etapas de Implantação — Iniciador de Transação de Pagamento (ITP)

Esta página complementa o [Checklist de Implantação — ITP](../integracao/itp/checklist.html) com uma descrição mais detalhada de cada etapa, incluindo o que é entregue por cada parte, referências técnicas e pontos de atenção observados em implantações reais.

## Etapa 1 — Onboarding: autorização e regulação junto ao Banco Central

Etapa de responsabilidade da **Instituição Cliente**, referente ao processo de compliance e jurídico junto ao Banco Central para atuar como ITP no Open Finance Brasil.

Consulte o guia de onboarding: [Onboarding ITP](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OnboardingITP.html)

## Etapa 2 — Liberação do ambiente de homologação (SaaS Opus)

A **Opus** provisiona e libera o ambiente de homologação (sandbox) para a instituição. A liberação ocorre em conjunto com a execução e publicação dos testes de segurança OpenID (Etapa 3) — só depois disso o ambiente pode ser efetivamente utilizado nos testes funcionais via Pix Tester.

## Etapa 3 — Testes de segurança OpenID — Perfil RP

A **Opus** executa os testes de conformidade de segurança (perfil FAPI-BR, papel Relying Party) e conduz o trâmite de assinaturas e pagamento da taxa junto à instituição. Ao final, a certificação RP da instituição é publicada no site da OpenID Foundation:

[Implementações certificadas — OpenID Foundation](https://openid.net/certification/all-certified-implementations/)

Perfil de certificação obrigatório para este perfil: **Relying Party (RP)**.

## Etapa 4 — Disponibilização da collection Postman

A **Opus** disponibiliza a collection do Postman para a instituição. Essa collection é utilizada para sensibilizar a ferramenta Pix Tester durante os testes funcionais (Etapa 5).

## Etapa 5 — Testes via Pix Tester

Testes funcionais conduzidos entre **Opus e Instituição Cliente**. Em geral a Opus executa uma primeira rodada de testes e a instituição conclui as demais verificações necessárias para fechar esta etapa.

## Etapa 6 — Desenvolvimento da integração do aplicativo com o produto Opus (ITP)

Etapa de responsabilidade da **Instituição Cliente**: desenvolver a integração do seu aplicativo com o produto de ITP da Opus.

Referências:
- [Pagamento Automático — Transferências Inteligentes](../../opusTPP/funcionamento/pagamentoAutomatico.html)
- Especificação de API (Swagger) — Pagamentos Automáticos
- [Redirecionamento App-to-App e Web](../../opusTPP/funcionamento/redirecionamento.html)

[COMPLEMENTAR E REESCREVER]

## Etapa 7 — Certificados digitais (BRCAC, BRSEAL, EV e mTLS)

Ver [Certificados Digitais](../certificados/certificados.html) para o detalhamento de cada tipo de certificado.

> Se a instituição já atua em outro perfil do Open Finance (por exemplo, Detentor de Conta) com a mesma marca/CNPJ, os certificados digitais já adquiridos podem, em alguns casos, ser reaproveitados para o perfil ITP — não sendo necessária a aquisição de novos certificados. Confirme esse aproveitamento com o Delivery Manager da Opus, pois depende da configuração específica de cada instituição.

## Etapa 8 — Validação do cadastro do Application

No ambiente de produção, uma vez criado o primeiro DCR (Dynamic Client Registration) da instituição, o Diretório de Participantes bloqueia a nomenclatura definida para o Application, que não pode mais ser alterada.

> **Importante:** caso seja necessário alterar o nome do Application, é obrigatória a criação de um novo Application, junto com a aquisição de um **novo certificado BRCAC de produção**.

## Etapa 9 — Validação da implantação do webhook

No fluxo de Transferências Inteligentes, o desenvolvimento do endpoint de webhook é opcional, mas recomendado para o ambiente de produção.

Ver [Webhooks](../../opusTPP/funcionamento/webhooks.html)

## Etapa 10 — Definição e cadastro das URLs de redirecionamento no Diretório de Participantes

A definição das URLs de redirecionamento é de responsabilidade da **instituição Cliente**. Consulte a orientação em [Configuração — Definir URLs de redirecionamento](../../opusTPP/index.html)

### 10.1. Applications → URIs

Campos a cadastrar no Diretório de Participantes (valores abaixo são apenas ilustrativos):

| Campo | Exemplo |
|---|---|
| Logo URI | `https://assets.<instituicao>.com/.../logo.svg` |
| Redirect URI | `https://<dominio-instituicao>/opus-open-finance/payments/redirect-uri/<instituicao>`<br>`https://<dominio-instituicao>/opus-open-finance/consents/redirect-uri/<instituicao>`<br>`https://<dominio-instituicao>/opus-open-finance/payments-recurring-consents/redirect-uri/<instituicao>` |
| Homepage URI | `https://www.<instituicao>.com/` |
| API Webhook URI | `https://mtls-<dominio-instituicao>` |

### 10.2. Applications → App Certificates

1. Cadastrar a EncKey no Diretório de Participantes.
2. Realizar o upload da CSR.
3. Encaminhar à Opus a chave privada gerada na etapa anterior, junto com a respectiva senha.

### 10.3. Applications → Certifications

Após concluídas as etapas anteriores, a certificação cadastrada passa a ser exibida na tela Applications → Certifications do Diretório de Participantes.

## Etapa 11 — Revisão e liberação do ambiente SaaS de produção

Após a instituição encaminhar a chave privada da EncKey (Etapa 10.2), a **Opus** realiza a configuração e revisão final do ambiente de produção. A Opus disponibiliza a URL operacional do produto, que deve ser acessada pela instituição através de rede privada (VPN) previamente estabelecida.

## Etapa 12 — Solicitação de participação nos testes em produção

A **Instituição Cliente** deve registrar a Solicitação de Interesse em Participação no Portal do Open Finance Brasil, selecionando a opção **"Iniciadora"**.

## Etapa 13 — Execução dos testes em produção

A **Instituição Cliente** executa os testes em produção — pré-requisito para a solicitação de aprovação via service desk (Etapa 14).

Orientações do processo de onboarding de ITPs: [Onboarding de Iniciadores de Transações de Pagamento (ITPs) — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1210318906/Onboarding+de+Iniciadores+de+Transa+es+de+Pagamentos+ITPs)

## Etapa 14 — Solicitação de aprovação via service desk

Após a conclusão dos testes em produção, a **Instituição Cliente** deve solicitar a aprovação via service desk.

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — O documento de origem não especifica qual service desk (da Opus, do Open Finance Brasil, ou de terceiros) nem os dados de contato/abertura de chamado. Complementar aqui.

## Etapa 15 — Habilitação da role PAGTO no Diretório de Participantes

Após a aprovação da etapa anterior, a role PAGTO é habilitada no Diretório de Participantes, concluindo a implantação do perfil ITP.

## Referências

- [Onboarding ITP — Opus Open Finance](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/PerfisOFB/OnboardingITP.html)
- [Implementações certificadas — OpenID Foundation](https://openid.net/certification/all-certified-implementations/)
- [Onboarding de Iniciadores de Transações de Pagamento (ITPs) — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1210318906/Onboarding+de+Iniciadores+de+Transa+es+de+Pagamentos+ITPs)
- [Checklist de Implantação — ITP](../integracao/itp/checklist.html)
- [Certificados Digitais](../certificados/certificados.html)

> ⚠️ *[PLACEHOLDER — aguarda confirmação da Opus]* — Os links de "Pagamento Automático / Transferências Inteligentes", "Redirecionamento" e "Webhooks" do documento de origem apontavam para `opusopenfinance.com/Documentation/...`, um domínio diferente do usado nas demais páginas deste repositório (`opusopenfinance.github.io/Realize/...`). Mantive os caminhos relativos desta documentação (`../../opusTPP/...`) por consistência, mas os caminhos exatos das páginas de destino (Pagamento Automático, Redirecionamento, Webhooks, Configuração de URLs) precisam ser conferidos e corrigidos por quem conhece a estrutura atual de `opusTPP/`.
