---
layout: default
title: Discovery de Recursos
parent: "Detentor de Conta / Transmissor de Dados"
nav_order: 1
has_children: false
lang: "pt-br"
---

# Discovery de Recursos

O discovery de recursos é o ponto de integração responsável por identificar quais produtos financeiros do cliente estão vinculados a um consentimento. É obrigatório para Detentores de Conta e Transmissores de Dados.

---

## Quando o discovery ocorre

O discovery acontece em dois momentos distintos:

### Produtos selecionáveis

Ocorre durante a fase de autorização do consentimento pelo cliente. Nesses casos, o cliente precisa escolher ativamente quais instâncias do produto serão compartilhadas. A plataforma chama o conector para listar as opções disponíveis.

| Tipo de consentimento | Produto | Rota Camel |
|---|---|---|
| Compartilhamento de dados | Conta | `direct:discoverAccounts` |
| Compartilhamento de dados | Cartão de crédito | `direct:discoverCreditCardAccounts` |
| Pagamento | Conta de pagamento | `direct:discoverPayments_v2` |

### Produtos não selecionáveis

Ocorre durante a utilização do consentimento, quando a plataforma precisa identificar os recursos vinculados para executar a operação. O cliente não participa ativamente — o conector simplesmente retorna a lista de recursos disponíveis.

---

## Formato dos conectores

### Produto selecionável

O conector recebe um objeto de request e deve retornar a lista de recursos disponíveis para seleção:

**Request:** segue o schema `discovery-resource-request.json`

**Response esperado:**

```json
{
  "resources": [
    {
      "resourceName": [
        { "key": "Agencia", "value": "1234" },
        { "key": "Conta Corrente", "value": "12345-6" }
      ],
      "resourceLegacyId": [
        { "key": "pkAgencia", "value": "1234" },
        { "key": "pkContaCorrente", "value": "123456" }
      ],
      "resourceBalanceCurrency": "BRL",
      "resourceBalanceAmount": 239.12,
      "authorizers": [
        { "cpf": "06672639004", "name": "João da Silva" }
      ],
      "defaultSelected": true
    }
  ]
}
```

- `resourceName`: lista de pares chave-valor que identificam o recurso para exibição ao cliente
- `resourceLegacyId`: identificadores internos do recurso nos sistemas legados (usados pela plataforma para mapeamento)
- `resourceBalanceCurrency` / `resourceBalanceAmount`: saldo para exibição ao cliente (opcional, mas recomendado para pagamentos)
- `authorizers`: titulares e co-titulares do recurso
- `defaultSelected`: se o recurso deve vir pré-selecionado na tela

> Se a instituição não disponibilizar um determinado produto (não criar a rota Camel correspondente), o retorno padrão do discovery é nulo e a plataforma não exibirá esse produto ao cliente.

---

## Conector de validação de dados de pagamento

Para consentimentos de pagamento, além do discovery de recursos existe um conector de validação que permite à instituição aprovar ou rejeitar a criação do consentimento com base em regras de negócio próprias (ex.: conta bloqueada, limites excedidos).

Consulte a documentação técnica completa de rotas e schemas na [seção de Integração da Plataforma](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/consent/Discovery-Recursos.html).

---

## Referências

- [Discovery de Recursos — documentação técnica](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/consent/Discovery-Recursos.html)
- [Connector Tester](../../ferramentas/connector-tester.html)
