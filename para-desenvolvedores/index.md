---
layout: default
title: Para Desenvolvedores
parent: "Documentação Opus Open Finance"
nav_order: 4
has_children: true
lang: "pt-br"
---

# Para Desenvolvedores

Esta seção é o guia técnico de integração com a Plataforma Opus Open Finance. Ela é voltada para os times de desenvolvimento das instituições clientes que precisam construir os **conectores** — a camada de integração entre a plataforma e os sistemas de retaguarda.

---

## Contexto de desenvolvimento

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Descrever aqui o ambiente de desenvolvimento recomendado: pré-requisitos de ferramentas (Docker, Java, etc.), como obter acesso ao ECR da Opus para baixar as imagens, e como montar um ambiente local funcional antes de iniciar o desenvolvimento dos conectores.

---

## Macro etapas

O desenvolvimento de conectores segue este ciclo:

1. **Entender o perfil de atuação** — cada perfil exige conectores diferentes. Consulte a seção do seu perfil abaixo.
2. **Configurar o ambiente local** — instalar Docker, obter as imagens da Opus, montar o ambiente de testes com o Connector Tester.
3. **Desenvolver as rotas Camel** — implementar as rotas de integração para cada endpoint do seu perfil, respeitando os contratos de request/response definidos pela plataforma.
4. **Testar com o Connector Tester** — executar as simulações de chamadas do ecossistema Open Finance contra os conectores desenvolvidos, de forma isolada.
5. **Integrar ao ambiente de homologação** — subir os conectores na instalação de homologação e executar os testes funcionais regulatórios.
6. **Go-live** — promover os conectores para produção.

---

## Como os conectores funcionam

A Plataforma Opus Open Finance usa **Apache Camel** como motor de integração. O desenvolvimento de um conector consiste em criar **rotas Camel XML** que:

1. Recebem um objeto de entrada no formato definido pela plataforma (`direct:<nomeDaRota>`)
2. Fazem as chamadas necessárias aos sistemas legados da instituição
3. Retornam a resposta no formato esperado pela plataforma

A plataforma é responsável por toda a camada de segurança regulatória — validação de consentimento, assinaturas criptográficas, mapeamento de IDs de recursos. O conector é responsável apenas por buscar ou executar os dados nos sistemas internos.

---

## Por onde começar

Selecione o perfil da sua instituição:

- [**Detentor de Conta / Transmissor de Dados**](perfis/detentor-transmissor/index.html) — conectores de pagamento, discovery e dados financeiros
- [**Receptor de Dados**](perfis/receptor/index.html) — integração via OpusTPP (sem conectores Camel)
- [**Iniciador de Transação de Pagamento (ITP)**](perfis/itp/index.html) — integração via OpusTPP (sem conectores Camel)
- [**Portabilidade de Crédito**](perfis/portabilidade/index.html) — conectores específicos para o fluxo de portabilidade

---

## Ferramentas de desenvolvimento

- [**Connector Tester**](ferramentas/connector-tester.html) — ferramenta Docker para testar os conectores isoladamente
- [**Quick Simulator**](ferramentas/quick-simulator.html) — simula um ITP ou Receptor de Dados para testar Detentoras e Transmissoras
- [**Opus TPP Demo**](ferramentas/opus-tpp-demo.html) — ⚠️ placeholder
