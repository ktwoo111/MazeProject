import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math 
class Nodes():
    def __init__(self,counter,numRow,numColumn,color,circle,direction):
        self.counter = counter 
        self.numRow = int(numRow)
        self.numColumn=int(numColumn)
        self.color=color
        self.circle = circle
        self.direction = direction
        self.discovered = "WHITE"
        self.parent = -1
        self.distance= math.inf


def ReadFile(fileName, g):
    file=open(fileName,'r')
    row,column = file.readline().split()
    grid = [[0 for i in range(int(column))] for j in range(int(row))]
   # print(row+ "and " +  column)
    counter = 1
    for i in range(int(row)):
        for j in range(int(column)):
            numRow,numColumn,color,circle,direction = file.readline().split()
            
            #g.add_node(counter,Pos=(int(numRow),int(numColumn)),Coord=(int(numColumn),0-int(numRow)),Color=color,Circle=circle,Direction=direction)
            grid[i][j] = Nodes(counter,numRow,numColumn,color,circle,direction)
            counter+=1
    file.close()
    return grid

"""
def DetermineOptions(node,grid): #TODO: finish filling in and also consider
option where the direction becomes opposite with circle
    row = node.numRow
    column = node.numColumn
    
    if node.direction== "N":

    elif node.direction == "S":
        #stuff
    elif node.direction == "W":
        #stuff
    elif node.direction == "E":
        #stuff
    elif node.direction == "NW":

    elif node.direction == "NE":

    elif node.direction == "SW":
    
    elif node.direction == "SE":
    
"""

def ModifiedBFS(grid):
    queue = [grid[0][0]]
    while (len(queue) > 0):
        u = queue[0]
        neighbors = []



#main
g = nx.Graph()
grid=ReadFile("input.txt", g)
for i in range(7):
    for j in range(7):
        print(grid[i][j].circle,end=" ")
    print()
#coordList = nx.get_node_attributes(g,'Coord')
#counterList = nx.get_node_attributes(g,'counter')

#nx.draw(g,coordList,with_labels=True)

#plt.show()
