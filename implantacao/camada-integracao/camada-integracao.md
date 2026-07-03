---
layout: default
title: Camada de Integração
parent: Implantação
nav_order: 7
has_children: false
lang: "pt-br"
---

# Camada de Integração

A **camada de integração** é o adaptador que conecta a Plataforma Opus Open Finance aos sistemas de retaguarda da instituição. É por ela que os dados dos clientes chegam à plataforma e os pagamentos são efetivados nos sistemas internos.

---

## O conceito

A Plataforma Opus Open Finance funciona como um middleware: ela recebe as requisições do ecossistema Open Finance, valida segurança e conformidade, e então aciona os sistemas internos da instituição para obter os dados ou executar as operações. A camada de integração é justamente a ponte entre a plataforma e esses sistemas internos.

**O importante:** na grande maioria dos casos, **não é necessário modificar os sistemas de retaguarda** da instituição. O que precisa ser construído é um adaptador — chamado de **conector** ou **plugin** — que traduz os formatos exigidos pelo Open Finance para os formatos que os sistemas internos já entendem.

Pense assim: se o Open Finance pede dados de conta no formato JSON com campos específicos, mas o sistema core bancário da instituição responde em outro formato, o conector faz essa tradução. A plataforma não fala diretamente com o core — ela fala com o conector, e o conector fala com o core.

---

## Conceitos básicos

### Protocolo de segurança

A comunicação entre a plataforma e os conectores acontece por HTTP/HTTPS interno. Os protocolos de segurança regulatórios (FAPI-BR, mTLS, JWS) são tratados inteiramente pela plataforma — o conector não precisa implementar nada disso.

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Detalhar aqui os protocolos de segurança específicos da comunicação entre a plataforma e os conectores (autenticação interna, certificados necessários, etc.).

### Documentação da camada

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Referenciar aqui onde fica a documentação técnica completa da API de integração (schemas, contratos, exemplos por produto).

---

## Desenvolvimento próprio

A instituição pode desenvolver os conectores em qualquer linguagem ou tecnologia, desde que respeite os contratos de API definidos pela Opus. A Plataforma usa o Apache Camel como motor de integração interno, mas os conectores externos podem ser serviços independentes.

A Opus disponibiliza:
- **Especificações dos contratos** de cada conector (o que a plataforma envia e o que espera de volta)
- **Exemplos de plugins** para os principais cenários
- **Connector Tester** — ferramenta que simula chamadas do ecossistema Open Finance e permite testar os conectores antes de conectar ao ambiente real

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Adicionar link para os exemplos de plugins disponibilizados no repositório.

---

## Desenvolvimento com suporte da Opus

> ⚠️ *[PLACEHOLDER — aguarda informações da Opus]* — Descrever aqui as opções em que a Opus participa do desenvolvimento da camada de integração: quais modelos de engajamento existem, quais sistemas de retaguarda já têm conectores prontos, etc.

---

## O que precisa ser conectado por perfil

### Detentor de Conta

| Conector | O que faz |
|---|---|
| Discovery de recursos | Retorna as contas e cartões do cliente que podem receber pagamentos |
| Iniciação de pagamento Pix imediato | Cria o pagamento Pix e retorna o status |
| Iniciação de pagamento Pix agendado | Agenda o pagamento para uma data futura |
| Consulta de status de pagamento | Verifica se o pagamento foi liquidado |
| Cancelamento de agendamento | Cancela um pagamento agendado ainda não executado |

### Transmissor de Dados

| Conector | O que faz |
|---|---|
| Discovery de recursos | Retorna os produtos financeiros do cliente disponíveis para compartilhamento |
| Dados abertos | Retorna produtos e serviços da instituição (sem autenticação) |
| Dados cadastrais | Retorna dados pessoais do cliente (PF e PJ) |
| Dados de contas | Retorna saldos, transações e limites das contas do cliente |
| Dados de cartão de crédito | Retorna faturas, transações e limites de cartões |
| Dados de crédito | Retorna contratos de empréstimos, financiamentos, etc. |
| Dados de investimentos | Retorna posições de renda fixa, variável, fundos, etc. |
| Dados de câmbio | Retorna operações de câmbio do cliente |

---

## Referências

- [Integração da Plataforma — documentação técnica](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/OOF-Integra%C3%A7%C3%A3o.html)
- [Compartilhamento de Dados — APIs de integração](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/CamadaIntegra%C3%A7%C3%A3o.html)
- [Pagamentos — APIs de integração](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/CamadaIntegra%C3%A7%C3%A3oPagamentos.html)
