import networkx

class Vertice1:
    def __init__(self, id, rotulo):
        self.id = id
        self.rotulo = rotulo

class Grafo1:
    def __init__(self, arquivo):
        self.grafo = networkx.Graph()
        self.vertices = []
        self.ler(arquivo)

    def ler(self, arquivo):
        file = open(arquivo, 'r')

        first = True
        reading = False
        edges = False
        qtd = 0
        for line in file:
            line = line[0:-1] # retirar \n das linhas
            aux = line
            
            if edges:
                aux = aux.split(" ")
                aresta = (int(aux[0]) - 1, int(aux[1]) - 1)
                self.grafo.add_edges_from([aresta])
            
            if aux == "*edges" or aux == "*arcs":
                reading = False
                edges = True
            
            if reading:
                split = aux.split('"') if aux.find('"') > 0 else aux.split(' ')
                id = int(split[0])
                rotulo = split[1]
                self.vertices.append(Vertice1(id, rotulo))

            if first:
                qtd = int(aux.replace(aux[0:10], ""))
                reading = True
                first = False