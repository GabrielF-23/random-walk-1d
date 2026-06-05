# Gerador de Caminhante Aleatório 1D
Random Walk 1D Generator

🇧🇷 [Português](#português) | 🇺🇸 [English](#english)
# Português
## Sobre
Esse programa foi desenvolvido como exercicio de aprendizado durante minha Iniciação Cientifica.

O objetivo desse programa foi compreender os conceitos fundamentais de processos estocasticos, simulações computacionais e modelagem matematica atraves de um modelo simples de caminhante aleatorio em uma dimensão em Python.

## Descrição do modelo
Um caminhante começa de um ponto x = 0 (origem).
A cada passo ele tem 50% de chance de escolher dar um passo para direita ou esquerda.<br>
Cada passo novo é dado por:

        step = random.choice([1,2])

        if step == 1:
            x += 1
        else:
            x -= 1
            
Quando `step == 1`: ele soma 1 a posição x dele.<br>
Quando `step == 2`: ele subtrai 1 da posição x dele.<br>

Cada passo tem a mesma probabilidade de acontecer.<br>

### Parametros do modelo
Temos 2 parametros nesse modelo:<br>
-`r`: número de caminhantes.<br>
-`s`: número de passos.<br>

Altere como desejar, por padrão o modelo vem:<br>
`r = 1000`<br>
`s = 1000`

### Gráficos
Após escolher a quantidade de caminhantes e a quantidade de passos, execute o programa e 
ele vai gerar dois gráficos:<br>

#### Gráfico A: Trajetória dos caminhantes
Mostra a trajetória de todos os caminhantes ao longo dos passos.

#### Gráfico B: Histograma das posições finais.
Mostra a distruibuição das posições finais de cada caminhante.

## Ferramentas e Bibliotecas
- Python
- Matplotlib
- Random

## Licença
Este projeto está licenciado sob a licença MIT.

## Autor
Gabriel Freitas.

# English
WIP.







 
