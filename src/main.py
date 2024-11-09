# Representação do labirinto como um grafo
grafo_labirinto = {
    (4, 0): [(4, 1), (3, 0)],          # U 
    (4, 1): [(4, 0), (3, 1), (4 ,2)],  # V 
    (4, 2): [(4, 1), (4, 3)],          # X 
    (4, 3): [(4, 2), (4, 4)],          # Y 
    (4, 4): [(3, 4), (4, 3)],          # Z 

    (3, 0): [(4, 0), (2, 0)],           # P 
    (3, 1): [(4, 1), (2, 1)],           # Q 
    (3, 2): [(3, 3), (2, 2)],           # R 
    (3, 3): [(3, 2), (3, 4)],           # S 
    (3, 4): [(4, 4), (3, 3)],           # T 

    (2, 0): [(3, 0)],                   # K 
    (2, 1): [(3, 1), (2, 2)],           # L 
    (2, 2): [(2, 1), (3, 2), (2, 3)],   # M 
    (2, 3): [(1, 3), (2, 2), (2, 4)],   # N 
    (2, 4): [(2, 3)],                   # O 

    (1, 0): [(0, 0), (1, 1)],           # F 
    (1, 1): [(1, 0), (1, 2)],           # G 
    (1, 2): [(0, 2), (1, 1), (1, 3)],   # H 
    (1, 3): [(2, 3), (1, 2)],           # I 
    (1, 4): [(0, 4)],                   # J 

    (0, 0): [(1, 0), (0, 1)],           # A 
    (0, 1): [(0, 0)],                   # B 
    (0, 2): [(1, 2), (0, 3)],           # C 
    (0, 3): [(0, 2), (0, 4)],           # D 
    (0, 4): [(1, 4), (0, 3)]            # E (fim) 
}

inicio = (4, 0)  # posição inicial no labirinto
fim = (0, 4)     # objetivo final

# daqui em diante temos a implementação dos algoritmos

def distanceCalculation(node, fim):
    return float(float(abs(node[0] - fim[0])) + float(abs(node[1] - fim[1])))


def a_star(grafo, inicio, fim):
    # inicializa as estruturas de dados
    abertos = [inicio]
    fechados = []
    g = {inicio: 0}
    f = {inicio: distanceCalculation(inicio, fim)}
    antecessores = {}

    # enquanto houverem nós abertos
    while abertos:
        # seleciona o nó com menor valor de f → então este vetor abertos é reordenado
        atual = abertos[0]
        for node in abertos:
            if f[node] < f[atual]:
                atual = node

        # se o nó atual é o nó objetivo, então terminamos
        if atual == fim:
            caminho = []
            while atual:
                caminho.insert(0, atual)
                atual = antecessores.get(atual)
                # print("caminho: ", caminho)
                # print("atual: ", atual)
            return caminho

        # remove o nó atual da lista de abertos e o coloca na lista de fechados
        abertos.remove(atual)
        fechados.append(atual)

        # para cada vizinho do nó atual
        for vizinho in grafo[atual]:
            # se o vizinho já está na lista de fechados, então ignora
            if vizinho in fechados:
                continue

            # calcula o custo para chegar no vizinho
            custo = float(g[atual]) + 1

            # se o vizinho não está na lista de abertos, então o adiciona
            if vizinho not in abertos:
                abertos.append(vizinho)
            # se o custo para chegar no vizinho é maior do que o custo atual, então ignora
            elif custo >= g[vizinho]:
                continue

            # atualiza os custos e o antecessor do vizinho
            antecessores[vizinho] = atual
            g[vizinho] = custo
            f[vizinho] = g[vizinho] + distanceCalculation(vizinho, fim)
            
            print("vizinho: ",vizinho, "atual: ", atual, "valor do vetor g:", g[vizinho],"valor do vetor f:", f[vizinho])

    # se não encontrou o caminho, então retorna uma lista vazia
    return []
    
print(a_star(grafo_labirinto, inicio, fim))

