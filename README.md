# Quebrabloco

Jogo 3D de quebrar blocos (estilo Brick Breaker) feito com three.js, num único arquivo HTML.

**Jogar:** https://costardiv1.github.io/quebrabloco/

- 4 mundos com 5 fases e um chefão cada: (Des)Construção, Praia Praiana, Orien Tal e Euro Peu
- Veículos no lugar da plataforma, com prêmios por mundo
- Moedas que caem dos caixotes e blocos, e uma garagem para comprar veículos
- Power-ups, debuffs, caixotes surpresa, música e sons gerados por código
- Modo desenvolvedor com velocidade da bola, troca de mundo, fase e veículo

## Arquivos

- `brickstorm.html`: o jogo inteiro (HTML, CSS e JavaScript). Modelos, texturas, sons e músicas são gerados por código.
- `index.html`: a mesma página com o cabeçalho completo, para o GitHub Pages. Gere de novo depois de mudar o jogo:
  `python scripts/gerar_index.py`
- `chefoes.md`: o desenho original dos chefões.

## Créditos

Desenvolvido em vibecode por Vinícius Costardi.

- three.js r170 (licença MIT)
- Fontes do Google Fonts (SIL Open Font License 1.1): Bungee, Barlow, Barlow Condensed e Sedgwick Ave
