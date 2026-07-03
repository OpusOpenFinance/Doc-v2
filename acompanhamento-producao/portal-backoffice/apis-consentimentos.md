---
layout: default
title: APIs de Gestão de Consentimentos
parent: Portal Backoffice
grand_parent: Acompanhamento em Produção
nav_order: 2
lang: "pt-br"
---

# APIs de Gestão de Consentimentos

A Plataforma Opus Open Finance expõe um conjunto de APIs de backoffice que permitem à instituição consultar, revogar e gerenciar consentimentos e pagamentos diretamente — sem passar pelo fluxo regulatório externo. São usadas por sistemas internos, portais de atendimento ao cliente e ferramentas de operações.

A especificação completa está disponível no OAS fornecido junto ao produto (`oas-oob-consents.yaml`).

---

## Autenticação

Todos os endpoints exigem um token gerado pelo fluxo **Client Credentials** no caminho base não-regulatório do Authorization Server. Os escopos necessários por endpoint estão definidos na seção de segurança da configuração da plataforma.

---

## Endpoints disponíveis

### Listagem de consentimentos

```
GET /open-banking/oob-consents/v1/consents
```

Lista os consentimentos de um titular. O dono pode ser identificado por:

- `cpf` — CPF do titular (apenas dígitos, ex.: `99999999999`)
- `consent-owner` — conjunto de informações customizadas pela instituição (ex.: agência + conta), em formato JSON URL Encoded

```
# Exemplo de consent-owner (antes do encoding):
[{"key": "conta", "value": "12345"}, {"key": "agencia", "value": "12345"}]
```

Filtros adicionais disponíveis:

| Filtro | Tipo | Descrição |
|---|---|---|
| `createdOnBegin` | datetime RFC-3339 | Data de criação mínima |
| `createdOnEnd` | datetime RFC-3339 | Data de criação máxima |
| `type` | string | `PAYMENT` ou `DATA_SHARING` |
| `status` | string | Status do consentimento (varia por tipo) |
| `modalityType`* | string | `IMMEDIATE` ou `SCHEDULED` (apenas pagamento) |
| `paymentType`* | string | `PIX`, `TED` ou `TEF` (apenas pagamento) |

*Filtros marcados com \* são exclusivos para consentimentos de pagamento.

---

### Detalhamento do consentimento

```
GET /open-banking/oob-consents/v1/consents/{consentId}
```

Retorna todas as informações de um consentimento, incluindo os recursos vinculados e o histórico completo de mudanças de status. O `consentId` aqui é o identificador interno UUID (não o URN regulatório).

---

### Listagem de consentimentos ativos de compartilhamento de dados

```
GET /open-banking/oob-consents/consents/v2/active
```

Lista consentimentos de compartilhamento de dados no status `AUTHORISED`. Filtros opcionais:
- `startDate` — seleciona consentimentos criados após esta data
- `endDate` — seleciona consentimentos cuja expiração seja anterior a esta data (consentimentos indeterminados não são retornados quando este filtro é informado)
- `page` / `page-size` — paginação

---

### Listagem de pagamentos por consentimento

```
GET /open-banking/oob-consents/consents/v1/consents/{consentId}/payments
```

Retorna todos os pagamentos relacionados a um consentimento.

---

### Revogação de consentimento de compartilhamento de dados

```
PATCH /open-banking/oob-consents/consents/v1/consents/{consentId}
```

Revoga o consentimento de compartilhamento de dados identificado.

---

### Revogação de consentimento de pagamento automático

```
PATCH /open-banking/oob-consents/payments/v1/consents/{consentId}
```

Revoga um consentimento de pagamento automático (Pix Automático).

---

### Revogação de pagamento individual

```
PATCH /open-banking/oob-payments/v2/pix/payments/{paymentId}
```

Revoga um pagamento específico, identificado pelo `paymentId` do Open Finance.

---

### Revogação de vínculo de dispositivo

```
PATCH /open-banking/oob-consents/enrollments/v1/enrollments/{enrollmentId}
```

Revoga um vínculo de dispositivo (enrollment), retornando os detalhes e o histórico de mudanças de status.

---

### Notificação de mudança de status de pagamento

```
POST /open-banking/oob-consents/v1/payment-status-notification
```

Permite que a retaguarda da instituição notifique a plataforma sobre uma mudança de status em um pagamento — útil para integrações onde o sistema de Pix da instituição precisa comunicar resultados de forma assíncrona.

---

### Notificação de alteração de recursos

```
POST /open-banking/oob-consents/v1/resources-notification
```

Notifica a plataforma sobre alterações em recursos não-selecionáveis por categoria (ex.: novo contrato de empréstimo, financiamento). Permite que a plataforma atualize os recursos vinculados a consentimentos ativos sem aguardar a próxima consulta do TPP.

---

### Listagem de Payment IDs gerados por ITP

```
GET /open-banking/oob-consents/v1/tpps/payment-legacy-ids
```

Lista os payment IDs gerados por ITPs em um intervalo de datas. Parâmetros:
- `startDate` — data mínima (formato `yyyy-MM-dd`)
- `endDate` — data máxima (formato `yyyy-MM-dd`)

---

### Detalhamento de prorrogações de consentimento

```
GET /open-banking/oob-consents/v1/consents/{consentId}/extends
```

Lista todas as prorrogações realizadas em um consentimento.

---

### Autorização de consentimento de múltipla alçada

```
POST /open-banking/oob-consents/v1/payments/consents/{consentId}/authorisation
```

Autoriza completamente um consentimento de pagamento de múltipla alçada, sinalizando a aprovação de todos os autorizadores.

---

### Gerenciamento de search-keys

```
POST   /open-banking/oob-consents/consents/v1/consents/{consentId}/search-key/{searchKey}
DELETE /open-banking/oob-consents/consents/v1/consents/{consentId}/search-key/{searchKey}
```

Permite associar e remover chaves de busca customizadas a consentimentos, para facilitar consultas posteriores por identificadores internos da instituição.

---

### Gerenciamento de metadata

```
PUT    /open-banking/oob-consents/consents/v1/consents/{consentId}/meta-data
GET    /open-banking/oob-consents/consents/v1/consents/{consentId}/meta-data
PATCH  /open-banking/oob-consents/consents/v1/consents/{consentId}/meta-data
DELETE /open-banking/oob-consents/consents/v1/consents/{consentId}/meta-data
```

Permite associar um JSON livre de informações extras a um consentimento — por exemplo, dados de contexto úteis para as telas da aplicação. `PUT` substitui o metadata existente; `PATCH` adiciona ao metadata existente.

---

### Controle de webhook por consentimento

```
PATCH /open-banking/oob-consents/v1/webhook/toggle/{consentId}
GET   /open-banking/oob-consents/v1/webhook/status/{consentId}
```

Ativa ou desativa o envio de webhooks opcionais para a retaguarda atrelados a um consentimento específico, e consulta o status atual desse envio.
