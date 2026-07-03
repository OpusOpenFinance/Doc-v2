---
layout: default
title: Receptor de Dados
parent: Para Desenvolvedores
nav_order: 2
has_children: false
lang: "pt-br"
---

# Desenvolvimento — Receptor de Dados

Para o perfil de Receptor de Dados, **não é necessário desenvolver conectores Camel**. A integração é feita diretamente com as APIs REST do OpusTPP.

O OpusTPP abstrai toda a complexidade regulatória — autenticação, DCR, gerenciamento de tokens, assinaturas criptográficas. Do ponto de vista do desenvolvedor, o trabalho consiste em:

1. Integrar a aplicação com as APIs REST do OpusTPP
2. Implementar o redirecionamento do usuário (App-to-App ou Web) para o fluxo de autorização de consentimento
3. Processar o retorno do fluxo e chamar o endpoint `authorization-result`
4. Consumir os dados via endpoints proxy do OpusTPP

---

## O que desenvolver

### Integração com a API do OpusTPP

| Etapa | Endpoint |
|---|---|
| Listar participantes disponíveis | `GET /opus-open-finance/participants` |
| Criar consentimento de dados | `POST /opus-open-finance/consents/v1/consents` |
| Retornar resultado da autorização | `POST /opus-open-finance/authorization-result` |
| Consultar status do consentimento | `GET /opus-open-finance/consents/v1/consents/{consentId}` |
| Obter dados via proxy | `GET /proxy/open-banking/<família>/<versão>/<endpoint>` |

### Redirecionamento mobile (se aplicável)

Se a aplicação for mobile, é necessário configurar Android App Links e iOS Universal Links para interceptar as URLs de retorno do fluxo de consentimento. Consulte [Redirecionamento App-to-App](../../opusTPP/funcionamento/redirecionamento.html).

### Definição de permissões

Ao criar o consentimento, as permissões precisam seguir os agrupamentos obrigatórios definidos pelo Open Finance Brasil. Consulte [Permissões e Agrupamentos](../../opusTPP/conceitos/permissoesOpenFinance.html).

---

## Referências

- [Recepção de Dados — documentação OpusTPP](../../opusTPP/funcionamento/recepcaoDeDados.html)
- [Fluxo de consentimentos — OpusTPP](../../opusTPP/funcionamento/index.html)
- [Redirecionamento App-to-App](../../opusTPP/funcionamento/redirecionamento.html)
- [Mockbank — testes em homologação](../../opusTPP/ferramentasAuxiliares/mockbank.html)
- [Checklist de implantação — Receptor de Dados](../../implantacao/integracao/receptor/checklist.html)
