#!/usr/bin/env python

try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

def dijkstra(self, src):

        dist = [sys.maxint] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


G=nx.Graph()


while True:
    a = input()
    if a == '0':
        break
    a = a.split(' ')
    G.add_edge(a[0],a[1],weight=float(a[2]))




# G.add_edge('a','b',weight=0.6)
# G.add_edge('b','c',weight=0.2)
# G.add_edge('c','d',weight=0.1)
# G.add_edge('c','e',weight=0.7)
# G.add_edge('e','f',weight=0.9)

# path returns shortest list of edges from 'a' to 'd'
z = input().split()
try:
    path = nx.shortest_path(G, z[0], z[1], weight=True)
except nx.NetworkXNoPath:
    raise Exception("Invalid input. Cant find path")


# mark usual path as us_nodes
# mark shortest path as spath
us_nodes=[(u,v) for (u,v,d) in G.edges(data=True)]
spath = [(u, v) for (u, v, d) in G.edges (data=True) if u in path and v in path]

pos=nx.spring_layout(G) # positions for all nodes

# draw nodes
nx.draw_networkx_nodes(G,pos,node_size=700)

nx.draw_networkx_edges(G, pos, edgelist=spath,
                    width=6, edge_color='r')
nx.draw_networkx_edges(G,pos,edgelist=us_nodes,
                    width=6,alpha=0.5,edge_color='b',style='dashed')


# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='Ubuntu')

plt.axis('off')
plt.savefig("weighted_graph.png") # save as png
plt.show() # display

# sample of input
# a b 0.6
# a c 0.2
# b e 0.1
# b f 0.7
# f g 0.9
# g k 0.5
# b d 0.3
# d k 0.5
# a e 0.6
# a d 0.7
# 0
# a g
