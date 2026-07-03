---
layout: default
title: Conceito — Diretório de Participantes PRD
parent: Preparativos para Produção
nav_order: 2
lang: "pt-br"
---

# Diretório de Participantes — Produção

O Diretório de Participantes de produção é o repositório oficial mantido pelo Banco Central onde todas as instituições autorizadas a operar no Open Finance Brasil estão registradas. É deste ambiente que saem os certificados, os Software Statements e as informações que os outros participantes usam para validar sua instituição em toda e qualquer chamada regulatória.

---

## Diferença entre Sandbox e Produção

Durante a implantação, a instituição trabalha no **ambiente sandbox** (homologação) para configurar certificados, executar testes e obter certificações. O ambiente de produção só é acessado quando tudo está aprovado.

| | Sandbox | Produção |
|---|---|---|
| URL | [web.sandbox.directory.openbankingbrasil.org.br](https://web.sandbox.directory.openbankingbrasil.org.br) | [web.directory.openbankingbrasil.org.br](https://web.directory.openbankingbrasil.org.br) |
| Certificados | Gerados para testes — não têm validade no ecossistema real | Certificados ICP-Brasil oficiais — usados em todas as chamadas regulatórias |
| Efeito das alterações | Apenas no ambiente de testes | Imediato no ecossistema real |
| Quando acessar | Durante toda a fase de implantação e homologação | Somente após aprovação de todas as certificações |

---

## O que o Diretório de Produção contém

A estrutura é a mesma do sandbox:

**Organização** — registro da instituição identificado pelo CNPJ. É a entidade raiz de tudo o que a instituição opera no Open Finance.

**Software Statements** — cada aplicação ou marca que a instituição opera tem um Software Statement próprio, com seu `softwareStatementId`, `client_id`, certificados associados e redirect URIs autorizadas.

**Certificados** — os certificados BRCAC e BRSEAL gerados no Diretório de Produção ficam publicados e são consultados pelas outras instituições para validar conexões mTLS e assinaturas JWS em tempo real.

---

## Múltiplos Diretórios

Open Finance e Open Insurance possuem Diretórios independentes. Instituições que atuam nos dois ecossistemas precisam de cadastros separados — um em cada Diretório.

---

## Quando fazer o cadastro de produção

O cadastro de produção é a última etapa antes do go-live. Ele só deve ser iniciado depois que:

- Todos os testes funcionais foram aprovados no certificador da governança
- A certificação de segurança OpenID foi aprovada e publicada
- Os certificados digitais de produção (BRCAC, BRSEAL, EV, MTLS) foram adquiridos junto às autoridades certificadoras ICP-Brasil

→ [Ir para o guia de cadastro](cadastro.html)
