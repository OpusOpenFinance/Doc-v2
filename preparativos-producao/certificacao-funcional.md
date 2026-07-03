---
layout: default
title: Aprovação dos Testes de Certificação Funcional
parent: Preparativos para Produção
nav_order: 1
lang: "pt-br"
---

# Aprovação dos Testes de Certificação Funcional

A certificação funcional valida que as APIs regulatórias da instituição estão respondendo de acordo com as especificações do Open Finance Brasil. É conduzida pelo certificador da governança e precisa estar aprovada antes do go-live.

Os testes aprovados ficam públicos e podem ser acompanhados em:
[https://web.conformance.directory.openbankingbrasil.org.br/plans.html?public=true](https://web.conformance.directory.openbankingbrasil.org.br/plans.html?public=true)

---

## Pré-requisito: DCR para o certificador funcional

O certificador funcional de pagamento exige um client registrado no Authorization Server gerado especificamente a partir de um Software Statement Assertion (SSA) do Diretório de sandbox. Mesmo que o certificador de segurança já tenha feito um DCR, ele usa redirect URIs diferentes — por isso é necessário fazer um DCR adicional via cURL.

### O que você vai precisar

- Certificado e chave privada BRCAC do Software Statement (sandbox)
- Endereço mTLS do Authorization Server da instalação
- Alias definido para a execução dos testes funcionais
- Acesso ao Diretório de sandbox com permissão para editar Software Statements
- Software Statement com os papéis **PAGTO** e **DADOS** ativos
- URL `software_jwks_uri` do Software Statement

> O SSA tem validade de **5 minutos**. Prepare tudo antes de gerá-lo.

### Passo 1 — Preparar o ambiente local

Crie um diretório de trabalho e copie os arquivos do certificado BRCAC para ele. Renomeie-os para facilitar o uso:

```sh
brcac.cer   # certificado de transporte
brcac.key   # chave privada do certificado
```

### Passo 2 — Obter a URL de DCR

Abra a URL de configuração do Authorization Server no browser:

```
https://<fqdn-da-instalacao>/.well-known/openid-configuration
```

No JSON retornado, localize a propriedade `registration_endpoint`. Esse é o endpoint de DCR que será usado no cURL.

Exemplo: `https://mtls-obb.qa.oob.opus-software.com.br/auth/reg`

### Passo 3 — Criar o arquivo dcr.json

```json
{
    "grant_types": [
        "authorization_code",
        "implicit",
        "refresh_token",
        "client_credentials"
    ],
    "jwks_uri": "<software_jwks_uri>",
    "token_endpoint_auth_method": "private_key_jwt",
    "response_types": ["code id_token"],
    "redirect_uris": [
        "https://web.conformance.directory.openbankingbrasil.org.br/test/a/<alias>/callback",
        "https://web.conformance.directory.openbankingbrasil.org.br/test/a/<alias>/callback?dummy1=lorem&dummy2=ipsum"
    ],
    "software_statement": "<ssa-jwt>"
}
```

Substitua `<alias>` pelo alias definido para os testes funcionais.

### Passo 4 — Configurar o Software Statement no Diretório sandbox

Acesse o [Diretório de sandbox](https://web.sandbox.directory.openbankingbrasil.org.br/) e verifique:

1. O Software Statement tem os papéis **PAGTO** e **DADOS** em *Authority Claims*. Se algum papel estiver faltando, adicione-o via *Authority Domain Role Claims* da organização.

2. As redirect URIs do `dcr.json` estão presentes no campo REDIRECT URI do Software Statement:
   ```
   https://web.conformance.directory.openbankingbrasil.org.br/test/a/<alias>/callback
   https://web.conformance.directory.openbankingbrasil.org.br/test/a/<alias>/callback?dummy1=lorem&dummy2=ipsum
   ```

3. Abra a seção *Software Statement Assertion*, clique em **Copy to clipboard** e cole o JWT no campo `software_statement` do `dcr.json`.

4. Copie o valor de `software_jwks_uri` e cole no campo `jwks_uri` do `dcr.json`.

Salve o arquivo `dcr.json`.

### Passo 5 — Executar o DCR

```bash
curl -k --cipher 'DEFAULT:!DH' \
  --cert brcac.cer --key brcac.key \
  -d @dcr.json \
  -H "content-type: application/json" \
  -H "accept: application/json" \
  -o dcr-result.json \
  <url-de-dcr-do-as>
```

Abra o arquivo `dcr-result.json`. A presença do atributo `client_id` no JSON confirma que o DCR foi bem-sucedido.

---

## Certificação de segurança OpenID (conduzida pela Opus)

A certificação de segurança valida o Authorization Server contra o perfil FAPI-BR. **A Opus conduz todo este processo.** Os detalhes abaixo descrevem o que acontece para que a instituição compreenda o processo e assine os documentos necessários.

### Composição da certificação

A certificação é composta por dois testes:

1. **DCR** — `Brazil Dynamic Client Registration Authorization server test`
2. **FAPI** — um dos perfis abaixo (pelo menos um é obrigatório):

| Perfil |
|---|
| `BR-OB Adv. OP w/ MTLS` |
| `BR-OB Adv. OP w/ Private Key` |
| `BR-OB Adv. OP w/ MTLS, PAR` |
| `BR-OB Adv. OP w/ Private Key, PAR` |
| `BR-OB Adv. OP w/ MTLS, JARM` |
| `BR-OB Adv. OP w/ Private Key, JARM` |
| `BR-OB Adv. OP w/ MTLS, PAR, JARM` |
| `BR-OB Adv. OP w/ Private Key, PAR, JARM` |

**Pré-requisito:** o ambiente precisa passar nos testes sem nenhum erro. Warnings são permitidos.

### Documento OpenID-Certification-of-Conformance

Para cada teste (DCR e FAPI), é necessário preencher e assinar o formulário `OpenID-Certification-of-Conformance`. Regras:

- Deve ser assinado por um **funcionário da organização** (não pode ser terceiro)
- A assinatura pode ser tradicional ou eletrônica (ex.: DocuSign)
- As pessoas de contato podem ser funcionários ou terceiros
- **Não** é necessário preencher o apêndice
- O arquivo final deve estar no formato **PDF** com o nome exato `OpenID-Certification-of-Conformance.pdf`

O template Word está disponível no [site da OpenID Foundation](https://openid.net/wordpress-content/uploads/2021/07/OpenID-Certification-of-Conformance.docx).

**Valores de referência para preenchimento:**

| Campo | DCR | FAPI |
|---|---|---|
| Name of Entity ("Implementer") | \<Nome da organização\> | \<Nome da organização\> |
| Software or Service ("Deployment") | Opus Open Banking v1 | Opus Open Banking v1 |
| OpenID Conformance Profile | BR-OB Adv. OP DCR | BR-OB Adv. OP w/ Private Key, PAR |
| Conformance Test Suite Software | www.certification.openid.net \<versão\> | www.certification.openid.net \<versão\> |
| Test Date | \<data em inglês\> | \<data em inglês\> |

### Geração e envio do pacote de certificação

Para cada teste (DCR e FAPI):

1. Acesse [https://www.certification.openid.net](https://www.certification.openid.net) com o usuário da Opus
2. Clique em "View all available test plans" e localize a execução correspondente
3. Clique em "View plan" → "Certification Package"
4. Faça upload do arquivo `OpenID-Certification-Terms-and-Conditions.pdf` (disponível no [site da OpenID](https://openid.net/wordpress-content/uploads/2019/03/OpenID-Certification-Terms-and-Conditions.pdf) — não requer alterações)
5. Faça upload do `OpenID-Certification-of-Conformance.pdf` correspondente ao teste
6. Clique em "Prepare Certification Package" e faça download do ZIP
7. Renomeie o ZIP conforme o padrão:

| Teste | Padrão de nomenclatura |
|---|---|
| DCR | `<Nome-Org>-Opus_Open_Banking_v1-BR-OB-Adv-OP-DCR-<Data-inglês>.zip` |
| FAPI | `<Nome-Org>-Opus_Open_Banking_v1-BR_OB_Adv_OP_w_Private-Key_PAR-<Data-inglês>.zip` |

Exemplo DCR: `Opus_Software-Opus_Open_Banking_v1-BR_OB_Adv_OP_DCR-14-Aug-2021.zip`

Envie os dois ZIPs pelo formulário da OpenID Foundation:
[https://openid.atlassian.net/servicedesk/customer/portal/3/group/3/create/10016](https://openid.atlassian.net/servicedesk/customer/portal/3/group/3/create/10016)

**Valores do formulário de envio:**

| Campo | Valor |
|---|---|
| Summary | \<Nome da Organização\> - Opus Open Banking v1 |
| Test Results | My tests have all passed (or have only warnings) |
| Certification Payment Status | \<modelo de pagamento utilizado\> |
| Certification Zip File | Anexar os dois ZIPs gerados |
| Email confirmation to | \<e-mail do responsável na organização\> |

Um e-mail de confirmação chegará após o envio. A OpenID Foundation processa em até **3 dias úteis**. A certificação aprovada fica publicada no [site oficial da OpenID](https://openid.net/certification/#FAPI_OPs).
