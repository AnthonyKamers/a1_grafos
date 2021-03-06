import sys
import itertools

from networkx.algorithms.approximation import *
from modules import Grafo1

def coloracao_minima(grafo):

    table_mark = make_table(grafo.grafo.number_of_nodes())
    table_mark[0]["value"] = 0

    for k, item in enumerate(table_mark):
        if k == 0:
            pass
        else:
            # fazer grafo' com elementos do item atual
            grafo_linha = grafo.grafo.subgraph(item["elements"])

            while True:
                max_set = maximum_independent_set(grafo_linha) # python Set
                max_set = [i for i in max_set] # transformar para lista

                subtraction_list = [i for i in grafo_linha.nodes if i not in max_set]
                subtraction_list.sort()

                find_table = list(filter(lambda i: i["elements"] == subtraction_list, table_mark))
                value_table = find_table[0]["value"]

                if (value_table + 1 < table_mark[k]["value"]):
                    table_mark[k]["value"] = int(value_table + 1)

                if subtraction_list != []:
                    grafo_linha = grafo_linha.subgraph(subtraction_list)
                else:
                    break

    print(table_mark[len(table_mark) - 1])

def make_table(n):
    table = list(itertools.product([False, True], repeat=n))

    table_mark = []
    for k, iterate in enumerate(table):
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