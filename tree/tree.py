import networkx as nx
import matplotlib.pyplot as plt

g=nx.DiGraph()
g.add_edges_from([(1,2), (1,3), (1,4), (2,5), (2,6), (2,7), (3,8), (3,9),
                  (4,10), (5,11), (5,12), (6,13)])
p=nx.drawing.nx_pydot.to_pydot(g)
p.write_png('example.png')


##G = nx.complete_graph(4)
##pos = nx.nx_pydot.graphviz_layout(G)
##pos = nx.nx_pydot.graphviz_layout(G, prog='dot')
