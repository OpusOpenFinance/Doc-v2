---
layout: default
title: Componentes Camel Suportados
parent: "Detentor de Conta / Transmissor de Dados"
nav_order: 6
has_children: false
lang: "pt-br"
---

# Componentes e Data Formats Suportados

A plataforma usa Apache Camel com Quarkus. Os componentes, data formats e linguagens abaixo estão disponíveis para uso nos conectores.

---

## Componentes HTTP (recomendações)

Para requisições HTTP aos sistemas de retaguarda, use preferencialmente o **Netty HTTP** por sua comunicação não bloqueante e maior eficiência em alto volume. O HTTP clássico (Apache HttpClient) e o Vertx HTTP também são suportados.

| Componente | Indicado para | Documentação |
|---|---|---|
| **Netty HTTP** *(recomendado)* | Alto volume, comunicação não bloqueante | [docs](https://camel.apache.org/components/3.21.x/netty-http-component.html) |
| HTTP | Necessidades simples | [docs](https://camel.apache.org/camel-quarkus/latest/reference/extensions/http.html) |
| Vertx HTTP | Aplicações reativas | [docs](https://camel.apache.org/components/3.21.x/vertx-http-component.html) |

---

## Componentes disponíveis

| Componente | Descrição |
|---|---|
| **ACTIVEMQ** | Envio e consumo de mensagens Apache ActiveMQ |
| **AMQP** | Mensagens com protocolo AMQP via Apache QPid Client |
| **ATLASMAP** | Transformação de mensagens com AtlasMap |
| **DATA FORMAT** | Uso de Data Formats como componentes Camel |
| **DIRECT** | Chamada síncrona a outro endpoint no mesmo Camel Context |
| **ELASTICSEARCH REST** | Requisições ao ElasticSearch via REST API |
| **EXEC** | Execução de comandos no sistema operacional |
| **FILE** | Leitura e escrita de arquivos |
| **HTTP** | Requisições HTTP via Apache HTTP Client 4.x |
| **JING** | Validação XML contra schema RelaxNG |
| **LOG** | Log de mensagens |
| **MOCK** | Mocks para testes de rotas |
| **MSV** | Validação XML com Multi-Schema Validator |
| **PLATFORM HTTP** | Criação de endpoints HTTP para consumir requisições |
| **REF** | Roteamento dinâmico por nome no Camel Registry |
| **REST** | Exposição de serviços REST ou chamadas a serviços externos |
| **SEDA** | Chamada assíncrona a endpoints no mesmo JVM |
| **TIMER** | Geração de mensagens em intervalos específicos |
| **VALIDATOR** | Validação de payload com XML Schema (JAXP) |
| **VELOCITY** | Transformação de mensagens com templates Velocity |
| **VM** | Chamada assíncrona a outro endpoint no mesmo CamelContext |

---

## Data Formats disponíveis

| Data Format | Descrição |
|---|---|
| **Jackson** | Conversão POJO ↔ JSON com Jackson |
| **Gson** | Conversão POJO ↔ JSON com Gson |
| **CSV** | Manipulação de arquivos CSV |
| **Flatpack** | Arquivos posicionais com FlatPack |
| **Bindy** | Conversão POJO ↔ CSV/posicional/KVP |
| **TidyMarkup** | Organização de HTML com TagSoup |
| **BASE64** | Codificação e decodificação Base64 |
| **JACKSONXML** | Conversão POJO ↔ XML com Jackson XMLMapper |

---

## Linguagens disponíveis

| Linguagem | Descrição |
|---|---|
| **Bean Method** | Chamada a métodos de beans Java com o Exchange |
| **CORE** | Funcionalidades essenciais: Constant, Header, Simple, ExchangeProperty, Ref, Tokenize |
| **HL7 Terser** | Manipulação de objetos HL7 (Health Care) |
| **JSON PATH** | Validação de expressões JsonPath contra JSON |
| **XML JAXP** | Tokenização de XML por expressão de caminho |
| **XPATH** | Validação de expressões XPath contra XML |
| **XQUERY** | Consulta e transformação de XML com XQuery/Saxon |
