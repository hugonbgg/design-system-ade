# Design System Smart Sampa: regras para agentes

Este projeto usa o design system Smart Sampa (pacote `@ade/design-system`). Siga estas regras em toda tela, componente ou ajuste visual. A referência completa (tabela de cores, eixos, tom de voz) está no `README.md` deste pacote.

## Como os tokens chegam ao projeto

- O CSS principal importa, nesta ordem: `tailwindcss`, `@ade/design-system/tokens.css`, `@ade/design-system/tailwind.css`.
- As fontes vêm do Google Fonts por `<link>` no `index.html`: Open Sans (300, 400, 600) e Lexend Exa (300, 500, 700). Kallisto, quando houver licença, entra na frente da pilha sozinha.
- Nunca edite `tokens.css` nem `tailwind.css`: são gerados a partir de `tokens.json` no repositório do design system.

## Cores

- Use só as classes dos tokens: `bg-surface`, `bg-surface-raised`, `text-ink`, `text-ink-muted`, `border-line`, `bg-rosa`, `bg-lilas`, `bg-azul-claro`, `bg-verde`, `bg-azul-escuro`, `bg-preto`.
- Nunca escreva HEX, `rgb()` ou cores da paleta padrão do Tailwind (`bg-blue-500`, `text-gray-400`, `bg-slate-900` etc.). Se faltar uma cor, pare e diga qual falta; não invente.
- Fundo de tela: `bg-surface`. Painéis e cartões: `bg-surface-raised`. Texto: `text-ink`; secundário: `text-ink-muted`.
- Sobre `bg-rosa`, `bg-azul-claro` e `bg-verde`, o texto é `text-on-claro`. Sobre `bg-lilas`, `bg-azul-escuro` e `bg-preto`, o texto é `text-branco`.
- Texto colorido só sobre fundo escuro: `text-verde`, `text-azul-claro` ou `text-rosa`. Nunca `text-lilas` como texto.
- Cada eixo tem cor fixa: SINCRONIZAR = rosa, PROPAGAR = lilás, CONECTAR = azul-claro, RESTAURAR = verde, IMAGINAR = azul-escuro.
- `logo-azul-marinho` e `logo-azul` são só do logotipo. Nunca use em interface.

## Status

- Três estados: estável, alerta, crítico.
  - Fill: `bg-status-estavel`, `bg-status-alerta`, `bg-status-critico`.
  - Texto: `text-status-estavel-texto`, `text-status-alerta-texto`, `text-status-critico-texto`.
- Sobre `bg-status-alerta`, o texto é `text-on-claro`. Sobre `bg-status-estavel` e `bg-status-critico`, o texto é `text-branco`.
- Região de mapa em crise: `bg-status-critico-area`.
- Status nunca vai só na cor: sempre com ícone e palavra ("ALERTA", "CRÍTICO", "ESTÁVEL").

## Tipografia

- Títulos e rótulos: `font-display` (Kallisto), sempre em caixa alta. Textos: `font-text` (Open Sans).
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
