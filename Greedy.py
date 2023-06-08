class Graph():
    
    def __init__(self, vertices):
        self.V = vertices
        self.adjacent = [[0 for columns in range (self.V)] for rows in range (self.V)]
        self.bird_lane = [[0 for columns in range (self.V)] for rows in range (self.V)]
    
    def Min_open_list(self, open_list, close_list, path, destination, bird_lane):
        min = bird_lane[open_list[0]][destination]
        min_vertice = open_list[0]
        for i in open_list:
            if min > bird_lane[i][destination]:
                min = bird_lane[i][destination]
                min_vertice = i
        open_list.remove(min_vertice)
        close_list.append(min_vertice)
        path.append(min_vertice)
        return min_vertice
    
    def print(self, path, source, destination):
        print("Greedy from: " + str(source) + " to " + str(destination))
        for i in range (len(path)):
            print("Step " + str(i) + ": " + str(path[i]))
        
    def Greedy(self, source, destination):
        self.open_list = []
        self.close_list = []
        self.path = []
        
        self.open_list.append(source)
        
        while True:
            
            if len(self.open_list) == 0:
                print("Failure!")
                return
            
            u = self.Min_open_list(self.open_list,self.close_list,self.path,destination,self.bird_lane)
            
            print("----------------------------")
            print("Path:")
            print(self.path)
            print("")
            
            for i in range (self.V):
                if self.adjacent[u][i] > 0 and self.open_list.count(i) == 0 and self.close_list.count(i) == 0:
                    self.open_list.append(i)
                    if i == destination:
                        self.open_list.clear()
                        self.close_list.clear()
                        self.path.append(i)
                        self.print(self.path,source,destination)
                        return
           
            
            
#Test_case
g = Graph(6)
g.adjacent = [[0,6,0,3,0,0],
              [6,0,2,0,0,0],
              [0,2,0,7,1,2],
              [3,0,7,0,0,8],
              [0,0,1,0,0,3],
              [0,0,2,8,3,0]]

g.bird_lane = [[0,6,7,3,8,9],
               [6,0,2,5,3,3],
               [7,2,0,7,1,2],
               [3,5,7,0,8,8],
               [8,3,1,8,0,3],
               [9,3,2,8,3,0]]           
g.Greedy(0,5)