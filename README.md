# Quebrabloco

Jogo 3D de quebrar blocos (estilo Brick Breaker) feito com three.js, num único arquivo HTML.

**Jogar:** https://costardiv1.github.io/quebrabloco/

- 4 mundos com 5 fases e um chefão cada: (Des)Construção, Praia Praiana, Orien Tal e Euro Peu
- Veículos no lugar da plataforma, com prêmios por mundo
- Moedas que caem dos caixotes e blocos, e uma garagem para comprar veículos
- Modo Caos: mundo sorteado, chefão, chuva de power-ups e debuffs, caixotes caindo e blocos que andam
- Qualidade gráfica HD, SD ou Leve (tecla Q), que se ajusta sozinha em PCs mais fracos
- Power-ups, debuffs, caixotes surpresa, música e sons gerados por código
- Modo desenvolvedor com velocidade da bola, troca de mundo, fase e veículo

## Arquivos

- `index.html`: o jogo inteiro (HTML, CSS e JavaScript), versão pública sem modo desenvolvedor. Modelos, texturas, sons e músicas são gerados por código.
- `scripts/gerar_index.py`: gera o `index.html` a partir da versão de desenvolvimento, que fica só no computador do autor.
- `chefoes.md`: o desenho original dos chefões.

## Créditos

Desenvolvido em vibecode por Vinícius Costardi.

- three.js r170 (licença MIT)
- Fontes do Google Fonts (SIL Open Font License 1.1): Bungee, Barlow, Barlow Condensed e Sedgwick Ave
