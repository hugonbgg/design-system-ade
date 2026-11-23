"""Gera tokens.css e tailwind.css a partir de tokens.json.

Uso:  python build-tokens.py
Edite sempre o tokens.json; tokens.css e tailwind.css são gerados e não devem ser editados à mão.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
tokens = json.loads((ROOT / "tokens.json").read_text(encoding="utf-8"))

ALIAS = re.compile(r"^\{([A-Za-z0-9_.-]+)\}$")


def css_value(v):
    m = ALIAS.match(str(v))
    return f"var(--{m.group(1)})" if m else v


def px(v):
    return f"{v}px" if isinstance(v, (int, float)) and v != 0 else str(v)


themes = [t["id"] for t in tokens["color"]["themes"]]
first = themes[0]
color_tokens = tokens["color"]["tokens"]

out = [f"/* {tokens['name']} — gerado de tokens.json por build-tokens.py. Não edite à mão. */", ""]

# Fontes servidas pelo próprio projeto (arquivos fora deste repositório)
web = tokens.get("webFonts")
if web:
    out.append(f"/* {web['note']} */")
    for face in web["faces"]:
        out.append("@font-face {")
        out.append(f"  font-family: \"{face['family']}\";")
        out.append(f"  src: url(\"{web['basePath']}{face['file']}\") format(\"woff2\");")
        out.append(f"  font-weight: {face['weight']};")
        out.append("  font-style: normal;")
        out.append("  font-display: swap;")
        out.append("}")
    out.append("")

# Tema padrão (primeiro tema) em :root
out.append(f":root,\n[data-theme=\"{first}\"] {{")
out.append(f"  color-scheme: {'dark' if first == 'dark' else 'light'};")
for t in color_tokens:
    v = t["value"]
    val = v.get(first) if isinstance(v, dict) else v
    out.append(f"  --{t['name']}: {css_value(val)};")
out.append("}")
out.append("")

# Demais temas: só o que muda
for th in themes[1:]:
    out.append(f"[data-theme=\"{th}\"] {{")
    out.append(f"  color-scheme: {'dark' if th == 'dark' else 'light'};")
    for t in color_tokens:
        v = t["value"]
        if isinstance(v, dict) and th in v:
            out.append(f"  --{t['name']}: {css_value(v[th])};")
    out.append("}")
    out.append("")

# Fontes, espaçamento, cantos
out.append(":root {")
for key, stack in tokens["type"]["families"].items():
    out.append(f"  --font-{key}: {stack};")
for fam in ("spacing", "radius"):
    for t in tokens.get(fam, {}).get("tokens", []):
        out.append(f"  --{t['name']}: {px(t['value'])};")
out.append("}")
out.append("")

# Classes de estilo tipográfico (em @layer components: utilitários do Tailwind vencem)
out.append("@layer components {")
for group in tokens["type"]["groups"]:
    out.append(f"/* {group['name']} */")
    for s in group["styles"]:
        fam = s.get("family", group["family"])
        out.append(f".{s['name']} {{")
        out.append(f"  font-family: var(--font-{fam});")
        out.append(f"  font-size: {px(s['fontSize'])};")
        out.append(f"  line-height: {s['lineHeight']};")
        out.append(f"  font-weight: {s['fontWeight']};")
        if "letterSpacing" in s:
            out.append(f"  letter-spacing: {px(s['letterSpacing'])};")
        if group["family"] == "display" and s["name"] != "numero":
            out.append("  text-transform: uppercase;")
        if s["name"] == "numero":
            out.append("  font-variant-numeric: tabular-nums;")
        out.append("}")
    out.append("")

out.append("}")
out.append("")

(ROOT / "tokens.css").write_text("\n".join(out), encoding="utf-8")
# ---------- tailwind.css (Tailwind v4) ----------
tw = [f"/* {tokens['name']} — tema Tailwind v4 gerado de tokens.json por build-tokens.py. Não edite à mão. */",
      "/* Importe depois de tokens.css. As cores apontam para as variáveis de tokens.css, então seguem data-theme. */", ""]
tw.append("@theme inline {")
for t in color_tokens:
    tw.append(f"  --color-{t['name']}: var(--{t['name']});")
tw.append("}")
tw.append("")
# Fontes e cantos não mudam com o tema: valores literais (os mesmos de tokens.css)
tw.append("@theme {")
for key, stack in tokens["type"]["families"].items():
    tw.append(f"  --font-{key}: {stack};")
for t in tokens.get("radius", {}).get("tokens", []):
    tw.append(f"  --{t['name']}: {px(t['value'])};")
tw.append("}")
tw.append("")
(ROOT / "tailwind.css").write_text("\n".join(tw), encoding="utf-8")

print(f"tokens.css e tailwind.css gerados: {len(color_tokens)} cores, temas {themes}")
