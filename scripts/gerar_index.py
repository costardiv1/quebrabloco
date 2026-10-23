"""Build the public index.html for GitHub Pages from brickstorm.html.

brickstorm.html is the developer build written for Claude Artifacts, which supply the
document skeleton. This turns developer mode off (DEV_BUILD = false) and wraps the page
in a full standalone document: doctype, charset, viewport, and the base styles the
Artifact host would otherwise provide. Run it after every change to the game:

    python scripts/gerar_index.py
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
src = (root / 'brickstorm.html').read_text(encoding='utf-8')
flag = 'const DEV_BUILD = true;'
if src.count(flag) != 1:
    raise SystemExit('DEV_BUILD flag not found in brickstorm.html')
src = src.replace(flag, 'const DEV_BUILD = false;')

marker = '</style>\n'
cut = src.index(marker) + len(marker)
head, body = src[:cut], src[cut:]

page = (
    '<!doctype html>\n<html lang="pt-BR">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="theme-color" content="#1c1e21">\n'
    '<meta name="description" content="Quebrabloco: jogo 3D de quebrar blocos com mundos, chefões e veículos.">\n'
    '<style>html, body { margin: 0; } [hidden] { display: none !important; }</style>\n'
    + head
    + '</head>\n<body>\n'
    + body
    + '</body>\n</html>\n'
)
(root / 'index.html').write_text(page, encoding='utf-8', newline='\r\n')
print('index.html gerado,', len(page), 'caracteres')
