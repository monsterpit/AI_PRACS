vertexList =[0,1,2,3,4,5,6]
edgeList=[(0,1),(0,2),
          (1,0),(1,3),
          (2,0),(2,4),(2,5),
          (3,1),
          (4,2),(4,6),
          (5,2),
          (6,4)]

#visualizing
import matplotlib.pyplot as plt
import networkx as nx
import time
G=nx.Graph()
G.add_nodes_from(vertexList)
G.add_edges_from(edgeList)
nx.draw_spectral(G,with_labels =True)
plt.show()


#creating a list with empty [] equal to total number of vertices
adjacencyList =[[] for vertex in vertexList]

for edge in edgeList:
    #edge[0] is the position value of [] in adjacencyList
    #edge[1] is appended value i.e. neighbor
    adjacencyList[edge[0]].append(edge[1])

#####         for displaying neighbors    ###################
for i,v in enumerate(vertexList):
    print (v," --> {}".format(adjacencyList[i]))


######          DFS algorithm  ###################
def dfs(start):
  
  stack= [start]
  visitedVertex=[]
  #while stack has some value in it
  while stack:
    current =stack.pop()
    G.remove_node(current)
    for neighbor in adjacencyList[current]:
      #if value is not in visitedVertex then append stack
      if not neighbor in visitedVertex:
        stack.append(neighbor)


        ### visualizing ###
        c=['r']*len(vertexList)
        for i in visitedVertex:
          c[i]='b'
        G.add_nodes_from(vertexList)
        G.add_edges_from(edgeList)
        nx.draw_spectral(G,with_labels =True,node_color=c)
        plt.show()

      else:
        c=['r']*len(vertexList)
        for i in visitedVertex:
          c[i]='b'
        G.add_nodes_from(vertexList,node_color='g')
        G.add_edges_from(edgeList)
        nx.draw_spectral(G,with_labels =True,node_color=c)
        plt.show()
        ### visualizing ended ###
        
    visitedVertex.append(current)

  return visitedVertex

######################################################



#value= start node (vertex value)
value=int(input("\n enter a value for start node"))
print (dfs(value))






