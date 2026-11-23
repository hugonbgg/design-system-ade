# Design System Smart Sampa: regras para agentes

Este projeto usa o design system Smart Sampa (pacote `@ade/design-system`). Siga estas regras em toda tela, componente ou ajuste visual. A referência completa (tabela de cores, eixos, tom de voz) está no `README.md` deste pacote.

## Como os tokens chegam ao projeto

- O CSS principal importa, nesta ordem: `tailwindcss`, `@ade/design-system/tokens.css`, `@ade/design-system/tailwind.css`.
- Kallisto é licenciada (comprada da Device) e servida pelo próprio projeto: os arquivos `Kallisto-Thin/Light/Medium/Bold.woff2` ficam em `public/fonts/kallisto/`. O `tokens.css` já declara o `@font-face` apontando para lá.
- Nunca coloque os arquivos da Kallisto em repositório público, nem dentro deste pacote. Se o projeto for público, pare e avise.
- Saira (fonte de texto) e Lexend Exa (reserva da Kallisto) vêm do Google Fonts por `<link>` no `index.html`: Saira (300, 400, 500) e Lexend Exa (300, 500, 700).
- Nunca edite `tokens.css` nem `tailwind.css`: são gerados a partir de `tokens.json` no repositório do design system.

## Cores

- Use só as classes dos tokens: `bg-surface`, `bg-surface-raised`, `text-ink`, `text-ink-muted`, `border-line`, `bg-rosa`, `bg-lilas`, `bg-azul-claro`, `bg-verde`, `bg-azul-escuro`, `bg-preto`.
- Nunca escreva HEX, `rgb()` ou cores da paleta padrão do Tailwind (`bg-blue-500`, `text-gray-400`, `bg-slate-900` etc.). Se faltar uma cor, pare e diga qual falta; não invente.
- Fundo de tela: `bg-surface`. Painéis e cartões: `bg-surface-raised`. Texto: `text-ink`; secundário: `text-ink-muted`.
- Sobre `bg-rosa`, `bg-azul-claro` e `bg-verde`, o texto é `text-on-claro`. Sobre `bg-lilas`, `bg-azul-escuro` e `bg-preto`, o texto é `text-branco`.
- Texto colorido só sobre fundo escuro: `text-verde`, `text-azul-claro` ou `text-rosa`. Nunca `text-lilas` como texto.
- Cada eixo tem cor fixa: SINCRONIZAR = rosa, PROPAGAR = lilás, CONECTAR = azul-claro, RESTAURAR = verde, IMAGINAR = azul-escuro.
- `logo-azul-marinho` e `logo-azul` são só do logotipo. Nunca use em interface.

## Destaque

- Para item ativo ou selecionado, foco, link, progresso e botão principal, use o papel de destaque: `bg-destaque` com `text-on-destaque`, `text-destaque-texto`, `border-destaque`, `ring-destaque`.
- Nunca use uma cor de eixo (`rosa`, `azul-claro`…) como destaque genérico, e nunca use as cores de status como destaque: vermelho é só `status-critico`.
- Use o destaque com parcimônia: no máximo um elemento em destaque por área da tela (a ação principal ou o item selecionado). Em listas e grades de cards, a ação repetida de cada card não leva destaque: use `text-ink-muted` ou só o ícone de seta, já que o card inteiro é clicável.

## Véus sobre fotos

- Véus de contraste sobre foto ou vídeo (para o texto ficar legível) podem ser gradientes CSS. Use sempre cores dos tokens, por exemplo `bg-gradient-to-t from-surface/90 to-transparent`, ou `from-preto/80` quando a imagem é sempre escura.
- Isso não vale para os gradientes "pulsar" da marca: eles são fundos decorativos e só entram como imagem de `assets/gradientes/`.

## Status

- Três estados: estável, alerta, crítico.
  - Fill: `bg-status-estavel`, `bg-status-alerta`, `bg-status-critico`.
  - Texto: `text-status-estavel-texto`, `text-status-alerta-texto`, `text-status-critico-texto`.
- Sobre `bg-status-alerta`, o texto é `text-on-claro`. Sobre `bg-status-estavel` e `bg-status-critico`, o texto é `text-branco`.
- Região de mapa em crise: `bg-status-critico-area`.
- Status nunca vai só na cor: sempre com ícone e palavra ("ALERTA", "CRÍTICO", "ESTÁVEL"). A palavra pode ser a própria mensagem quando ela já diz o estado ("Não foi possível carregar a narração"): não acrescente "ALERTA:" na frente.

## Erros e avisos do app

- Falhas do próprio app (rede, áudio, carregamento) usam `text-status-alerta-texto` com o ícone `AlertTriangle` e uma mensagem que diga o que falhou.
- A ação de recuperação ("Tentar novamente") é neutra: `text-ink` com `border-line`, nunca amarela nem em destaque.
- `status-critico` fica para estados críticos da cidade ou falhas que impedem o uso do app, não para erros recuperáveis.
- Estados de liga e desliga que não são "ativo" (som desligado, por exemplo) só trocam o ícone, em `text-ink`. Sem destaque.

## Tipografia

- Títulos e rótulos: `font-display` (Kallisto), sempre em caixa alta. Textos: `font-text` (Saira). Nunca use Kallisto em parágrafos ou frases longas: em caixa baixa e bloco, ela cansa a leitura.
- Kallisto em caixa alta nunca fica com espaçamento normal ou fechado: as letras se encostam e o título vira um bloco. Mínimo de 0.05em em títulos, 0.06em em títulos de card e 0.1em em rótulos pequenos. As classes prontas já trazem esses valores; não sobrescreva com `tracking-normal`, `tracking-tight` etc.
- Pesos: títulos grandes em Light (`titulo-hero`, `titulo`); títulos de card e subtítulos em Medium (`titulo-card`, `subtitulo`); números em Bold (`numero`).
- Títulos de cards e de itens de lista usam `titulo-card`. Em espaços estreitos (carrossel, balão de mapa, barra do topo) pode reduzir o tamanho com `text-sm`, mantendo a classe.
- Links e ações secundárias não levam caixa alta: ficam na fonte de texto. Link ou ação só em texto (sem fundo nem borda) usa `text-ink-muted`. Botão secundário com fundo ou borda é um controle: usa `text-ink`.
- Pesos da fonte de texto (Saira): só 300, 400 e 500 (`font-light`, `font-normal`, `font-medium`). Nunca `font-semibold` ou `font-bold` em texto: esses pesos não são carregados e o navegador desenha um negrito falso.
- Texto de apoio (descrições de card, legendas) fica abaixo do título na hierarquia: `text-ink-muted` ou peso leve, nunca branco cheio maior que o título.
- Prefira as classes prontas: `titulo-hero`, `titulo`, `subtitulo`, `rotulo`, `numero`, `corpo`, `corpo-leve`, `legenda`.
- Não use outras famílias de fonte.

## Espaço e cantos

- Espaçamento na escala de 8: `2` (8px), `4` (16px), `6` (24px), `10` (40px). Por exemplo `p-4`, `gap-6`, `px-10`. Evite valores fora dela.
- Cantos: `rounded-tag` em tags, `rounded-painel` em painéis e cartões, `rounded-pill` em botões de chamada.

## Tema

- O padrão é escuro. Para claro, use `data-theme="light"` no `<html>` ou num contêiner. Nunca use as variantes `dark:` do Tailwind para trocar cor: os tokens já trocam sozinhos.

## Marca e imagens

- Logotipo só a partir de `@ade/design-system/assets/logos/`: `smartsampa-positivo.svg` sobre fundo claro, `smartsampa-negativo-branco.svg` sobre fundo escuro. Não recolora nem redesenhe.
- Gradientes de fundo só de `@ade/design-system/assets/gradientes/`, nunca recriados em CSS, e sem texto corrido por cima.
- Ícones: `lucide-react`, traço único. Sem emoji na interface.

## Texto da interface

- Português; títulos e chamadas em caixa alta, curtos, no imperativo: "TOQUE NA TELA PARA INICIAR", "ESCOLHA UM TEMA".
