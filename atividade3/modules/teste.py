import networkx
import matplotlib.pyplot as plt

from networkx.algorithms.approximation import *

def main():
    w = 4
    h = 3
    d = 70
    plt.figure(figsize=(w,h), dpi=d)

    G = networkx.Graph()
    G.add_edges_from([
        (0, 1), (0, 2), (1, 2), (2, 3),
        (3, 5), (3, 4), (4, 5), (5, 6)
    ])
    # G.add_edges_from([
    #     (0, 1), (1, 2)
    # ])

    labels=[0, 1, 2, 3, 4, 5, 6]
    # labels=[0, 1, 2]
    networkx.draw_networkx(G, with_labels=labels)
    
    plt.axis("off")
    plt.savefig("out.png")

    max_set = maximum_independent_set(G)
    print(max_set)
    # for i in max_set:
    #     print(i)

if __name__ == "__main__":
    main()