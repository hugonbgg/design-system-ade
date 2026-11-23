Smart Sampa é a central de inteligência da cidade de São Paulo. A identidade parte de uma ideia: **a cidade é um organismo que pulsa**, uma rede de informação que conecta secretarias, territórios e pessoas. Este sistema cobre cores, gradientes, tipografia e logotipo, e serve às telas interativas (mesa do Átrio, Maquete, Sincronizar) e às peças impressas.

## Conteúdo e tom

- Escreva em português, com versão em inglês quando a tela tiver o seletor **EN**.
- Títulos e chamadas vão em **caixa alta**, curtos e diretos: "O QUE FAZ UMA CIDADE PULSAR?", "EXPLORE OS FLUXOS DA CIDADE", "COMO SÃO PAULO FUNCIONA?".
- Chamadas de ação falam com quem está na frente da tela, no imperativo: "TOQUE NA TELA PARA INICIAR", "ESCOLHA UMA SECRETARIA PARA INICIAR", "SELECIONE UM TEMA E DESCUBRA COMO CADA SISTEMA INTERAGE COM OS TERRITÓRIOS DA CIDADE".
- Em atividades em grupo, use a segunda pessoa do plural: "Coordenem ações para minimizar os impactos sobre a população."
- Estados da cidade são frases afirmativas curtas: "A CIDADE ESTÁ SEGURA!", "SISTEMAS AMBIENTAIS ESTÁVEIS", "QUALIDADE AMBIENTAL EM ALERTA".
- Não use emoji.

## Cores

A paleta oficial tem seis cores. Use os nomes da paleta como nome dos tokens.

| Token | Nome | HEX | Eixo temático |
|---|---|---|---|
| `rosa` | Rosa | #DC58E0 | SINCRONIZAR (Gestão) |
| `lilas` | Lilás | #6F51B7 | PROPAGAR (Demografia e Cultura) |
| `azul-claro` | Azul Claro | #4AACD3 | CONECTAR (Mobilidade) |
| `verde` | Verde | #28C6A8 | RESTAURAR (Meio Ambiente e Território) |
| `azul-escuro` | Azul Escuro | #0E254F | IMAGINAR (Futuros Urbanos) |
| `preto` | Preto | #191919 | Fundo de peças em negativo |

- Telas são escuras: use `surface` (= `azul-escuro`) como fundo e `ink` (branco) como texto. O tema **Telas (escuro)** é o padrão; **Impresso (claro)** serve para pranchas, cartazes e documentos.
- Cada eixo temático tem uma cor fixa. Use a cor do eixo nas tags, nos nós do infográfico e nos destaques daquela sala. Não troque a cor de um eixo.
- Sobre fills `rosa`, `azul-claro` e `verde`, escreva com `on-claro` (azul-escuro). Sobre `lilas`, `azul-escuro` e `preto`, escreva com `branco`.
- Texto colorido só vai sobre `azul-escuro`: `verde`, `azul-claro` e `rosa` passam de 4,5:1 ali. `lilas` não funciona como texto sobre o fundo escuro (2,6:1). No tema claro, nenhuma cor da paleta serve para texto pequeno; use `ink`.
- O caderno escreve as etiquetas da paleta em branco sobre todas as cores. Sobre `azul-claro` e `verde` isso fica abaixo de 3:1; nas telas, prefira `on-claro`.
- `logo-azul-marinho` e `logo-azul` são exclusivas do logotipo. Não use em interface.
- **Destaque** é um papel, não uma cor nova: `destaque` aponta hoje para `azul-claro`. Use-o para item ativo, foco, link, progresso e botão principal, com `on-destaque` para o texto por cima e `destaque-texto` para texto colorido. Nunca use uma cor de eixo ou de status como destaque genérico.
- Use o destaque com parcimônia: no máximo um elemento em destaque por área. Em grades de cards, a ação repetida de cada card fica em `ink-muted`.
- `surface-raised`, `ink-muted` e `line` são derivados da paleta para dar estrutura às telas. Eles não aparecem no caderno.

## Estados da cidade (status)

Na mesa interativa, cada sistema da cidade está em um de três estados. A cor de status é separada da cor do eixo: um eixo continua com sua cor, e o status aparece no ícone, na tag ou na região do mapa.

| Estado | Fill | Texto | Exemplo real |
|---|---|---|---|
| Estável | `status-estavel` | `status-estavel-texto` | "SISTEMAS AMBIENTAIS ESTÁVEIS", "A CIDADE ESTÁ SEGURA!" |
| Alerta | `status-alerta` | `status-alerta-texto` | "QUALIDADE AMBIENTAL EM ALERTA", triângulos no mapa |
| Crítico | `status-critico` | `status-critico-texto` | "INFRAESTRUTURA PRECISANDO DE MANUTENÇÃO" |

- Status nunca vai só na cor. Cada estado leva sempre a frase do estado e um ícone: triângulo para alerta, ícone do sistema sobre fill vermelho para crítico. Estável e crítico têm luminosidade parecida e não se distinguem só pelo tom.
- Sobre `status-critico` e `status-estavel`, use ícone e texto em `branco`. Sobre `status-alerta`, use `on-claro`.
- Para marcar uma região do mapa em crise, use o véu `status-critico-area` por cima do mapa.
- Em texto, use sempre os tokens `-texto`, que passam de 4,5:1 nos dois temas.
- Os três fills foram amostrados das imagens das telas (pp. 133–134). Os tons `-texto` derivados são ajustes de contraste.

## Gradientes

Os gradientes "pulsar" são fundos de luz difusa: faixas verticais de `lilas`, `rosa` e `azul-claro` com verde-água atravessando um campo de `azul-escuro` que escurece até `preto`. Estão no grupo de assets **Gradientes**.

- Use os gradientes como fundo de telas de abertura, menus e cartazes. Não use atrás de texto corrido.
- Coloque o texto sobre a área escura (`azul-escuro` / `preto`) do gradiente, em `branco`.
- Não recrie os gradientes em CSS. Use as imagens do grupo.
- Véus de contraste sobre fotos (para o texto ficar legível) podem ser gradientes CSS, sempre com cores dos tokens: `surface` ou `preto` com transparência. Eles não são os gradientes da marca.

## Tipografia

| Família | Papel | Pesos |
|---|---|---|
| **Kallisto** | Títulos, rótulos, números (`display`) | Light 300 para títulos, Medium 500 para rótulos, Bold 700 para números |
| **Open Sans** | Textos (`text`) | Light 300, Regular 400 |

- Títulos (`titulo-hero`, `titulo`, `subtitulo`, `titulo-card`) em Kallisto e sempre em caixa alta.
- Kallisto em caixa alta sempre com espaçamento aberto: 0.05em nos títulos, 0.06em em títulos de card, 0.1em em rótulos. Com espaçamento fechado as letras se encostam. Títulos grandes em Light, títulos de card e subtítulos em Medium.
- Texto de apoio (descrições, legendas) fica abaixo do título na hierarquia: `ink-muted` ou peso leve.
- Rótulos, tags e botões em `rotulo`: Kallisto Medium 13px, caixa alta, espaçamento de 0.08em.
- Indicadores numéricos em `numero`, com três dígitos ("040", "045").
- Texto corrido em `corpo` (Open Sans 16/24). Em telas escuras, `corpo-leve` só a partir de 16px.
- Kallisto é licenciada (comprada da Device) e servida por cada projeto em `public/fonts/kallisto/` (Thin, Light, Medium e Bold em `.woff2`). O `tokens.css` já declara o `@font-face`. Os arquivos não ficam neste repositório, que é público: guarde o pacote original num local privado do time. Sem os arquivos, a pilha usa **Lexend Exa** (Google Fonts) como reserva. Open Sans vem do Google Fonts.

## Espaçamento e cantos

- Espaçamento em quatro passos: `space-2` (8), `space-4` (16), `space-6` (24), `space-10` (40). As margens externas das telas usam `space-10`.
- Cantos: `radius-tag` (4) em tags, `radius-painel` (12) em painéis e cartões de evento, `radius-pill` em botões de chamada.

## Logotipo

O logotipo é o wordmark **smartsampa** ("smart" leve, "sampa" em negrito) com a linha "central de inteligência da cidade". Está no grupo de assets **Logos**.

- Sobre fundo claro: `smartsampa-positivo.svg` (`logo-azul-marinho` com linha em #231F20).
- Sobre `preto` ou `azul-escuro`: `smartsampa-negativo-branco.svg`, ou `smartsampa-negativo-azul.svg` sobre `preto`.
- Não recolora, não distorça e não separe a linha de apoio do wordmark.

## Iconografia

O caderno não define um conjunto de ícones. As telas usam pictogramas lineares brancos (mão de toque, globo do seletor de idioma, triângulos de alerta no mapa). Até que um conjunto seja fornecido, use traço branco de espessura única sobre fundo escuro e não use emoji.

## Arquivos e uso nos projetos

| Arquivo | O que é |
|---|---|
| `tokens.json` | Fonte única de todos os valores. Edite só aqui. |
| `tokens.css` | Variáveis CSS e classes tipográficas. Gerado, não edite à mão. |
| `tailwind.css` | Tema Tailwind v4 (`bg-surface`, `font-display`, `rounded-painel`…). Gerado, não edite à mão. |
| `build-tokens.py` | Gera `tokens.css` e `tailwind.css`: rode `python build-tokens.py` depois de mudar o `tokens.json`. |
| `AGENTS.md` | Regras para agentes de IA seguirem o design system. |
| `package.json` | Publica esta pasta como o pacote `@ade/design-system`. |
| `assets/logos/`, `assets/gradientes/` | Logotipo em SVG e os três gradientes "pulsar". |

### Num projeto com Tailwind v4

1. Instale o pacote pelo GitHub: `"@ade/design-system": "github:hugonbgg/design-system-ade"` no `package.json` e `npm install` (ou `bun install`). O repositório é público, então instala em qualquer máquina ou deploy sem token. Para atualizar depois de uma mudança aqui, rode `npm update @ade/design-system`.
2. No CSS principal:

```css
@import "tailwindcss";
@import "@ade/design-system/tokens.css";
@import "@ade/design-system/tailwind.css";
```

3. Copie os arquivos da Kallisto (`Kallisto-Thin.woff2`, `-Light`, `-Medium`, `-Bold`) para `public/fonts/kallisto/` do projeto. Só em repositório privado.
4. No `index.html`, carregue as fontes do Google (Open Sans e a reserva Lexend Exa):

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend+Exa:wght@300;500;700&family=Open+Sans:wght@300;400;600&display=swap">
```

5. Para o agente seguir as regras, crie um `CLAUDE.md` na raiz do projeto com a linha:

```
@node_modules/@ade/design-system/AGENTS.md
```

Uso:

```html
<main class="bg-surface text-ink p-10">
  <h1 class="titulo-hero">O que faz uma cidade pulsar?</h1>
  <span class="bg-status-alerta text-on-claro rotulo rounded-tag px-2">Alerta</span>
</main>
```

O tema escuro é o padrão. Para o claro, coloque `data-theme="light"` no `<html>` ou em qualquer contêiner.
