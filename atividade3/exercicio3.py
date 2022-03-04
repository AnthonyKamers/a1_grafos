import sys
import itertools

from modules import Grafo1

def coloracao_minima(grafo):
    table_mark = make_table(grafo.grafo.number_of_nodes())
    table_mark[0]["value"] = 0

    for item in table_mark:
        if item["elements"] == []:
            pass
        else:
            # fazer grafo' com elementos do item atual
            grafo_linha = make_grafo(grafo, item["elements"])

def make_grafo(grafo, elements):
    print(elements)
    print(grafo.grafo.subgraph(elements).edges())
    print('')

def make_table(n):
    table = list(itertools.product([False, True], repeat=n))
    lista = list(table[1])
    lista.reverse()

    table_mark = []
    for iterate in table:
        elements = [k for k,v in enumerate(iterate) if v]

        dict1 = {
            "key": iterate,
            "elements": elements,
            "value": sys.float_info.max
        }
        table_mark.append(dict1)

    return table_mark

def main():
    grafo = Grafo1.Grafo1("testes/coloracao/aula.net")
    coloracao_minima(grafo)
    # edges = list(grafo.grafo.edges)

if __name__ == "__main__":
    main()