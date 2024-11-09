# Busca Gulosa e A-estrela
## Objetivo
Implementar e comparar dois diferentes algoritmos de busca informada (A* e Busca Gulosa) aplicados a um problema classico de busca - o problema do labirinto (Imagem 1). Pode-se utilizar algoritmos ´
discutidos em sala de aula ou outros algoritmos conhecidos. A atividade pode ser realizada individualmente ou em dupla.

![Imagem 1](<Captura de tela de 2024-11-08 12-36-18.png>)

## Descrição dos algoritmos implementados
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

## Resultados das medicões de desempenho 
## Análise comparativa dos algoritmos 

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

## Conclusão sobre os resultados obtidos e sugestão de possíveis melhorias para cada algoritmo
## Autores

Frank Leite Lemos Costa, aluno do 6° período do curso de engenharia da computação.
Mateus Henrique Pereira, aluno do 8° período do curso de engenharia da computação.