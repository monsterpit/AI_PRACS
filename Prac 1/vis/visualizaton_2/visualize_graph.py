import pydot
import matplotlib.pyplot as plt
from PIL import Image

graph = pydot.Dot(graph_type='digraph')

def add_node(nodes,visited=[]):
    for node in nodes:
        if node in visited:
            graph.add_node(pydot.Node(node, style="filled", fillcolor="#00e6e6"))
        else:
            graph.add_node(pydot.Node(node, style="filled", fillcolor="red"))

        
        

        
def edges (edges):
    for edge in edges:
        graph.add_edge(pydot.Edge(edge[0], edge[1]))      
 
def save_graph(name):
# and we are done
    graph.write_png('vis\{}.png'.format(name))
    img = Image.open('vis\{}.png'.format(name))
    plt.imshow(img)
    plt.show()
