---
title: "Dados abertos"
summary: "A frente de dados abertos do Open Finance faz referência à fase 1 do Open Finance. A Fase 1 possibilita que as instituições participantes do Open Finance pub..."
---

## Dados abertos

A frente de dados abertos do Open Finance faz referência à [Fase 1 do Open Finance](/docs/ecossistema). A Fase 1 possibilita que as Instituições participantes do Open Finance publiquem seus dados de forma pública e acessível via API, para que qualquer requisição possa recuperar essas informações. Os dados são referentes a informações não sensíveis das próprias Instituições.

### Dados listados

#### Canais de atendimento

- Dependências próprias, incluindo a lista de agências bancárias mantidas pela Instituição;
- Canais de atendimento eletrônico;
- Canais de atendimento telefônico;
- Correspondentes bancários da instituição;
- Terminais de autoatendimento (próprios e compartilhados).

#### Produtos

- Contas;
- Empréstimos;
- Financiamentos;
- Antecipação de recebíveis;
- Cartão de crédito;
- Adiantamento a depositantes;
- Investimentos;
- Câmbio;
- Credenciamento;
- Títulos de capitalização;
- Seguros;
- Previdência.

> - No caso dos produtos financeiros, todos devem ser separados entre Pessoa Fisica e Jurídica.

### Critério de obrigatoriedade

O perfil de dados abertos é obrigatório a todas as instituições que são participantes (obrigatórios ou voluntários) do perfil de dados transacionais (Fase 2).

### Plataforma Opus Open Finance

A **Plataforma Opus Open Finance** implementa a API de dados abertos e basta uma integração muito simples para que a Fase 1 esteja operacional, além das seguintes etapas:

1. Ter concluído a [implantação do produto][Implantação].

2. Realizar a integração em conjunto à integração do Transmissor de Dados, sendo ideal que ambos os perfis entrem em produção ao mesmo tempo.

> A integração é realizada por meio de uma estrutura em formato JSON gerada dinâmica ou estaticamente para reportar os dados ao ecossistema do Open Finance Brasil.

[Implantação]: /docs/implantacaodaplataforma