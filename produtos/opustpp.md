---
layout: default
title: OpusTPP
parent: Produtos
nav_order: 2
has_children: false
lang: "pt-br"
---

# OpusTPP

O **OpusTPP** é o middleware da Opus Software para instituições que atuam como **Iniciador de Transação de Pagamento (ITP)** e/ou **Receptor de Dados** no Open Finance Brasil.

Seu propósito é simples: permitir que a instituição consuma APIs regulatórias complexas como se fossem APIs REST tradicionais, enquanto o OpusTPP cuida de toda a camada de segurança, autenticação e conformidade regulatória.

---

## O problema que resolve

Para consumir serviços do Open Finance Brasil — seja iniciar um pagamento ou obter dados de um cliente — uma instituição precisaria implementar diretamente uma série de requisitos técnicos e regulatórios:

- Padrões de segurança avançados (FAPI-BR, DCR, certificados específicos)
- Gerenciamento de tokens de acesso por instituição
- Fluxos completos de solicitação, aprovação e consumo de consentimentos
- Diferenças operacionais entre cada Transmissora ou Detentora
- Atualização contínua com as mudanças regulatórias

O OpusTPP assume toda essa complexidade. A instituição interage com uma API REST simples e o OpusTPP faz o restante — incluindo DCR automático em todas as Detentoras e Transmissoras listadas no Diretório de Participantes.

---

## Módulos disponíveis

O OpusTPP é composto por dois módulos que podem ser adquiridos independentemente:

### Iniciador de Transação de Pagamento (ITP)

Suporta a iniciação, execução e acompanhamento de transações de pagamento Pix, incluindo toda a jornada de criação e consumo de consentimentos.

**O que o módulo faz:**
- Criação de consentimento de pagamento em uma única requisição REST
- Gerenciamento automático dos tokens de acesso por Detentora
- Iniciação do pagamento Pix após aprovação do consentimento
- Consulta de status do pagamento
- Revogação de pagamentos agendados
- Suporte a pagamentos automáticos (Pix Automático / Transferências Inteligentes)
- Suporte a pagamento sem redirecionamento via FIDO2 (vínculo de dispositivo)
- DCR e DCM automáticos em todas as Detentoras do Diretório
- Envio automático de reportes à PCM

**Casos de uso:**

- **Pagamento Pix imediato**: o cliente da instituição ITP seleciona a Detentora, autoriza o consentimento nos canais dela e o pagamento é efetivado em tempo real.
- **Pagamento Pix agendado**: consentimento criado hoje, pagamento executado em data futura — com possibilidade de cancelamento antes da liquidação.
- **Pix Automático (recorrente)**: consentimento de longa duração que autoriza débitos periódicos, ideal para assinaturas, mensalidades e cobranças recorrentes.
- **Transferências inteligentes**: autorização de transferências automáticas entre contas de mesma titularidade em diferentes instituições.
- **Pagamento sem redirecionamento (FIDO2)**: após vínculo de dispositivo estabelecido, o cliente autoriza pagamentos com biometria — sem redirecionar ao app da Detentora a cada transação.
- **Jornada Otimizada**: combina consentimento de pagamento e consentimento de dados em um único fluxo, permitindo verificação de saldo antes da execução do pagamento.

### Receptor de Dados Cadastrais e Transacionais

Suporta a solicitação e obtenção de dados financeiros de clientes junto às Transmissoras de Dados.

**O que o módulo faz:**
- Criação de consentimento de dados em uma única requisição REST
- Exposição de endpoints proxy que se comportam como as APIs regulatórias das Transmissoras
- Gerenciamento automático de tokens por Transmissora
- Suporte a renovação de consentimentos sem novo fluxo de autorização completo
- DCR e DCM automáticos em todas as Transmissoras do Diretório
- Envio automático de reportes à PCM

**Dados acessíveis após consentimento autorizado:**

| Categoria | O que inclui |
|---|---|
| Dados cadastrais | Informações pessoais PF e PJ |
| Contas | Saldos, transações, limites, saldo reservado |
| Cartão de crédito | Faturas, transações, limites |
| Empréstimos | Contratos, prestações, pagamentos, garantias |
| Financiamentos | Contratos, prestações, pagamentos, garantias |
| Adiantamento a depositantes | Contratos |
| Direitos creditórios descontados | Contratos |
| Renda fixa bancária | Posições e movimentações |
| Renda fixa crédito | Posições e movimentações |
| Renda variável | Posições e movimentações |
| Fundos de investimento | Posições e movimentações |
| Tesouro Direto | Posições e movimentações |
| Câmbio | Operações |

**Casos de uso:**

- **Portabilidade de crédito**: obter dados de crédito do cliente em outras instituições para oferecer condições mais competitivas.
- **Análise de crédito enriquecida**: acessar o histórico financeiro completo do cliente (contas, cartões, contratos) para decisões de crédito mais precisas.
- **Gestão financeira pessoal (PFM)**: consolidar todas as contas e investimentos do cliente em diferentes instituições em uma única visão.
- **Verificação de saldo pré-pagamento**: na Jornada Otimizada, verificar saldo disponível antes de iniciar um pagamento.

---

## O que o OpusTPP não faz

- Não atua como instituição regulada — a responsabilidade regulatória permanece com a Instituição Cliente
- Não substitui sistemas internos, cores bancários ou lógica de negócio
- Não cria experiências de usuário final para consentimento
- Não garante a certificação da instituição nos ambientes regulatórios
- Não realiza análises ou interpreta os dados financeiros obtidos
- Não executa liquidação financeira ou processamento próprio de transações

---

## Referências

- [Documentação técnica do OpusTPP](../opusTPP/index.html)
- [Fluxo de consentimentos](../opusTPP/funcionamento/index.html)
- [Iniciação de pagamento](../opusTPP/funcionamento/iniciacaoDePagamento.html)
- [Recepção de dados](../opusTPP/funcionamento/recepcaoDeDados.html)
- [Checklist de implantação — ITP](../implantacao/integracao/itp/checklist.html)
- [Checklist de implantação — Receptor de Dados](../implantacao/integracao/receptor/checklist.html)
