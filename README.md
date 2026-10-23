# Quebrabloco

Jogo 3D de quebrar blocos (estilo Brick Breaker) feito com three.js, num único arquivo HTML.

**Jogar:** https://costardiv1.github.io/quebrabloco/

- 4 mundos com 5 fases e um chefão cada: (Des)Construção, Praia Praiana, Orien Tal e Euro Peu
- 11 veículos no lugar da plataforma, cada um com seu som de motor (sirene na viatura, nos bombeiros e na ambulância), e um veículo de prêmio por mundo
- Moedas que caem dos caixotes e blocos, e uma garagem para comprar veículos
- Modo Caos: mundo sorteado, chefão, chuva de power-ups e debuffs, caixotes caindo e blocos que andam
- Dificuldade Fácil, Normal ou Difícil (velocidade da bola), com um recorde para cada uma
- Quatro ângulos de câmera (alta, média, deitada e rasante), ajustados para PC e celular
- Qualidade gráfica HD, SD ou Leve (no menu ou tecla Q), que se ajusta sozinha em PCs mais fracos
- Power-ups, debuffs (como Ventania e Bola Fantasma), caixotes surpresa, música e sons gerados por código
- Modo desenvolvedor na versão de desenvolvimento: velocidade da bola, tamanho e sensibilidade do veículo, simulação de celular e atalhos para mundos, fases e veículos

## Arquivos

- `index.html`: o jogo inteiro (HTML, CSS e JavaScript), versão pública sem modo desenvolvedor. Modelos, texturas, sons e músicas são gerados por código.
- `scripts/gerar_index.py`: gera o `index.html` a partir da versão de desenvolvimento, que fica só no computador do autor.
- `chefoes.md`: o desenho original dos chefões.

## Créditos

Feito por Vinícius Costardi e Claude Code. Desenvolvido em vibe code.

- three.js r170 (licença MIT)
- Fontes do Google Fonts (SIL Open Font License 1.1): Bungee, Barlow, Barlow Condensed, Sedgwick Ave, Pacifico, Potta One e Ma Shan Zheng
