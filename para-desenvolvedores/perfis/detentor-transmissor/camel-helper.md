---
layout: default
title: Classe utilitária camelHelper
parent: "Detentor de Conta / Transmissor de Dados"
nav_order: 5
has_children: false
lang: "pt-br"
---

# Classe utilitária camelHelper

O `camelHelper` é uma classe utilitária disponível nos conectores que oferece funções auxiliares para operações comuns no desenvolvimento das rotas Camel.

---

## Como usar

Todas as funções são chamadas via `${bean:camelHelper.<nomeDaFuncao>(...)}` dentro do XML Camel:

```xml
<setProperty name="resultado">
    <simple>${bean:camelHelper.lPad("191", '0', 14)}</simple>
</setProperty>
```

---

## Funções disponíveis

### `lPad(inputString, character, length)`

Completa uma string com um caractere à esquerda até atingir o tamanho especificado.

```xml
<!-- Resultado: 00000000000191 -->
<simple>${bean:camelHelper.lPad("191", '0', 14)}</simple>
```

Se `length` for menor ou igual ao tamanho da string original, retorna a string sem modificação.

---

### `getCurrentZonedDateTime(zone, separator, dateFormat, timeFormat)`

Retorna a data e hora atual em um fuso horário específico.

```xml
<!-- Resultado: 2021-12-21;13-30-00 -->
<simple>${bean:camelHelper.getCurrentZonedDateTime("America/Sao_Paulo", ";", "yyyy-MM-dd", "HH-mm-ss")}</simple>
```

Fuso horários: consulte a [lista de fusos IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

---

### `getUTCFromDateTimeZoned(dateTime, pattern, zoneOrigin)`

Converte uma data/hora de um fuso horário específico para UTC no formato ISO (`yyyy-MM-ddTHH:mm:ssZ`).

```xml
<!-- Resultado: 2021-12-21T16:30:00Z -->
<simple>${bean:camelHelper.getUTCFromDateTimeZoned("21/12/2021 13-30-00", "dd/MM/yyyy HH-mm-ss", "America/Sao_Paulo")}</simple>
```

---

### `getSplittedStringFromPosition(text, separator, position)`

Quebra uma string por um separador e retorna o item na posição indicada (base 0).

```xml
<!-- Resultado: teste -->
<simple>${bean:camelHelper.getSplittedStringFromPosition("teste;quebra;texto", ";", 0)}</simple>
```

Se a posição for maior ou igual ao total de itens, retorna o texto original.

---

### `getStringFromNumberWithPlaces(number, decimalPlaces)`

Formata um número com um número específico de casas decimais.

```xml
<!-- Resultado: 1.100 -->
<simple>${bean:camelHelper.getStringFromNumberWithPlaces("1.1", 4)}</simple>
```

Usa o formato americano (separador decimal `.`). Número inválido retorna string vazia.

---

### `concatenateStrings(s1, s2)`

Concatena duas strings.

```xml
<!-- Resultado: abcd -->
<simple>${bean:camelHelper.concatenateStrings("ab", "cd")}</simple>
```

---

### `hmacCalculator(algorithm, data, key)`

Calcula o hash HMAC de um dado com uma chave secreta.

```xml
<simple>${bean:camelHelper.hmacCalculator("HmacSHA256", "abcd", "bc19bec7-339f-452f-8548-3daa889e6f79")}</simple>
```

Algoritmos suportados: `HmacMD5`, `HmacSHA1`, `HmacSHA224`, `HmacSHA256`, `HmacSHA384`, `HmacSHA512`.

---

### `makePostCall(authorization, transactionHash, contentType, endpoint, payload)`

Realiza uma chamada HTTP POST com suporte a certificado mTLS configurado nas variáveis adicionais do Camel.

```xml
<simple>${bean:camelHelper.makePostCall("", "", ${contentType}, ${endpoint}, ${body})}</simple>
```

---

### `makeGetCall(authorization, transactionHash, contentType, endpoint)`

Realiza uma chamada HTTP GET com suporte a certificado mTLS.

```xml
<simple>${bean:camelHelper.makeGetCall("", "", ${contentType}, ${endpoint})}</simple>
```

---

### `convertFieldToListOfKeyValue(jsonMap, path)`

Transforma um campo de um objeto JSON em uma lista com um único par `{key: "id", value: <valor original>}`. Usado para converter identificadores internos para o formato esperado pela plataforma.

```xml
<unmarshal><json library="Jackson"/></unmarshal>
<setBody>
    <simple>${bean:camelHelper.convertFieldToListOfKeyValue(${body}, "data[-].accountId")}</simple>
</setBody>
<marshal><json library="Jackson"/></marshal>
```

O caminho suporta listas: `data[-]` aplica em todos os itens, `data[0]` aplica apenas no primeiro.

---

### `convertListOfKeyValueToField(jsonMap, path)`

Operação inversa: converte uma lista `[{key: "id", value: "..."}]` de volta para o valor simples.

```xml
<setBody>
    <simple>${bean:camelHelper.convertListOfKeyValueToField(${body}, "data[-].accountId")}</simple>
</setBody>
```

---

### `generateUrlEncodedOrDecodedValue(value, operation)`

Codifica ou decodifica uma string em URL encoding.

```xml
<!-- Resultado: testl%21encode%2Asf13 -->
<simple>${bean:camelHelper.generateUrlEncodedOrDecodedValue("testl!encode*sf13", "ENCODE")}</simple>
```

Operações: `ENCODE` ou `DECODE`.
