from modules import Grafo

def greedyColoring(grafo):
    # lista de cores para cada vértice
    result = [-1] * grafo.qtdVertices()

    # atribui a primeira cor para o primeiro vértice
    result[0] = 0

    # lista para manter informação se vértice já foi atribuída cor ou não
    available_color = [False] * grafo.qtdVertices()

    for u in range(1, grafo.qtdVertices() + 1):
        # processa todos os vértices adjacentes e
        # coloca flag dizendo que está indisponível
        for vizinho in grafo.grafo[u-1].vizinhos():
            if u == vizinho:
                continue
            print(u, vizinho-1)
            if (result[vizinho-1] != -1):
                available_color[result[vizinho-1]] = True

        # encontra a primeira cor disponível
        color_now = 0
        while color_now < grafo.qtdVertices():
            if (available_color[color_now] == False):
                break
            
            color_now += 1

        # atribui a cor encontrada
        result[u-1] = color_now

        # resetta os valores para False para próxima iteração
        for vizinho in grafo.grafo[u-1].vizinhos():
            if (result[vizinho-1] != -1):
                available_color[result[vizinho-1]] = False
        
    # print the result
    for u in range(grafo.qtdVertices()):
        print(f'vértice {u} ---> cor: {result[u]}')


def main():
    grafo = Grafo.Grafo("testes/coloracao/aula.net")
    greedyColoring(grafo)


if __name__ == "__main__":
    main()