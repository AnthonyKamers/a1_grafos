#Algorithms for bipartite graphs

import networkx as nx
import collections

class HopcroftKarp(object):
    INFINITY = -1

    def __init__(self, G):
        self.G = G

    def match(self):
        self.N1, self.N2 = self.partition()
        self.pair = {}
        self.dist = {}
        self.q = collections.deque()

        #init
        for v in self.G:
            self.pair[v] = None
            self.dist[v] = HopcroftKarp.INFINITY

        matching = 0

        while self.bfs():
            for v in self.N1:
                if self.pair[v] is None and self.dfs(v):
                    matching = matching + 1

        return matching

    def dfs(self, v):
        if v != None:
            for u in self.G.neighbors_iter(v):
                if self.dist[ self.pair[u] ] == self.dist[v] + 1 and self.dfs(self.pair[u]):
                    self.pair[u] = v
                    self.pair[v] = u

                    return True

            self.dist[v] = HopcroftKarp.INFINITY
            return False

        return True

    def bfs(self):
        for v in self.N1:
            if self.pair[v] == None:
                self.dist[v] = 0
                self.q.append(v)
            else:
                self.dist[v] = HopcroftKarp.INFINITY

        self.dist[None] = HopcroftKarp.INFINITY

        while len(self.q) > 0:
            v = self.q.popleft()
            if v != None:
                for u in self.G.neighbors_iter(v):
                    if self.dist[ self.pair[u] ] == HopcroftKarp.INFINITY:
                        self.dist[ self.pair[u] ] = self.dist[v] + 1
                        self.q.append(self.pair[u])

        return self.dist[None] != HopcroftKarp.INFINITY


    def partition(self):
        return nx.bipartite_sets(self.G)

if __name__ == "__main__":
    grafo = {'a': {1}, 'b': {1, 2}, 'c': {1, 2}, 'd': {2, 3, 4}, 'e': {3, 4}, 'f': {4, 5, 6}, 'g': {5, 6, 7}, 'h': {8}}
    HopcroftKarp(grafo).match()