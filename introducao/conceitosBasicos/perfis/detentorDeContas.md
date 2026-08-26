---
title: "Detentor de Conta"
summary: "O perfil de participação como Detentor de Conta no Open Finance Brasil representa a instituição que recebe solicitações de pagamento de um Iniciador de Trans..."
---

## Detentor de Conta

O perfil de participação como Detentor de Conta no Open Finance Brasil representa a Instituição que recebe solicitações de pagamento de um Iniciador de Transação de Pagamento (ITP). Este perfil na Plataforma Opus Open Finance é responsável por atender todas as exigências regulatórias estabelecidas pelo Banco Central.

### Ecossistema Open Finance - Detentor de Conta

Os Detentores de Contas são as Instituições onde os clientes possuem contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas, que podem ser acessadas no contexto do Open Finance Brasil para processar iniciações de pagamento. Quem envia os pedidos de pagamento são Instituições homologadas como Iniciadoras de Transação de Pagamento.

### Jornada de Consentimento

O processo de autorização para efetuar pagamentos é feito pelo cliente por meio de uma **jornada completa de consentimento**. Mais detalhes podem ser encontrados [aqui](/docs/jornadaconsentimento).

### Roadmap Regulatório

#### Funcionalidades já disponíveis

- Pagamento Pix imediato;
- Pagamento Pix agendado;
- Recorrência de pagamentos agendados;
- Transferências automáticas entre contas de mesma titularidade (recurso também conhecido como *sweeping accounts* ou *transferências inteligentes*);
- Pagamentos sem redirecionamento (ausência do redirecionamento para a Detentora de Conta na perspectiva do usuário);
- Pix por aproximação.

#### Funcionalidades previstas

- Pagamentos em lote (1:n);
- Pagamentos recorrentes (Variable Recurring Payment - VRP - implementado pelo *Pix Automático*).

O [portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/DraftOF/calendars) oferece um calendário com as próximas entregas.

### Plataforma Opus Open Finance

Para utilizar a Plataforma Opus Open Finance para atender às exigências regulatórias do perfil de participação Detentor de Conta, é necessário concluir as seguintes etapas:

1. Completar o processo de [implantação](/docs/implantacaodaplataforma).
2. Construir a experiência do usuário para aplicativo e Internet Banking (se houver). [O guia de experiência do usuário](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/2029715458/v.22.01.00+Guia+de+Experi+ncia+do+Usu+rio) apresenta os detalhes do fluxo de interação com  o usuário final que os canais digitais de atendimento devem implementar para atender às normas regulatórias.
3. Construir a camada de integração com os sistemas de retaguarda de pagamentos.
