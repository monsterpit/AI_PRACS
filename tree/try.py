import visualize_graph
v=["Node B"]
a=["Node A","Node B","Node C","Node D"]
visualize_graph.add_node(a,v)

e=[("Node A", "Node B"),("Node A", "Node C"),("Node C", "Node D"),("Node D", "Node A")]
visualize_graph.edges(e)


visualize_graph.save_graph("hello")
