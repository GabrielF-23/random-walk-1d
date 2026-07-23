# Gerador de Caminhante Aleatório Gaussiano 1D
Gaussian Random Walk 1D Generator

🇧🇷 [Português](#português) | 🇺🇸 [English](#english)

# Português

## Sobre

Esse programa foi desenvolvido como exercício de aprendizado durante minha Iniciação Científica.

O objetivo desse programa foi compreender os conceitos fundamentais de processos estocásticos, difusão, simulações computacionais e modelagem matemática através de um modelo de caminhante aleatório gaussiano em uma dimensão utilizando Python.

## Descrição do modelo

Um caminhante começa na posição

```
x = 0
```

A cada passo, seu deslocamento é sorteado a partir de uma distribuição normal (gaussiana) de média zero e desvio padrão σ:

```
Δx ~ N(0, σ)
```

No código, esse deslocamento é gerado por

```python
step = np.random.normal(0, sigma)
```

A posição do caminhante é então atualizada por

```python
x += step
```

Como a média da distribuição é igual a zero, não existe direção preferencial para o movimento. Entretanto, o tamanho de cada passo pode variar continuamente, diferentemente do modelo clássico onde os deslocamentos possuem apenas dois valores possíveis.

O parâmetro σ controla a intensidade das flutuações:

- valores pequenos produzem trajetórias mais suaves;
- valores maiores produzem trajetórias mais dispersas.

## Parâmetros do modelo

O modelo possui três parâmetros principais:

- `n_steps`: número de passos de cada caminhante;
- `n_runs`: número total de caminhantes simulados;
- `sigma`: desvio padrão da distribuição normal utilizada para gerar cada deslocamento.

Por padrão o programa utiliza

```
n_steps = 1000
n_runs = 1000
sigma = 0.1
```

## Gráficos

Após executar o programa, são gerados três gráficos.

### Gráfico A — Trajetórias dos caminhantes

Mostra a evolução temporal da posição de todos os caminhantes ao longo da simulação.

### Gráfico B — Distribuição das posições finais

Apresenta um histograma das posições finais dos caminhantes após todos os passos, permitindo observar a distribuição estatística dos resultados.

### Gráfico C — Deslocamento Quadrático Médio (MSD)

Mostra o deslocamento quadrático médio

```
⟨x²(t)⟩
```

calculado para todos os caminhantes em função do número de passos.

Além dos dados simulados, também é apresentada a solução teórica

```
⟨x²(t)⟩ = σ² t
```

permitindo comparar a simulação numérica com o comportamento esperado para um processo difusivo gaussiano.

## Ferramentas e Bibliotecas

- Python
- NumPy
- Matplotlib

## Licença

Este projeto está licenciado sob a licença MIT.

## Autor

Gabriel Freitas.

# English

WIP.
