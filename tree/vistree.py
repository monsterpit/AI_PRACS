import pydot
import matplotlib.pyplot as plt
from PIL import Image

graph = pydot.Dot(graph_type='digraph')
##node_a = pydot.Node("Node A", style="filled", fillcolor="red")
##node_b = pydot.Node("Node B", style="filled", fillcolor="green")
##node_c = pydot.Node("Node C", style="filled", fillcolor="#0000ff")
##node_d = pydot.Node("Node D", style="filled", fillcolor="#976856")
##
##graph.add_node(node_a)
##graph.add_node(node_b)
##graph.add_node(node_c)
##graph.add_node(node_d)
graph = pydot.Dot(graph_type='digraph')
graph.add_node(pydot.Node("Node A", style="filled", fillcolor="red"))
graph.add_node(pydot.Node("Node B", style="filled", fillcolor="green"))
graph.add_node( pydot.Node("Node C", style="filled", fillcolor="#0000ff"))
graph.add_node(pydot.Node("Node D", style="filled", fillcolor="#976856"))



graph.add_edge(pydot.Edge("Node A", "Node B"))
graph.add_edge(pydot.Edge("Node B", "Node C"))
graph.add_edge(pydot.Edge("Node C", "Node D"))

##graph.add_edge(pydot.Edge(node_a, node_b))
##graph.add_edge(pydot.Edge(node_b, node_c))
##graph.add_edge(pydot.Edge(node_c, node_d))
# but, let's make this last edge special, yes?
graph.add_edge(pydot.Edge("Node D", "Node A", label="and back we go again", labelfontcolor="#009933", fontsize="10.0", color="blue"))



# and we are done
graph.write_png('example2_graph.png')
img = Image.open('example2_graph.png')
plt.imshow(img)
plt.show()
