---
layout: default
title: Customização Visual
parent: Portal Backoffice
grand_parent: Acompanhamento em Produção
nav_order: 3
lang: "pt-br"
---

# Customização Visual do Portal Backoffice

O Portal Backoffice pode ser customizado com a identidade visual da instituição — logo, favicon, título da página e paleta de cores.

---

## Propriedades configuráveis

| Propriedade | Descrição |
|---|---|
| `app.title` | Título da página no browser |
| `app.faviconPath` | Caminho do ícone da aba do browser |
| `app.copyright` | Texto de copyright no rodapé |
| `brand.name` | Nome da marca exibido no portal |
| `brand.path` | Caminho do arquivo de logotipo |

---

## Customização de cores (temas)

É possível criar múltiplos temas e definir qual está ativo via a propriedade `selectedTheme`. A estrutura de configuração de tema é:

```json
{
  "selectedTheme": "minha-marca",
  "themes": [
    {
      "name": "minha-marca",
      "variables": {
        "primary-color": "#003B8E",
        "primary-color-light": "#0052C4",
        "secondary-color": "#E8F0FE",
        "tertiary-color": "#F5F5F5",
        "bg-color": "#FFFFFF",
        "alert-color": "#D93025",
        "attention-color": "#F9AB00",
        "success-color": "#1E8E3E",
        "link-color": "#1967D2"
      }
    }
  ]
}
```

> É obrigatório informar o `selectedTheme`. Sem ele, a aplicação do tema não tem efeito.

### Variáveis de tema disponíveis

| Variável | Aplicação |
|---|---|
| `primary-color` | Cor principal — aplicada na maioria dos elementos |
| `primary-color-light` | Variação mais clara da cor principal |
| `secondary-color` | Cor secundária |
| `tertiary-color` | Cor terciária |
| `bg-color` | Cor de fundo da página |
| `alert-color` | Cor de alerta, usada principalmente no ícone de exclusão |
| `attention-color` | Cor de aviso |
| `success-color` | Cor de sucesso |
| `link-color` | Cor dos links |
