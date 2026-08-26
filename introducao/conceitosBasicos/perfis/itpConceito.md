---
title: "ITP"
summary: "O Iniciador de Transação de Pagamento (ITP) é o perfil do Open Finance Brasil autorizado a realizar iniciações de pagamento no ecossistema. O ITP conduz jorn..."
---

## Iniciador de Transação de Pagamentos

O Iniciador de Transação de Pagamento (ITP) é o perfil do Open Finance Brasil autorizado a realizar iniciações de pagamento no ecossistema. O ITP conduz jornadas de consentimento para a realização de pagamentos junto a Instituições participantes do Open Finance que possuem o perfil Detentor de Conta. Esse perfil possibilita uma série de novos casos de uso, pois o ITP faz a ponte entre a Instituição e o Cliente, não precisando possuir a custódia dos recursos em nenhum momento da transação e não sendo o titular da conta corrente que realizará a liquidação do pagamento.

### Ecossistema Open Finance - ITP

O perfil de ITP diz respeito às Instituições Financeiras autorizadas pelo Banco Central a iniciar pagamentos no Open Finance Brasil em nome de seus clientes. Para tanto, o ITP obtém o consentimento do usuário pagador e, com base nesse consentimento, instrui a Instituição Detentora de Conta a processar a transação.

A norma regulatória estabelece requisitos de certificação e homologação que precisam ser cumpridos antes de uma instituição poder operar como ITP em produção com sua própria licença. O processo completo está descrito na página de [onboarding do ITP][OnboardingITP].

### Jornada de Consentimento

O processo de autorização para efetuar pagamentos é realizado pelo cliente por meio de uma jornada completa de consentimento. Mais detalhes podem ser encontrados [aqui][Jornada-Consentimento].

> O [diagrama de sequência][Diagrama-Sequência] ilustra o fluxo de consentimento de acordo com cada modalidade de pagamento.

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

Para utilizar a Plataforma Opus Open Finance no perfil de ITP, é necessário concluir as seguintes etapas:

1. Completar o processo de [implantação][Setup].
2. Ter completado toda a homologação do perfil de Detentor de Conta. (recomendamos a avaliação desse critério com o compliance de sua instituição)
3. Construir a experiência de usuário para que a jornada de consentimento seja possível para os clientes. O [Guia de Experiência do Usuário do Open Finance Brasil][GuiaUX] traz uma descrição detalhada sobre essa jornada.
4. Caso utilize sua própria licença, completar todo o processo de [onboarding de ITP][OnboardingITP].

[GuiaUX]: https://guia-de-ux-open-finance-brasil.scroll.site/guia-de-experi-ncia-open-finance-brasil/v.22.00.01
[Portal-Dev]: https://openfinancebrasil.atlassian.net/wiki/spaces/DraftOF/calendars
[OnboardingITP]: /docs/onboarding
[Setup]: /docs/implantacaodaplataforma
[Jornada-Consentimento]: /docs/jornadaconsentimento
[Diagrama-Sequência]: ./anexos/imagens/itp-consentSequence.png