import sys 

class DijkstraGraph(): 
    path_elim = []
    def __init__(self, vertices, graph): 
        self.V = vertices 
        self.graph = graph

    def printSolution(self, dist): 
        print ("Vertex tDistance from Source")
        for node in range(self.V): 
            print (node, "t", dist[node] )

    # function to find the vertex with minimum distance
    # value, from the set of vertices 
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 

        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        # Search not nearest vertex not in the 
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 

        return min_index 

    # Funtion that implements Dijkstra's  
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation and passing
    # the source and destination nodes
    def dijkstra(self, src, dest): 

        dist = [sys.maxsize] * self.V 
        dist[src-1] = 0
        path=[src-1]
        sptSet = [False] * self.V 

        for iters in range(self.V): 

            # Pick the minimum distance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
            

            # Put the minimum distance vertex in the 
            # shotest path tree 
            sptSet[u] = True

            # Update dist value of the adjacent vertices 
            # of the picked vertex only if the current 
            # distance is greater than new distance and 
            # the vertex in not in the shortest path tree 
            for v in range(self.V): 
                if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v] 
                    
                    if(v == dest-1):
                        if(path != [] and self.graph[u][path[-1]] == 0):
                            del path[-1]
                        path.append(u)
                        
        path.append(dest-1)
        DijkstraGraph.printPath(path, dist, dest)
        DijkstraGraph.path_elim = path
        DijkstraGraph.printRoutingTab(self.graph) 
        
    def eliminatePath(self, Matrix):
        for elems in range(len(DijkstraGraph.path_elim)-1):
            Matrix[DijkstraGraph.path_elim[elems]][DijkstraGraph.path_elim[elems+1]] = 0
            Matrix[DijkstraGraph.path_elim[elems+1]][DijkstraGraph.path_elim[elems]] = 0
        self.path_elim.clear()
        
    def printPath(path, dist, dest):
        print("Path : " , end = " " )
        for i in path:
            print(i+1 , end = " ")
        print("")
        print("Total Distance to Destination = ", dist[dest-1])
        
    def printRoutingTab(Matrix):
        print("N \t\t\t 2 3 4 5 6 7")
        routDist = Matrix[0][1:]
        
        n = 1
        indList = [1]
        print("{", *indList, "} \t\t\t", *routDist)
        while(n!=7):
            s, ind = DijkstraGraph.findsmallest(routDist, [x-2 for x in indList[1:]])
            indList.append(ind)
            nDist = Matrix[ind-1][1:]
            for i in range(len(Matrix)-1):
                if(routDist[i] == 0 and nDist[i]!=0):
                    routDist[i] = nDist[i]+s
                elif((nDist[i]+s) < routDist[i] and nDist[i]>0):
                    routDist[i] = nDist[i]+s
            
            if(n < 5):
                print("{", *indList, "} \t\t", *routDist)
            else:
                print("{", *indList, "} \t", *routDist)
            n = n+1
        print("\n")
               
                
    def findsmallest(routLine, exceptions):
        smallest = 100
        for i, elems in enumerate(routLine):
            if(i not in exceptions ):
                if(elems < smallest and elems > 0):
                    smallest = elems
                    ind = i+2
        
        return smallest, ind
                
        
        
def three_link_dsp(src, dest):
    Matrix = [[0,2,1,0,0,0,3],
              [2,0,5,5,9,0,0],
              [1,5,0,9,0,2,0],
              [0,5,9,0,2,2,6],
              [0,9,0,2,0,0,3],
              [0,0,2,2,0,0,3],
              [3,0,0,6,3,3,0]]
    Matrix_Dji = DijkstraGraph(len(Matrix[0]), Matrix)
    Matrix_Dji.dijkstra(src, dest)
    Matrix_Dji.eliminatePath(Matrix)
    Matrix_Dji.dijkstra(src, dest)
    Matrix_Dji.eliminatePath(Matrix)
    Matrix_Dji.dijkstra(src, dest)
    
    print("\nFinal Matrix after eliminating first two shortest paths: \n")
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            print(Matrix[i][j], " ", end= " ")
        print("")

# Call the function to find the three link disjoint shortest path,
# provide the source and destination nodes
three_link_dsp(1,4)



