---
layout: default
title: Recepção de Dados
parent: Produtos
nav_order: 4
has_children: false
lang: "pt-br"
---

# Recepção de Dados

A **Recepção de Dados** é a capacidade de solicitar e obter dados financeiros dos seus clientes junto às instituições onde eles possuem conta — com autorização explícita de cada cliente, dentro das regras do Open Finance Brasil.

Esta página descreve o que é possível fazer como Receptora de Dados, quais dados ficam disponíveis e como o OpusTPP simplifica o acesso a eles.

---

## O que é possível fazer

Com os consentimentos dos seus clientes ativos, sua instituição pode consultar os dados deles em qualquer Transmissora de Dados participante do Open Finance Brasil. Os dados retornam em tempo real a cada consulta e refletem o estado atual na Transmissora.

Se precisar de dados sempre atualizados sem gerenciar consultas manualmente, o [Opus Data Receiver](opus-data-receiver.html) automatiza essa atualização periódica e consolida dados de múltiplas instituições.

---

## Dados disponíveis para recepção

### Dados cadastrais

Informações pessoais e empresariais do cliente:
- Pessoa física: nome, CPF, data de nascimento, endereço, contatos, nacionalidade, filiação, estado civil
- Pessoa jurídica: razão social, CNPJ, endereço, contatos, representantes

### Contas

Para cada conta do cliente na Transmissora:
- Dados da conta (tipo, agência, número, ISPB)
- Saldos (disponível, bloqueado, automaticamente investido)
- Transações (créditos e débitos com data, valor e descrição)
- Limites de crédito

### Cartão de crédito

- Dados das contas pós-pagas
- Faturas (abertas e fechadas, com vencimento e valor)
- Transações do cartão
- Limites (total, disponível, parcelado)

### Operações de crédito

- **Empréstimos**: contrato, prestações, pagamentos realizados, garantias
- **Financiamentos**: contrato, prestações, pagamentos realizados, garantias
- **Adiantamento a depositantes**: contrato e condições
- **Direitos creditórios descontados**: contrato e condições

### Investimentos

- **Renda fixa bancária**: CDB, RDB, LCI, LCA e similares
- **Renda fixa crédito**: debêntures, CRI, CRA e similares
- **Renda variável**: ações, ETFs, BDRs
- **Fundos de investimento**: cotas e movimentações
- **Tesouro Direto**: títulos e movimentações

### Câmbio

Operações de câmbio do cliente: tipo de operação, valor, moeda, taxa e data.

---

## Como funciona com o OpusTPP

O OpusTPP abstrai toda a complexidade do processo. Do ponto de vista da sua aplicação, o fluxo é:

1. **Listar participantes**: `GET /opus-open-finance/participants` — retorna as Transmissoras disponíveis
2. **Criar consentimento**: `POST /opus-open-finance/consents/v1/consents` — define quais dados você quer acessar e por quanto tempo
3. **Redirecionar o cliente**: o cliente autoriza o consentimento nos canais da Transmissora
4. **Consultar dados**: com o consentimento aprovado, as APIs de proxy do OpusTPP retornam os dados diretamente

Nas etapas 3 e 4, o OpusTPP gerencia automaticamente os tokens de acesso, as assinaturas criptográficas e todos os requisitos de segurança — sua aplicação não precisa lidar com nada disso.

### Sobre as permissões

Ao criar o consentimento, é necessário especificar exatamente quais dados você quer acessar. O Open Finance Brasil define agrupamentos obrigatórios: você não pode pedir apenas uma permissão isolada de um grupo — precisa solicitar o conjunto completo definido pelo regulador. A Transmissora rejeita consentimentos com permissões divergentes dos agrupamentos.

> Para a tabela completa de permissões e agrupamentos obrigatórios, consulte a [documentação de permissões do OpusTPP](../opusTPP/conceitos/permissoesOpenFinance.html).

### Sobre a vigência dos consentimentos

Consentimentos de dados têm vigência de até 12 meses. Durante esse período, o cliente pode revogar o consentimento a qualquer momento nos canais da Transmissora. O OpusTPP suporta renovação de consentimentos e nova tentativa de autorização em caso de falha no redirecionamento.

---

## Relação com os outros produtos

| Necessidade | Produto indicado |
|---|---|
| Consultar dados pontualmente sob demanda | OpusTPP (módulo Receptor de Dados) |
| Manter dados atualizados automaticamente | Opus Data Receiver + OpusTPP |
| Consolidar dados de múltiplas instituições numa visão única | Opus Data Receiver |
| Receber alertas quando algo muda nos dados do cliente | Opus Data Receiver (fila de eventos) |

---

## Referências

- [OpusTPP — Recepção de Dados (documentação técnica)](../opusTPP/funcionamento/recepcaoDeDados.html)
- [Opus Data Receiver](opus-data-receiver.html)
- [Permissões e agrupamentos — Open Finance](../opusTPP/conceitos/permissoesOpenFinance.html)
- [Checklist de implantação — Receptor de Dados](../implantacao/integracao/receptor/checklist.html)
