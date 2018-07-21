vertexList =[0,1,2,3,4,5,6]
edgeList=[(0,1),(0,2),
          (1,0),(1,3),
          (2,0),(2,4),(2,5),
          (3,1),
          (4,2),(4,6),
          (5,2),
          (6,4)]


#creating a list with empty [] equal to total number of vertices
adjacencyList =[[] for vertex in vertexList]

for edge in edgeList:
    #edge[0] is the position value of [] in adjacencyList
    #edge[1] is appended value i.e. neighbor
    adjacencyList[edge[0]].append(edge[1])

#####         for displaying neighbors    ###################
for i,v in enumerate(vertexList):
    print (v," --> {}".format(adjacencyList[i]))

######          BFS algorithm  ###################
def bfs(start):
  queue= [start]
  visitedVertex=[]
  #while stack has some value in it
  while queue:
    #poping the last element
    current =queue.pop()
    for neighbor in adjacencyList[current]:
      #if value is not in visitedVertex then append stack
      if not neighbor in visitedVertex:
        # inserting at first position
        queue.insert(0,neighbor)
    visitedVertex.append(current)
  return visitedVertex

######################################################



#value= start node (vertex value)
value=int(input("\n enter a value for start node"))
print (bfs(value))






