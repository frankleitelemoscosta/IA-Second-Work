# Trabalho IA: Comparação entre Algoritmos de Busca Informada

## Objetivo 🎯

Implementar e comparar dois diferentes algoritmos de busca informada: A* (A-estrela) e Busca Gulosa. O objetivo é aplicá-los ao problema clássico do labirinto para analisar eficiência, consumo de recursos e eficácia na busca de soluções.

![Imagem 1](<img/Captura de tela de 2024-11-08 12-36-18.png>)

## Descrição dos algoritmos implementados 📜
O algoritmo A* (A Estrela) é uma técnica de busca de caminho mais curto em grafos ou redes.Quanto a seu funcionamento ele vai se prover de um nó inicial, um nó final, alem de usar dos vizinho de um nó(conexões) 
o custo local e o global. Alem disso existem duas listas as quais uma vai armazenar os nós que não foram anali
sados os seguintes quesitos:

* Custo acumulado
* estimativa até o nó de objetivo
* Custo global

E com isso se inicia uma sequência de fatos que estruturam o caminhamento pelo grafo com as posições dos elementos
da Figura 1, os quais são:

1. Inicialização: Cria-se uma lista de nós abertos (nó inicial) e uma lista de nós fechados (vazia).
2. Avaliação: Para cada nó aberto, calcula-se:
- Custo acumulado (g): soma dos custos desde o nó inicial.
- Heurística (h): estimativa da distância ao nó objetivo.
- Custo total (f): g + h.
1. Seleção: Escolhe-se o nó com menor custo total (f).
2. Expansão: Adicionam-se os nós vizinhos não visitados à lista de abertos.
3. Atualização: Atualiza-se a lista de fechados com o nó selecionado.
4. Repetição: Volta-se ao passo 2 até encontrar o nó objetivo.

Este algoritmo é projetado para encontrar o caminho mais curto entre dois pontos, mas isso não significa que ele 
encontra a melhor solução para o problema.

## Estrutura do Projeto 🏗️
- **Linguagem:** Python.
- **Bibliotecas utilizadas:**
  - collections.deque: para implementar a fila de pesquisa no BFS.
  - numpy: para manipulação e conversão de arrays.
  - time: para medir o tempo de execução.
  - tracemalloc : para medir o consumo de memória.

## Resultados das medicões de desempenho ⏱️
![image](https://github.com/user-attachments/assets/f3266c97-c539-4710-8ca1-eb4c150c505f)

## Análise comparativa dos algoritmos 🔍

As principais diferenças entre os algoritmos Guloso e A* são:

Algoritmo Guloso

1. Escolha do próximo nó: Baseia-se apenas na heurística local (custo imediato).
2. Custo considerado: Apenas o custo do próximo passo.
3. Objetivo: Encontrar uma solução razoável, não necessariamente ótima.
4. Comportamento: Avança rapidamente, mas pode ficar preso em ótimos locais.

Algoritmo A*

1. Escolha do próximo nó: Combina custo acumulado (g) e heurística (h).
2. Custo considerado: Soma do custo acumulado e heurística (f = g + h).
3. Objetivo: Encontrar o caminho mais curto possível.
4. Comportamento: Equilibra custo e heurística para evitar ótimos locais.

Principais diferenças

1. Custo considerado: Guloso considera apenas o custo imediato, enquanto A* considera o custo total.
2. Heurística: Guloso usa apenas heurística local, enquanto A* usa heurística global (considera o objetivo).
3. Ótimo: A* busca o ótimo global, enquanto Guloso busca uma solução razoável.

## Considerações Finais 📝
- A* é o algoritmo ideal para encontrar o menor caminho em grafos, especialmente quando a precisão é essencial.
- Busca Gulosa pode ser mais rápida, mas é menos confiável em termos de encontrar a solução mais curta.
- Os resultados variam dependendo do tamanho e da complexidade do grafo.
## Autores

- Frank Leite Lemos Costa – Aluno do 6º período de Engenharia da Computação.
- Mateus Henrique Pereira – Aluno do 8º período de Engenharia da Computação.