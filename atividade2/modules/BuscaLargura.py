from exercicio1 import *

# classe auxiliar para manter organizado
class NodeTree:
    def __init__(self, node):
        self.node = node
        self.nivel = 0
        self.pai = None

def busca_em_largura(grafo, n):
    # iniciar variaveis necessárias para realizar busca
    arvore = []
    passados = []
    fila = []
    maxNivel = 0

    nodeInit = NodeTree(grafo.grafo[n-1])
    fila.append(nodeInit)

    # while da busca em largura
    while len(fila) != 0:
        u = fila.pop(0)

        arvore.append(u)
        passados.append(u.node.id)

        for vizinho in u.node.edgesSaida:
            if vizinho[0] not in passados:
                passados.append(vizinho[0])
                nodeTree = NodeTree(grafo.grafo[vizinho[0]])
                nodeTree.nivel = u.nivel + 1
                nodeTree.pai = u
                fila.append(nodeTree)
                maxNivel = u.nivel + 1

    # printtar no formato do exercício
    for i in range(0, maxNivel+1):
        line = f'{i}: '
        for item in arvore:
            if item.nivel == i:
                aux = item.node.id[:-1]
                line += aux + ","
        print(line[:-1])


def main():
    arquivo = "testes/arvore_geradora_minima/agm_tiny.net"
    grafo = Grafo(arquivo)
    n = 1
    busca_em_largura(grafo, n)

if __name__ == "__main__":
    main()