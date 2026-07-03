---
layout: default
title: Certificados Digitais
parent: Implantação
nav_order: 1
has_children: false
lang: "pt-br"
---

# Certificados Digitais

Para participar do Open Finance Brasil, todas as instituições precisam obter **certificados digitais** emitidos por autoridades certificadoras ICP-Brasil. Eles garantem a autenticidade das comunicações e a identidade de cada participante no ecossistema.

> **Certificados ≠ Certificações.** Certificados são arquivos criptográficos emitidos por uma autoridade certificadora. Certificações são as aprovações regulatórias obtidas após passar nos testes de conformidade. Esta página trata dos certificados.

---

## Os quatro tipos de certificado

### BRCAC — Certificado de Transporte
Usado nas conexões **mTLS** (mutual TLS) para identificar a aplicação cliente e criptografar a comunicação entre os participantes. No formato JWK, tem `"use": "enc"`.

Funções:
- Autentica o canal mTLS
- Realiza autenticação da aplicação cliente via OAuth 2.0 mTLS ou `private_key_jwt`

### BRSEAL — Certificado de Assinatura
Usado para **assinar mensagens** JWS trocadas entre a aplicação e o servidor de autenticação. No formato JWK, tem `"use": "sig"`.

Funções:
- Assina os payloads das requisições regulatórias
- Assina tokens JWS

### EV — Certificado de Validação Estendida
Usado nos endpoints que hospedam **interfaces web para clientes** da instituição (páginas de consentimento, portais). Exigência da seção 5.2.4 das especificações de segurança do Open Finance Brasil.

Funções:
- Protege as URLs de front-end acessadas pelos usuários finais
- Obrigatório para o Authorization Server e páginas de consentimento expostas ao cliente

### MTLS — Certificado de Servidor ICP-Brasil
Certificado de servidor instalado nos endpoints que exigem comunicação mTLS entre instituições. Segue a especificação de certificado de servidor da ICP-Brasil (seção 5.2.1 das especificações de segurança do Open Finance Brasil).

Funções:
- Protege os endpoints de Resource Server (APIs regulatórias não abertas)
- Protege o Authorization Server no endpoint mTLS

---

## Quais certificados cada perfil precisa

| Certificado | Detentor de Conta | Transmissor de Dados | ITP | Receptor de Dados |
|---|:---:|:---:|:---:|:---:|
| **BRCAC** (transporte/cliente) | ✅ | ✅ | ✅ | ✅ |
| **BRSEAL** (assinatura) | ✅ | ✅ | ✅ | ✅ |
| **EV** (front-end/portal) | ✅ | ✅ | ⚠️ | ⚠️ |
| **MTLS** (servidor ICP-Brasil) | ✅ | ✅ | — | — |

> ⚠️ ITP e Receptor de Dados precisam de certificado EV se expuserem páginas web para usuários finais. Se a solução for 100% mobile sem front-end web próprio, pode não ser necessário.

---

## Domínios e endpoints associados

A tabela abaixo mostra quais componentes da plataforma requerem cada tipo de certificado (para Detentor de Conta e Transmissor de Dados):

| Componente | Obrigatório | Tipo de certificado | Exemplo de domínio |
|---|---|---|---|
| Authorization Server (público) | Sim | EV ou HTTPS | `https://as-obb.banco.com.br` |
| Authorization Server (mTLS) | Sim | MTLS + ICP-Brasil | `https://matls-as-obb.banco.com.br` |
| Authorization Server | Sim | BRSEAL (assinatura) | — |
| Resource Server — dados abertos | Sim | HTTPS padrão | `https://api.banco.com.br` |
| Resource Server — APIs regulatórias | Sim | MTLS + ICP-Brasil | `https://matls-api.banco.com.br` |
| Portal Backoffice | Opcional | HTTPS padrão | `https://interno.banco.com.br/backoffice` |
| Portal Gestão de Consentimento | Opcional | EV | `https://www.banco.com.br/gestaoconsentimento` |

### Unificação de FQDNs (recomendada)

É possível consolidar todos os endpoints em dois FQDNs, reduzindo o número de certificados necessários:

- `openbanking.<instituição>.com.br` → para endpoints HTTPS e HTTPS EV
- `mtls-openbanking.<instituição>.com.br` → para endpoints HTTPS mTLS ICP-Brasil

Um proxy reverso (WAF ou Kong) roteia as requisições para o serviço correto com base no path:

| Path | Destino |
|---|---|
| `/auth`, `/.well-known`, `/apple-app-site-association` | Authorization Server |
| `/open-banking`, demais rotas | Kong (Resource Server) |

> ⚠️ Jamais disponibilize suas chaves privadas em serviços da internet. A geração e conversão de certificados deve ser feita exclusivamente em ambiente local controlado.

---

## Como obter os certificados

Os certificados BRCAC e BRSEAL são gerados diretamente no **Diretório de Participantes** do Open Finance Brasil. O certificado EV e o certificado de servidor mTLS são adquiridos junto a uma **autoridade certificadora ICP-Brasil** homologada.

Para ITP e Receptor de Dados, os certificados BRCAC e BRSEAL são gerados no Diretório de Participantes do sandbox durante a fase de homologação — veja [Diretório de Participantes — Homologação](../diretorio-hml/diretorio-hml.html).

---

## Conversão para JWK (quando necessário)

Alguns processos, como a certificação de segurança OpenID, exigem os certificados no formato JWK. A conversão é feita localmente:

**Pré-requisito:** Node.js e o pacote `pem-jwk` instalados (`npm install -g pem-jwk`).

```shell
# 1. Converter a chave para o formato RSA
openssl rsa -in certificado.key -out certificado-rsa.key

# 2. Gerar o JWK
pem-jwk certificado-rsa.key > certificado-jwk.json
```

Após a conversão, adicione manualmente os campos obrigatórios ao JSON:
- `"use"`: `"enc"` para BRCAC; `"sig"` para BRSEAL
- `"alg"`: `"PS256"`
- `"kid"`: o `kid` do certificado emitido pelo Diretório

Para encapsular em um JWKS:
```json
{
  "jwks": [
    { /* JWK do BRCAC */ },
    { /* JWK do BRSEAL */ }
  ]
}
```

---

## Referências

- [Especificação de Certificados — Open Finance Brasil](https://openbanking-brasil.github.io/specs-seguranca/open-banking-brasil-certificate-standards-1_ID1.html)
- [Certificações e Certificados — Open Finance Brasil](https://opusopenfinance.github.io/Realize/pt-br/Open-Finance/Open-Finance-Brasil/OFB-Certifica%C3%A7%C3%B5es.html)
- [Diretório de Participantes — Homologação](../diretorio-hml/diretorio-hml.html)
