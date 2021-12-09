from exercicio1 import *
import sys

class Vertice:
    def __init__(self, id):
        self.id = id
        self.distancia = sys.float_info.max # representando infinito
        self.antecessor = None

class Aresta:
    def __init__(self, u, v, valor):
        self.u = u
        self.v = v
        self.valor = valor

def criarArestas(grafo, vertices):
    arestas = []

    for node in grafo.grafo:
        for item in node.edgesSaida:
            aresta = Aresta(vertices[int(node.id) - 1], vertices[int(item[0])], int(item[1]))
            arestas.append(aresta)

    return arestas

def criarVertices(grafo):
    return [Vertice(node.id) for node in grafo.grafo]

def getCaminho(vertices, vertice_now):
    caminho = [int(vertice_now.id)]
    
    if vertice_now.antecessor != None:
        while True:
            if vertice_now.antecessor == None:
                break

            next_vertice = vertices[int(vertice_now.antecessor) - 1]
            caminho.insert(0, int(next_vertice.id))
            vertice_now = vertices[int(next_vertice.id) - 1]
    
    return caminho

# caminho mínimo usando o algoritmo de Bellman-Ford
def caminho_minimo(grafo, vertice_origem):
    vertices = criarVertices(grafo)
    arestas = criarArestas(grafo, vertices)

    # settar distância do vertice de origem para 0
    vertices[vertice_origem - 1].distancia = 0

    # for do número de vértices
    for i in range(0, len(vertices)):
        
        # for das arestas (para cada aresta, executar)
        for aresta in arestas:
            # relaxamento
            if aresta.v.distancia > aresta.u.distancia + aresta.valor:
                aresta.v.distancia = aresta.u.distancia + aresta.valor
                aresta.v.antecessor = aresta.u.id
    
    # for do teste de ciclo negativo
    for aresta in arestas:
        if aresta.v.distancia > aresta.u.distancia + aresta.valor:
            print("Ciclo negativo! Erro")
            break
    
    # rodar cada vértice para printtar no formato do exercício
    for vertice in vertices:
        print(f'{int(vertice.id)}: ', end="")
        print(*getCaminho(vertices, vertice), sep=",", end="")
        print(f'; d={vertice.distancia}')

def main():
    grafo = Grafo("testes/caminho_minimo/fln_pequena.net")
    caminho_minimo(grafo, 1)


if __name__ == "__main__":
    main()