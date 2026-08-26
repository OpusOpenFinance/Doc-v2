# Páginas pausadas (Em construção)

_Última atualização: 2026-07-28_

Estas páginas foram **removidas do hub ReadMe** (Doc-Readme) por estarem em construção, mas continuam **guardadas aqui no Doc-v2**. Quando o conteúdo estiver pronto, peça a republicação da seção para trazê-las de volta ao hub.

**Total pausado: 25 páginas.**

---

## Como republicar uma página

Quando o conteúdo de uma página não estiver mais "Em construção", basta:

1. No **Doc-v2**, edite o arquivo (caminho listado abaixo) e tire o aviso de "Em construção" / 🚧.
2. Me avise qual página/seção ficou pronta. Eu então:
   - copio a página do Doc-v2 para o hub (`Doc-Readme/docs/<Seção>/…`) no formato ReadMe (frontmatter `title`, sem `hidden`);
   - se tiver imagens, você roda o upload pro CDN: `python upload-imagens-readme.py "docs\<Seção>"`;
   - religo os links `/docs/…` e `/reference/…` que a página usar;
   - removo a linha correspondente deste arquivo.
3. Você dá `git add -A && git commit && git push` nos **dois** repositórios.

> Regra atual: o hub só mostra páginas prontas. Páginas ainda "Em construção" continuam **só no Doc-v2** (não sobem com `hidden: true`).


## Para Desenvolvedores

- **Ferramentas** — `paraDesenvolvedores/ferramentas/index.md`
- **Connector Tester** — `paraDesenvolvedores/ferramentas/connectorTester.md`
- **Opus TPP Demo** — `paraDesenvolvedores/ferramentas/opusTppDemo.md`
- **Quick Simulator** — `paraDesenvolvedores/ferramentas/quickSimulator.md`
- **Classe utilitária camelHelper** — `paraDesenvolvedores/perfis/detentorTransmissor/camelHelper.md`
- **Componentes Camel Suportados** — `paraDesenvolvedores/perfis/detentorTransmissor/componentes.md`


## Implantação

- **Diretório de Participantes — Homologação** — `implantacao/diretorioHml/index.md`
- **Integração** — `implantacao/integracao/index.md`
- **Checklist: Detentor de Conta / Transmissor de Dados** — `implantacao/integracao/checklistDetentorTransmissor.md`
- **Checklist: Iniciador de Transação de Pagamento (ITP)** — `implantacao/integracao/checklistItp.md`
- **Checklist: Receptor de Dados** — `implantacao/integracao/checklistReceptor.md`


## Preparativos para Produção

- **Preparativos para Produção** — `preparativosProducao/index.md`
- **Diretório de Participantes — Produção** — `preparativosProducao/diretorioPrd/index.md`
- **Cadastro — Diretório de Participantes PRD** — `preparativosProducao/diretorioPrd/cadastro.md`
- **Conceito — Diretório de Participantes PRD** — `preparativosProducao/diretorioPrd/conceito.md`


## Acompanhamento em Produção

- **Acompanhamento em Produção** — `acompanhamentoProducao/index.md`
- **Customer Service Opus** — `acompanhamentoProducao/customerService/index.md`
- **Diretório de Participantes — Produção** — `acompanhamentoProducao/diretorioPrd/index.md`
- **Relatórios Regulatórios** — `acompanhamentoProducao/relatoriosRegulatorios/index.md`
- **Relatórios — OpusTPP** — `acompanhamentoProducao/relatoriosRegulatorios/opustppRelatorios.md`
- **Relatórios Semanais — Plataforma** — `acompanhamentoProducao/relatoriosRegulatorios/plataformaSemanal.md`
- **Relatório Semestral — Plataforma** — `acompanhamentoProducao/relatoriosRegulatorios/plataformaSemestral.md`
- **Customização Visual** — `acompanhamentoProducao/portalBackoffice/customizacao.md`
- **Falhas e Indisponibilidades** — `acompanhamentoProducao/portalBackoffice/falhasIndisponibilidades.md`
- **Autenticação via Federation** — `acompanhamentoProducao/portalBackoffice/federation.md`

---

## Links pendentes (neutralizados no hub)

Estes links apontavam para páginas que **não existem no hub**. Na auditoria eles foram **transformados em texto** (deixaram de ser links) para não ficarem quebrados. Quando a página de destino for criada/migrada, é só religar como `/docs/<slug>` nos arquivos listados.

### "Implantação da Plataforma" (destino sugerido: `/docs/implantacaodaplataforma`)
Página de visão geral do setup/implantação — ainda não existe no hub. Links neutralizados em:
- `Introdução/perfis/dadosAbertosConceito.md`
- `Introdução/perfis/detentorDeContas.md`
- `Introdução/perfis/itpConceito.md`
- `Introdução/perfis/receptorDeDados.md`
- `Introdução/perfis/transmissorDeDados.md`
- `Para Desenvolvedores/perfisIntegracao/itp/index.md`
- `Para Desenvolvedores/perfisIntegracao/receptor/index.md`

### "Compartilhamento de Dados" (destino sugerido: `/docs/compartilhamentodedados`)
Página conceitual — não migrada. Link neutralizado em:
- `Para Desenvolvedores/index.md`

### "APIs Internas" (destino sugerido: `/docs/apisinternas`)
Página não migrada. Link neutralizado em:
- `Produtos/iniciacaoDePagamentos/funcionamento/webhooks.md`

### "approvePaymentConsentCreation" (era referência mal-apontada)
Apontava para `/docs/approvepaymentconsentcreation_v3`, que não existe. Se for uma rota de API, o correto é apontar para o endpoint em `/reference/…` (ou para a seção interna "Solução provisória para rota approvePaymentConsentCreation" da própria página). Neutralizado em:
- `Para Desenvolvedores/perfisIntegracao/detentorTransmissor/discovery.md`

> Observação: também há 2 links legado (para arquivos `.yml`/`.json` de anexos) que foram neutralizados em `Acompanhamento em Produção/portalBackoffice/apisConsentimentos/index.md` e no `discovery.md` — como os anexos não vão para o hub, viraram texto.

