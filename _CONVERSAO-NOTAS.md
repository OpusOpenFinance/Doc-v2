# Conversão-piloto para o formato ReadMe

Esta pasta (`conversao-readme/`) é o **piloto** de conversão da `estrutura-montada/` para o formato do ReadMe. Nada foi convertido "por cima" — é uma cópia paralela, para você comparar e validar o padrão antes de aplicarmos no resto.

## Padrão adotado

**1. Frontmatter** — trocado do Jekyll para o do ReadMe (Bi-Directional Sync):
```
---
title: "..."
summary: "..."
---
```
(sem `layout`, `parent`, `nav_order`, `has_children`, `lang` — nada disso existe no ReadMe.)

**2. Navegação** — cada pasta tem um `_order.yaml` com a ordem das páginas (é assim que o ReadMe monta o menu no sync com Git, no lugar do `nav_order`).

**3. MDX** — removidos os comentários HTML (`<!-- -->`), que quebram no MDX do ReadMe.

**4. Links internos** — removido o `.html` (ex.: `conceitos.html` → `conceitos`).

## O ponto central: referência aos ymls (swagger-ui → API Reference)

No formato antigo, cada API era aberta por um link para o swagger-ui, que carregava um yml:
```
[API-Pagamentos]: /reference/otpp-iniciacao_pagamentos
```

No ReadMe **não existe swagger-ui**: cada yml é enviado como uma **API Reference nativa** e passa a ter uma URL própria em `/reference/<slug>`. Então a convenção da conversão é:

- todo link de swagger-ui vira `/reference/<slug>`;
- todo link direto para o `.yml` também vira `/reference/<slug>` (a spec passa a viver na API Reference, não como download).

### Mapa yml → API Reference (slugs PROPOSTOS)

| yml (origem) | swagger `api=` | slug no ReadMe (`/reference/…`) |
| --- | --- | --- |
| opusTPP-iniciacaoPagamentos.yml | otpp-iniciacao_pagamentos | `iniciacao-de-pagamentos` |
| opusTPP-pagamentosAutomaticos.yml | otpp-pagamentos_automaticos | `pagamentos-automaticos` |
| opusTPP-pagamentosSR.yml | otpp-pagamentos_sem_redirecionamento | `pagamentos-sem-redirecionamento` |
| opusTPP-webhooks.yml | otpp-webhooks | `webhooks` |
| opusTPP-backoffice.yml | otpp-backoffice | `backoffice` |
| opusTPP-apisInternas.yml | — | `apis-internas` |
| opusTPP-recepcaoDadosOf.yml | otpp-recepcao_dados_of | `recepcao-de-dados` |
| opusTPP-recepcaoDadosOi.yml | — | `recepcao-de-dados-open-insurance` |
| (perfis) oas-receptor | oas-receptor | `receptor-de-dados` |

> Os slugs acima são **propostos**. O slug real é definido quando o yml é enviado ao ReadMe (via upload no painel ou `rdme openapi upload`). Depois de subir as APIs, é um find-replace simples para casar os slugs finais. Recomendo **fixar esses nomes** e usá-los em toda a documentação — assim os links já nascem certos.

### Recomendação para o resto da documentação
1. Enviar cada yml como uma API Reference no ReadMe, usando os slugs da tabela.
2. Em todas as páginas, referenciar as APIs por `/reference/<slug>` (nunca mais por caminho de arquivo).
3. Os ymls ficam versionados no Git (aqui em `anexos/yml/`) como fonte para o upload; a renderização é a API Reference do ReadMe.

## Separação dos produtos (Iniciação de Pagamentos × Recepção de Dados)

O conteúdo vinha combinado na sua pasta `iniciacaoDePagamentosERecepcaoDeDados` (que **não foi alterada**). Aqui foi separado em dois produtos, lendo daquela pasta como origem:

- **produtos/iniciacaoDePagamentos/** — conceitos, funcionamento (iniciação, automáticos, vínculo, redirecionamento, webhooks, backoffice), configuração e os ymls de pagamento.
- **produtos/recepcaoDeDados/** — o fluxo de recepção + os ymls de recepção.

### ⚠️ O que ficou avisado (não soube separar sozinho)
- **Conteúdo compartilhado:** consentimento, redirecionamento, vínculo de dispositivo e configuração/certificados valem para os dois produtos. Ficaram descritos em *Iniciação de Pagamentos* e a página de *Recepção de Dados* aponta para lá, para não duplicar. Se preferir duplicar ou criar uma seção "Comum aos dois", me avise.
- **Recepção de Dados está fina:** hoje só há o fluxo em `recepcaoDeDados`. Tópicos próprios (paginação, tipos de recurso por API, erros específicos de recepção) ainda não existem como páginas — precisam ser escritos ou extraídos das APIs.

## Ainda pendente nesta fase
- **Imagens:** ✅ todas as imagens referenciadas foram colocadas em `anexos/imagens/` dentro de cada seção, e todas as referências relativas resolvem (0 quebradas). Elas viajam com o repositório no sync. **Único ponto que depende da conexão:** confirmar no hub publicado se o ReadMe renderiza a imagem pelo caminho relativo do repo ou se re-hospeda no CDN dele — isso só dá para verificar com o projeto já conectado.
- **Links entre páginas:** apontam para os slugs novos; conferir todos após subir ao ReadMe.
- **Demais seções** (o resto da estrutura) seguem exatamente este mesmo padrão quando você aprovar o piloto.


---

## Para Desenvolvedores — APIs referenciadas

Slugs `/reference/<slug>` usados nesta seção (a confirmar no upload dos ymls):

- `adiantamentos`
- `cambio`
- `cartao-de-credito`
- `contas`
- `dados-cadastrais`
- `data-variable-incomes`
- `direitos-creditorios`
- `emprestimos`
- `financiamentos`
- `fundos-investimento`
- `oas-receptor`
- `open-data-accounts`
- `open-data-acquiring`
- `open-data-capitalization`
- `open-data-channels`
- `open-data-credit-cards`
- `open-data-exchange`
- `open-data-financings`
- `open-data-insurance`
- `open-data-investments`
- `open-data-invoice-financings`
- `open-data-loans`
- `open-data-pension`
- `open-data-unarranged`
- `opus-commons`
- `payment-integration-v5`
- `portability`
- `renda-fixa-bancaria`
- `renda-fixa-credito`
- `tesouro-direto`

Links diretos a .yml convertidos (yml → slug):

- `accounts-2-4-1.yml` → `/reference/accounts`
- `bankFixedIncomes.yml` → `/reference/bank-fixed-incomes`
- `creditCards-2-3-1.yml` → `/reference/credit-cards`
- `creditFixedIncomes.yml` → `/reference/credit-fixed-incomes`
- `customers-2-2-0.yml` → `/reference/customers`
- `exchange-1-0-0.yml` → `/reference/exchange`
- `financings-2-3-0.yml` → `/reference/financings`
- `funds.yml` → `/reference/funds`
- `invoiceFinancings-2-3-0.yml` → `/reference/invoice-financings`
- `loans-2-4-0.yml` → `/reference/loans`
- `opusCommons-1-0-0.yml` → `/reference/opus-commons`
- `overdraft-2-4-0.yml` → `/reference/overdraft`
- `paymentIntegration-0.1.0.yml` → `/reference/payment-integration`
- `paymentIntegration-v5.0.0-rc.1-2.2.0.yaml` → `/reference/payment-integration-v5.0.0-rc`
- `portability.yml` → `/reference/portability`
- `treasuryBonds.yml` → `/reference/treasury-bonds`
- `variableIncomes.yml` → `/reference/variable-incomes`


---

## Implantação — APIs referenciadas

- `/reference/mobile`


---

## Preparativos para Produção — APIs referenciadas

_(nenhuma API referenciada nesta seção)_


---

## Acompanhamento em Produção — APIs referenciadas

- `/reference/oas-back-dados`
- `/reference/otpp-backoffice`

Links diretos a .yml (yml → slug):

- `opusTPP-backoffice.yml` → `/reference/backoffice`


---

## Introdução — APIs referenciadas

- `/reference/oas-receptor`


---

## ✅ Conversão completa (todas as seções)

Toda a documentação foi convertida para o formato ReadMe em `conversao-readme/`:

| Seção | Páginas |
| --- | --- |
| Introdução | 13 |
| Produtos | 17 |
| Para Desenvolvedores | 46 |
| Implantação | 12 |
| Preparativos para Produção | 4 |
| Acompanhamento em Produção | 14 |
| **Total** | **107** |

Verificações finais (páginas de conteúdo): **0** swagger-ui, **0** atributos kramdown `{:}`, **0** links `.html`, **0** imagens quebradas.

### Pendências conhecidas (decisão sua)
- **Slug único por API:** a mesma API às vezes aparece com nomes diferentes no conteúdo antigo (ex.: `contas`/`accounts`; `backoffice`/`otpp-backoffice`/`oas-back-dados`). Ao subir os ymls, escolher **um slug canônico** e alinhar os links `/reference/<slug>`.
- **`detentorTransmissor/index.md`** segue concatenado (item adiado).
- **Páginas "Em construção"** convertidas como placeholder — a preencher.
- **A pasta protegida** `iniciacaoDePagamentosERecepcaoDeDados` não foi reconvertida (virou os dois produtos separados).
- **Imagens:** resolvidas por caminho relativo; validar renderização no hub após conectar o ReadMe.
