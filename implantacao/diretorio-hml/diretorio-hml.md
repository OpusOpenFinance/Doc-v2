---
layout: default
title: Diretório de Participantes — Homologação
parent: Implantação
nav_order: 2
has_children: false
lang: "pt-br"
---

# Diretório de Participantes — Homologação (Sandbox)

O **Diretório de Participantes** é o repositório oficial mantido pelo Banco Central que registra todas as instituições autorizadas a operar no Open Finance Brasil. Ele tem dois ambientes: **sandbox** (homologação) e **produção**.

Durante a implantação, a instituição trabalha primeiro no sandbox para configurar certificados, realizar testes e obter as certificações necessárias. Só após a aprovação de todas as etapas de homologação o cadastro é replicado no ambiente de produção.

---

## Conceito

### O que é o Diretório

O Diretório centraliza três tipos de informação:

- **Organizações**: cada instituição participante cadastra sua organização identificada pelo CNPJ.
- **Software Statements**: cada aplicação cliente (TPP) que a organização opera é registrada como um Software Statement, gerando um `softwareStatementId` e um `client_id` únicos.
- **Certificados**: os certificados BRCAC e BRSEAL da organização ficam publicados no Diretório, permitindo que outras instituições os consultem para validar assinaturas e conexões mTLS.

### Por que ele importa

Nenhuma instituição consegue participar do ecossistema sem estar registrada no Diretório. É dele que saem:
- Os **certificados regulatórios** (BRCAC e BRSEAL)
- O **Software Statement Assertion (SSA)** — documento JWS que descreve a aplicação e é usado no processo de DCR (Dynamic Client Registration) junto às outras instituições
- A lista de **redirect URIs** autorizadas para o fluxo de consentimento

### Open Finance e Open Insurance são Diretórios separados

Instituições que atuam nos dois ecossistemas precisam de cadastros independentes — um no Diretório do Open Finance Brasil e outro no Diretório do Open Insurance Brasil.

---

## Cadastro no Sandbox

### Passo 1 — Criar conta no sandbox

Acesse o [sandbox do Diretório de Participantes](https://web.sandbox.directory.openbankingbrasil.org.br/organisations) e crie uma conta para sua organização.

> Você precisará de um usuário com privilégio de criação e alteração de Software Statements para as etapas seguintes.

### Passo 2 — Cadastrar a organização

Registre a organização informando os dados básicos da instituição (CNPJ, razão social, etc.).

### Passo 3 — Criar o Software Statement

Dentro da organização, crie um **Software Statement** para cada aplicação que sua instituição irá operar. O Software Statement representa uma marca ou aplicativo específico.

> ⚠️ Não é possível alterar as informações do Software Statement após visualizar o Software Statement Assertion (SSA). Verifique todos os campos múltiplas vezes antes de concluir.

Campos de atenção especial:

**Redirect URIs**: são as URLs para as quais o fluxo de autorização de consentimento pode redirecionar o usuário. Toda URL que sua aplicação usa no fluxo de consentimento precisa estar cadastrada aqui.

Para testes com as ferramentas da Opus, inclua:

```
https://tpp-client1.127.0.0.1.nip.io/cb
https://tpp-client1.127.0.0.1.nip.io:3100/auth
https://tpp-client1.127.0.0.1.nip.io:3100/cb
https://tpp-client2.127.0.0.1.nip.io:3100/auth
https://tpp-client2.127.0.0.1.nip.io:3100/cb
```

Para o certificador de segurança OpenID (em execução na nuvem):

```
https://www.certification.openid.net/test/a/<alias>/callback
https://www.certification.openid.net/test/a/<alias>/callback?dummy1=lorem&dummy2=ipsum
```

Para o certificador funcional:

```
https://web.conformance.directory.openbankingbrasil.org.br/test/a/<alias>/callback
```

> Substitua `<alias>` por uma string única que identifique sua instalação. Isso evita que execuções de diferentes instituições interfiram umas com as outras.

**Papel regulatório (role):** defina o papel da aplicação:
- `DADOS` — para Transmissor de Dados
- `PAGTO` — para Detentor de Conta e ITP
- `CONTA` — para operações em conta corrente
- `CCORR` — para câmbio

Para o certificador funcional, o Software Statement precisa ter os papéis `PAGTO` e `DADOS` simultaneamente.

### Passo 4 — Gerar os certificados

No Diretório, gere os certificados **BRCAC** e **BRSEAL** para o Software Statement criado. Eles ficam associados à sua organização e são consultados pelas outras instituições para validar suas chamadas.

Renomeie os arquivos para facilitar o uso nos exemplos e na configuração da plataforma:
- `brcac.cer` e `brcac.key` para o certificado de transporte
- `brseal.key` para o certificado de assinatura

> Guia de referência: [Guia de Operação do Diretório Central](https://openbanking-brasil.github.io/areadesenvolvedor/documents/OpenBanking-Guia_Operacao_Diretorio_Central.pdf)

### Passo 5 — Obter o Software Statement Assertion (SSA)

O SSA é o documento JWS gerado pelo Diretório que descreve sua aplicação. Ele é necessário para o processo de DCR junto às outras instituições. Tem validade de **5 minutos**, então prepare o processo de DCR antes de gerá-lo.

---

## DCR — Dynamic Client Registration no sandbox

O DCR é o processo pelo qual a sua aplicação se registra dinamicamente como cliente nas outras instituições. No sandbox, ele é necessário para executar os testes de certificação funcional.

O certificador de segurança realiza DCR automaticamente, mas usa redirect URIs que não servem para o certificador funcional — por isso é necessário fazer um DCR adicional via cURL.

**O que você vai precisar:**
- Certificado e chave privada BRCAC do Software Statement
- Endereço mTLS do Authorization Server da instalação
- Alias utilizado na configuração dos testes funcionais
- SSA válido (gerado agora no Diretório)
- URL do endpoint de DCR da instalação

**Como descobrir a URL de DCR:**
Abra a URL de configuração do Authorization Server (`.well-known/openid-configuration`) no browser e localize o campo `registration_endpoint`.

Exemplo: `https://mtls-obb.qa.oob.opus-software.com.br/auth/reg`

O arquivo `dcr.json` para o registro:

```json
{
    "grant_types": [
        "authorization_code",
        "implicit",
        "refresh_token",
        "client_credentials"
    ],
    "jwks_uri": "<url-jwks-do-software-statement>",
    "token_endpoint_auth_method": "private_key_jwt",
    "response_types": ["code id_token"],
    "redirect_uris": [
        "https://web.conformance.directory.openbankingbrasil.org.br/test/a/<alias>/callback"
    ],
    "software_statement": "<ssa-jwt>"
}
```

---

## Próximos passos

Com o sandbox configurado, você está pronto para:

- [Executar os testes de certificação de segurança OpenID](../../certificacoes/certificacao-seguranca.html) *(ver checklist do seu perfil)*
- [Executar os testes de certificação funcional](../../certificacoes/certificacao-funcional.html) *(ver checklist do seu perfil)*
- Configurar o diretório de **produção** — etapa realizada após a aprovação de todas as certificações, seguindo o mesmo processo deste guia no ambiente de produção.

---

## Referências

- [Sandbox do Diretório de Participantes](https://web.sandbox.directory.openbankingbrasil.org.br/organisations)
- [Guia de Operação do Diretório Central](https://openbanking-brasil.github.io/areadesenvolvedor/documents/OpenBanking-Guia_Operacao_Diretorio_Central.pdf)
- [Guia de Certificação de Conformidade — Open Finance Brasil](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/155910145)
- [Certificações e Certificados](../../certificados/certificados.html)
