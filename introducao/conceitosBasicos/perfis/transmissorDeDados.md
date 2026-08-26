---
title: "Transmissor de Dados"
summary: "O perfil de Transmissor de Dados representa a instituição que recebe solicitações de compartilhamento de dados de um Receptor de Dados. A Plataforma Opus Ope..."
---

## Transmissor de Dados

O perfil de **Transmissor de Dados** representa a Instituição que recebe solicitações de compartilhamento de dados de um **Receptor de Dados**. A **Plataforma Opus Open Finance** atende a todas as exigências regulatórias estabelecidas pelo regulatório do *Open Finance Brasil* para a implementação desse perfil.

---

### Ecossistema Open Finance Brasil - Transmissor de Dados

O perfil de *Transmissor de Dados* diz respeito às Instituições Financeiras que participam do compartilhamento de dados no *Open Finance Brasil*. Tipicamente, ele é acionado quando clientes da Instituição concedem consentimentos de compartilhamento de dados a outras Instituições que, nesse contexto, são chamadas de *Instituições Receptoras de Dados*.

Uma vez que o cliente aceitou compartilhar seus dados com outras Instituições, essas passam a ter o direito de enviar periodicamente requisições de dados que podem incluir dados cadastrais do cliente, transações de conta e de cartões de crédito, operações de crédito, câmbio e investimentos (veja mais adiante). O perfil de *Transmissor de Dados* é justamente o responsável por receber, validar e atender essas requisições.

> A norma regulatória estabelece limites, chamados de *limites operacionais*, que estabelecem cotas máximas de requisições que uma Instituição Receptora de Dados pode enviar para uma Instituição Transmissora de Dados. Os limites operacionais atualmente vigentes no *Open Finance Brasil* podem ser encontrados [aqui][Limites-operacionais].  

---

### Dados Compartilhados

Quando ocorre um compartilhamento, o ecossistema é preparado para fornecer as seguintes informações:

#### **Dados cadastrais do correntista**

- Dados cadastrais.

#### **Conta Corrente**

- Extrato;
- Saldo.

#### **Cartão de crédito**

- Fatura;
- Limites;
- Transações.

#### **Operações de crédito**

- Empréstimos;
- Financiamentos;
- Adiantamento a depositantes (cheque especial);
- Direitos creditórios descontados (antecipação de recebíveis).

#### **Câmbio**

- Operações de câmbio.

#### **Investimentos**

- Renda fixa bancária (CDB, LCI, LCA - protegidos pelo FGC);
- Renda fixa crédito (CRI, CRA, Debenture);
- Renda variável;
- Títulos do tesouro direto;
- Fundos de investimento;

**Nota:** É responsabilidade do **Transmissor de Dados** fornecer todas as informações listadas acima que são oferecidas pela Instituição.

---

### Jornada de Consentimento

O processo de autorização para compartilhamento de dados segue uma **jornada completa de consentimento**. Para mais informações, clique [aqui][JornadaConsentimento].

---

### Roadmap regulatório

#### Funcionalidades já disponíveis

- Consulta de todos os dados listados acima.

#### Funcionalidades previstas

- Sistemática de notificações: existe um desejo de aumentar a eficiência do compartilhamento de dados. Atualmente, para saber se um cliente realizou novas transações em um determinado período, é necessário explicitamente realizar uma chamada à Instituição Financeira Transmissora de Dados periodicamente. A sistemática de notificações deverá permitir ao Receptor de Dados indicar ao Transmissor quais os clientes - dos quais ele já possui consentimento de compartilhamento de dados válidos - ele gostaria de monitorar. Dessa forma, periodicamente - provavelmente uma vez por dia - o Transmissor poderá enviar diretamente ao Receptor as eventuais transações ou alterações de dados cadastrais realizadas pelo cliente. Esse mecanismo certamente economizará inúmeras chamadas desnecessárias, reduzindo o custo para todos os participantes do ecossistema.

O [portal do desenvolvedor][Portal-Desenvolvedor] também oferece um calendário com as próximas entregas.

### Plataforma Opus Open Finance

A **Plataforma Opus Open Finance** implementa todas as APIs regulatórias do perfil Transmissor de Dados. Para operacionalizar esse perfil utilizando a plataforma, é necessário:

1. Completar todo o processo de [implantação][Implantação].
2. Construir, para o aplicativo móvel e Internet Banking (se houver), a experiência de usuário referente à concessão de consentimentos de compartilhamento de dados, conforme definido pelo regulatório do *Open Finance Brasil*. [O Guia de Experiência do Usuário][GuiaUX] dá mais detalhes sobre o fluxo de interação com o usuário que deve ser implementado.
3. Construir a [camada de integração][Camada-Integração] com os sistemas de retaguarda conforme os produtos financeiros oferecidos pela Instituição para seus clientes.

[Limites-operacionais]: https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17924220/Limites+operacionais
[JornadaConsentimento]: /docs/jornadaconsentimento
[Portal-Desenvolvedor]: https://openfinancebrasil.atlassian.net/wiki/spaces/DraftOF/calendars
[Implantação]: /docs/implantacaodaplataforma
[GuiaUX]: https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/1477279745/v.19.00.01+Guia+de+Experi+ncia+do+Usu+rio+Open+Finance+Brasil
[Camada-Integração]: /docs/camadaintegracao