---
layout: default
title: Cadastro — Diretório de Participantes PRD
parent: Preparativos para Produção
nav_order: 3
lang: "pt-br"
---

# Cadastro no Diretório de Participantes — Produção

Este guia descreve o processo de cadastro da instituição no Diretório de Participantes de **produção**. O processo é análogo ao do sandbox, mas com implicações diretas no ecossistema real — qualquer dado cadastrado incorretamente pode afetar o funcionamento em produção.

> O cadastro de produção é conduzido em conjunto com o Delivery Manager da Opus. Não realize etapas sem alinhamento prévio.

---

## Pré-requisitos

Antes de iniciar o cadastro de produção, confirme que:

- [ ] Todos os testes de certificação funcional foram aprovados
- [ ] A certificação de segurança OpenID foi publicada no site da OpenID Foundation
- [ ] Os certificados digitais de produção foram adquiridos (BRCAC, BRSEAL e, conforme o perfil, EV e MTLS)
- [ ] As redirect URIs definitivas de produção foram definidas

---

## Passo 1 — Acessar o Diretório de Produção

Acesse [https://web.directory.openbankingbrasil.org.br](https://web.directory.openbankingbrasil.org.br) com um usuário com permissão de criação e edição de Software Statements na organização.

---

## Passo 2 — Registrar a organização

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Descrever aqui se a organização de produção já existe (criada pela Opus ou pelo regulador) ou se precisa ser criada pela instituição, e qual o processo de aprovação envolvido.

---

## Passo 3 — Criar o Software Statement

Dentro da organização, crie um Software Statement para cada aplicação ou marca que a instituição irá operar em produção.

> ⚠️ Não é possível alterar as informações do Software Statement após visualizar o Software Statement Assertion (SSA). Verifique todos os campos múltiplas vezes antes de concluir.

**Campos de atenção especial:**

**Redirect URIs de produção** — diferentemente do sandbox, as URIs de produção são as URLs reais da aplicação da instituição. Não use URLs de ferramentas de teste ou certificação. Toda URL usada no fluxo de consentimento precisa estar cadastrada aqui.

**Papel regulatório (role)** — defina os papéis correspondentes aos perfis de atuação em produção:
- `DADOS` — para Transmissor de Dados
- `PAGTO` — para Detentor de Conta
- `CONTA` — para operações em conta corrente

---

## Passo 4 — Gerar os certificados de produção

No Diretório, gere os certificados **BRCAC** e **BRSEAL** para o Software Statement de produção. Esses certificados são diferentes dos usados no sandbox — são certificados ICP-Brasil com validade no ecossistema real.

> ⚠️ Jamais disponibilize as chaves privadas em serviços da internet. Guarde-as em um cofre de senhas ou Kubernetes Secret imediatamente após a geração.

---

## Passo 5 — Configurar os certificados na plataforma

Com os certificados de produção gerados, atualize os Kubernetes Secrets da instalação de produção com os novos arquivos. O processo é o mesmo descrito em [Instalação e Configuração](../../opusTPP/configuracao/index.html).

---

## Passo 6 — Validar o cadastro

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Descrever aqui como validar que o cadastro de produção está correto antes do go-live: como verificar se os certificados estão publicados corretamente no Diretório, como confirmar que o DCR automático da plataforma consegue se registrar nas outras instituições, e qual é o procedimento de smoke test recomendado.

---

## Referências

- [Diretório de Participantes — Homologação](../../implantacao/diretorio-hml/diretorio-hml.html) — processo de cadastro no sandbox (estrutura idêntica)
- [Certificados Digitais](../../implantacao/certificados/certificados.html) — quais certificados cada perfil precisa
- [Guia de Operação do Diretório Central — Open Finance Brasil](https://openbanking-brasil.github.io/areadesenvolvedor/documents/OpenBanking-Guia_Operacao_Diretorio_Central.pdf)
