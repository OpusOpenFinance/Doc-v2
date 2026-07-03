---
layout: default
title: Detentor de Conta / Transmissor de Dados
parent: Para Desenvolvedores
nav_order: 1
has_children: true
lang: "pt-br"
---

# Desenvolvimento — Detentor de Conta / Transmissor de Dados

Para os perfis de Detentor de Conta e Transmissor de Dados, o desenvolvimento consiste em criar **conectores Camel** que integram a Plataforma Opus Open Finance com os sistemas de retaguarda da instituição.

---

## Divisão de responsabilidades

**A plataforma (OOB) é responsável por:**
- Verificar se existe consentimento válido para a requisição recebida
- Validar o request contra as especificações do Open Finance Brasil
- Mapear IDs de recursos entre o formato OFB e o formato interno da instituição
- Converter a resposta do conector para o formato regulatório
- Retornar os erros no formato exigido pelo OFB em caso de falha
- Toda a segurança regulatória (FAPI-BR, assinaturas, certificados)

**O conector (desenvolvido pela instituição) é responsável por:**
- Implementar a interface de entrada definida pela plataforma
- Fazer as chamadas aos sistemas legados da instituição
- Retornar a resposta no formato definido pela plataforma
- Controlar idempotência nas operações que exigem
- Consultar o objeto de consentimento quando necessário para decidir quais dados retornar

---

## Como o carregamento funciona

O carregamento do conector é feito em **tempo de execução**. A plataforma busca os arquivos de rota Camel no diretório `/work` da imagem Docker. O conector é desenvolvido como uma extensão da imagem base da Opus:

```dockerfile
FROM 618430153747.dkr.ecr.sa-east-1.amazonaws.com/opus-open-banking-release/<servico>:latest

COPY ./meu-conector/rotas/ /work/
```

A variável de ambiente `camel.main.routes-include-pattern` controla onde a plataforma procura as rotas, caso o diretório padrão seja alterado.

---

## Tratamento de erros

Em caso de falha, o objeto retornado pelo conector deve seguir o schema de erro definido pela plataforma (`response-error-schema.json`).

Duas regras importantes:
- Mensagens de erro podem ser exibidas na tela do usuário ou retornadas ao TPP — não inclua erros técnicos nas descrições. Use linguagem que o usuário possa entender, como "não foi possível realizar a operação, tente novamente".
- Erros de sistema (códigos 5xx) são contabilizados como indisponibilidade nos cálculos de SLA — minimize-os.

---

## Configuração de timeout

Configure timeouts nas chamadas HTTP do conector em milissegundos:

```xml
<route id="getCustomersPersonalQualificationsRoute">
    <from uri="direct:getCustomersPersonalQualifications"/>
    <to uri="https://endpoint.dominio?bridgeEndpoint=true&amp;socketTimeout=5000"/>
</route>
```

Para usar variável de ambiente:

```xml
<to uri="https://endpoint.dominio?bridgeEndpoint=true&amp;socketTimeout={{env:SOCKET_TIMEOUT}}"/>
```

Tipos de timeout disponíveis:
- `connectionRequestTimeout` — tempo para obter uma conexão do pool de conexões
- `connectTimeout` — tempo para estabelecer a conexão TCP
- `socketTimeout` — tempo máximo de inatividade entre pacotes de dados

Quando o timeout é excedido, a plataforma retorna HTTP 500 com mensagem genérica.

---

## Componente HTTP recomendado: Netty HTTP

Para requisições HTTP nos conectores, o componente **Netty HTTP** é o recomendado por proporcionar comunicação não bloqueante e maior eficiência em cenários de alto volume.

Exemplo de rota com Netty HTTP (POST):

```xml
<route id="discoveryLoansRoute">
    <from uri="direct:discoverLoans"/>
    <setHeader name="Content-Type"><constant>application/json</constant></setHeader>
    <setHeader name="Accept"><constant>application/json</constant></setHeader>
    <setHeader name="CamelHttpMethod"><constant>POST</constant></setHeader>
    <toD uri="netty-http:{{host}}/api/v1/loans?bridgeEndpoint=true&amp;throwExceptionOnFailure=false&amp;encoding=UTF-8"/>
</route>
```

Para chamadas GET, defina body vazio para evitar envio de payload:

```xml
<setBody><constant></constant></setBody>
<toD uri="netty-http:{{host}}/api/v1/accounts?bridgeEndpoint=true&amp;throwExceptionOnFailure=false&amp;encoding=UTF-8"/>
```

> O componente HTTP clássico (Apache HttpClient) ainda é suportado para necessidades simples. O Vertx HTTP também está disponível para cenários reativos.

---

## Tratamento de headers

Os headers recebidos pela plataforma no request REST são repassados para o conector no contexto Camel. Headers FAPI, user agent e outros gerados pelo TPP ou infraestrutura ficam disponíveis. Para acessar um header no XML Camel:

```xml
<simple>${header.nomeDoHeader}</simple>
```

---

## Conectores por perfil

- [Discovery de Recursos](discovery.html) — obrigatório para Detentor e Transmissor
- [Pagamentos (Detentor de Conta)](pagamentos.html) — conectores Pix
- [Dados Abertos (Transmissor)](open-data.html) — produtos e serviços públicos
- [Dados Financeiros (Transmissor)](financial-data.html) — dados cadastrais e transacionais

---

## Referências

- [Componentes Camel suportados](componentes.html)
- [Classe utilitária camelHelper](camel-helper.html)
- [Connector Tester](../ferramentas/connector-tester.html)
