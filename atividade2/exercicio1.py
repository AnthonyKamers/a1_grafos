import sys
from modules import Grafo

class VerticeDFS:
    def __init__(self, vertice):
        self.vertice = vertice
        self.hasPassed = False
        self.tempo = sys.float_info.max
        self.final = sys.float_info.max
        self.antecessor = None


def componentes_fort_conexas(grafo):
    vertices = DFS(grafo)
    vertices.sort(key = lambda x: x.tempo, reverse=True) # saber ordem do tempo final, para passar na próxima etapa

    vertices_final = DFS(grafo, vertices)
    vertices_escolhidos = filter(lambda x: x.antecessor != None, vertices_final)
    
    for item in vertices_escolhidos:
        print(item.vertice.id)


def DFS(grafo, vertices1=None):
    vertices = criar_verticesDFS(grafo)

    tempo = 0 # tempo de início
    for i in range(0, len(vertices)):
        id_now = i if not vertices1 else int(vertices1[i].vertice.id) - 1
        if vertices[id_now].hasPassed == False:
            vertices = DFS_visit(vertices[id_now], vertices, tempo, entrada=False if not vertices1 else True)
    
    return vertices

def DFS_visit(verticeOrigem, vertices, tempo, entrada=False):
    indexVerticeOrigem = int(verticeOrigem.vertice.id) - 1

    vertices[indexVerticeOrigem].hasPassed = True
    tempo += 1
    vertices[indexVerticeOrigem].tempo = tempo

    vizinhos = verticeOrigem.vertice.vizinhosSaida() if not entrada else verticeOrigem.vertice.vizinhosEntrada()
    
    for id in vizinhos:
        if vertices[id - 1].hasPassed == False:
            vertices[id - 1].antecessor = verticeOrigem
            vertices = DFS_visit(vertices[id - 1], vertices, tempo)
    
    tempo += 1
    vertices[indexVerticeOrigem].final = tempo

    return vertices

def criar_verticesDFS(grafo):
    return [VerticeDFS(vertice) for vertice in grafo.grafo]

def main():
    grafo = Grafo.Grafo("testes/dirigidos/teste.net")
    componentes_fort_conexas(grafo)

if __name__ == "__main__":
    main()