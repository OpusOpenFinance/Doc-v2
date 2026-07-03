---
layout: default
title: Connector Tester
parent: Para Desenvolvedores
nav_order: 5
has_children: false
lang: "pt-br"
---

# Connector Tester

O **Connector Tester** é uma ferramenta Docker que permite testar os conectores Camel de forma isolada — sem precisar de um ambiente completo do Open Finance nem de conexões reais com outras instituições.

Ela simula as chamadas que os módulos da plataforma fariam aos conectores, permitindo que o desenvolvimento e depuração aconteçam localmente, antes de qualquer integração com o ambiente de homologação.

---

## O que a ferramenta faz

A ferramenta expõe endpoints REST que representam todos os pontos de integração dos módulos da plataforma. Cada endpoint recebe o mesmo objeto JSON que o módulo real enviaria ao conector — incluindo o consentimento, headers e demais informações de contexto. A ferramenta então chama as rotas Camel do conector e retorna o resultado.

A ferramenta suporta testes de conectores de `payments` e `financial-data`. Os exemplos fornecidos para `financial-data` cobrem o subgrupo de Accounts; os demais produtos são análogos.

---

## Como obter a imagem

A imagem está disponível no ECR da Opus:

```sh
docker pull 618430153747.dkr.ecr.sa-east-1.amazonaws.com/opus-open-banking-release/oob-connector-tester:latest
```

---

## Como executar sem conector

Para explorar os endpoints disponíveis antes de integrar um conector:

```sh
docker run -it -p 8080:8080 \
  618430153747.dkr.ecr.sa-east-1.amazonaws.com/opus-open-banking-release/oob-connector-tester:latest
```

Após iniciar, acesse `http://localhost:8080/swagger-ui` para visualizar e testar os endpoints disponíveis.

---

## Como integrar o conector

O conector é integrado estendendo a imagem base:

```dockerfile
FROM 618430153747.dkr.ecr.sa-east-1.amazonaws.com/opus-open-banking-release/oob-connector-tester:latest

# Copiar os arquivos de rota e templates do conector
COPY ./conector/specs/ /work/specs/
COPY ./conector/connectorCustom/ /work/connectorCustom/
```

### Estrutura de arquivos esperada

```
connectorCustom/
├── accounts/          # Templates e mapeamentos para endpoints de contas
│   ├── getAccounts/
│   ├── getAccountsAccountIdBalances/
│   └── ...
├── payments/          # Templates e mapeamentos para endpoints de pagamento
│   ├── postPixPayments/
│   └── ...
└── specs/             # Arquivos de rotas Camel XML
    └── *.xml
```

Os arquivos de rota Camel XML são os mesmos que serão usados no ambiente de produção — não é necessário criar rotas diferentes para teste.

---

## Executando os testes

Com a imagem estendida construída:

```sh
docker build -t meu-conector-tester .
docker run -it -p 8080:8080 meu-conector-tester
```

Acesse o Swagger em `http://localhost:8080/swagger-ui`, selecione o endpoint que deseja testar, preencha o payload de entrada com os dados de contexto (consentimento, parâmetros, etc.) e execute. O resultado mostrará o que o conector retornou.

---

## Referências

- [Desenvolvimento de conectores — Detentor/Transmissor](../perfis/detentor-transmissor/index.html)
- [Validações de Pagamentos](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Plataforma-OpusOpenFinance/Integra%C3%A7%C3%A3o/Pagamentos/integracao-plugin/validacoes-pagamentos/Validacoes-Pagamentos.html)
