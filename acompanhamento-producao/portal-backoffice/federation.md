---
layout: default
title: Autenticação via Federation
parent: Portal Backoffice
grand_parent: Acompanhamento em Produção
nav_order: 4
lang: "pt-br"
---

# Autenticação via Federation

O Portal Backoffice suporta autenticação via **Federation**, permitindo que a instituição integre seu próprio **Identity Provider (IDP)** ao Authorization Server da plataforma. Com isso, os usuários acessam o portal com o mesmo login institucional que já utilizam em outros sistemas internos — sem precisar de credenciais separadas.

---

## Como funciona

O fluxo de autenticação envolve três componentes:

1. **Portal Backoffice** inicia o processo de autenticação junto ao Authorization Server (AS) da plataforma
2. **Authorization Server** se autentica junto ao IDP externo da instituição
3. O IDP retorna a identidade do usuário; o AS gera e retorna ao Portal um token de acesso válido

---

## O que precisa ser configurado

A configuração envolve três partes:

### 1. Portal Backoffice

Configurar as seguintes variáveis de ambiente para que o Portal saiba onde está o AS e como se comunicar com ele:

| Variável | Descrição |
|---|---|
| `authDiscoveryDocumentUrl` | URL do discovery document do AS |
| `authIssuer` | Issuer do AS |
| `authClientId` | Client ID do Portal no AS |
| `authClientSecretName` | Nome do Kubernetes Secret com o client secret |
| `authClientSecretKey` | Chave dentro do Secret com o client secret |

Detalhes e exemplos estão na documentação de deploy do Portal Backoffice.

### 2. Authorization Server

Dois conjuntos de configurações são necessários:

**Client estático do Portal Backoffice** — registra o Portal como cliente do AS. A documentação detalhada está na seção de deploy do Authorization Server.

**Client para comunicação com o IDP externo** — configura como o AS se autentica junto ao IDP da instituição. Os parâmetros variam conforme o protocolo do IDP (OIDC, SAML, LDAP, etc.).

### 3. IDP externo da instituição

O IDP precisa ser configurado para gerar tokens no formato esperado pelo AS. Os requisitos específicos dependem do IDP utilizado pela instituição e são detalhados na documentação de configuração do Authorization Server.

---

## Referências

- Documentação de deploy do Portal Backoffice — para detalhes das variáveis de ambiente
- Documentação de deploy do Authorization Server — para configuração de clients estáticos e federation
