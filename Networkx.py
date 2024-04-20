import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
l=[1,2,3]
# G.add_nodes_from(l)
# G.add_edge(1,2)
# G.add_edge(1,3)
# G.add_edge(3,2)
G=nx.complete_graph(5)
nx.draw(G)
plt.show()