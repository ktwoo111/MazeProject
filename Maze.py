import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math

def ReadFileAndFillNodes(fileName):
    file=open(fileName,'r')
    row,column = file.readline().split()
    grid = [[0 for i in range(int(column))] for j in range(int(row))]
   # print(row+ "and " +  column)
    reverseDict = {"N": "S", "S": "N", "W": "E", "E": "W", "NE": "SW", "SW": "NE", "NW": "SE", "SE": "NW"}
    for i in range(int(row)):
        for j in range(int(column)):
            numRow,numColumn,color,circle,direction = file.readline().split()
            g.add_node((int(numRow),int(numColumn)),Color=color,Circle=circle,Direction=direction,Parent=None,Discovered = "WHITE",CircleCount=0) #adding normal node
            if(color != "X" and circle != "X" and direction != "X"):
                g.add_node((int(numRow),int(numColumn),"R"),Color=color,Circle=circle,Direction=reverseDict[direction],Parent=None,Discovered="WHITE",CircleCount=0) #adding reverse node
    file.close()
    return int(row),int(column)

def FillEdges(row,column):
    for i in range(1, row + 1):
        for j in range(1,column+1):
            if g.node[(i,j)]['Circle'] == "C": # connecting the circle nodes to its reverse copy
                g.add_edge((i, j), (i,j,"R"), color='r', direction="R")
                g.add_edge((i,j,"R"),(i,j),color='r', direction = "R")

            if g.node[(i,j)]['Direction'] == "N":
                for before in range(1,i):
                    if g.node[(i,j)]['Color'] != g.node[(before,j)]['Color']:
                        g.add_edge((i,j),(before,j),color='b',direction="N")
            elif g.node[(i, j)]['Direction'] == "S":
                for after in range(i+1,row+1):
                    if after <= row:
                        if g.node[(i,j)]['Color'] != g.node[(after,j)]['Color']:
                            g.add_edge((i,j),(after,j),color='b',direction="S")
            elif g.node[(i, j)]['Direction'] == "W":
                for before in range(1,j):
                    if g.node[(i, j)]['Color'] != g.node[(i, before)]['Color']:
                        g.add_edge((i,j),(i,before),color='b',direction="W")
            elif g.node[(i, j)]['Direction'] == "E":
                for after in range(j+1,column+1):
                    if after <= column:
                        if g.node[(i, j)]['Color'] != g.node[(i,after)]['Color']:
                            g.add_edge((i,j),(i,after),direction="E")
            elif g.node[(i, j)]['Direction'] == "NW":
                beforeRow = i-1
                beforeColumn = j-1
                while beforeRow >= 1 and beforeColumn >= 1:
                        if g.node[(i, j)]['Color'] != g.node[(beforeRow,beforeColumn)]['Color']:
                            g.add_edge((i,j),(beforeRow,beforeColumn),color='b',direction="NW")
                        beforeRow-=1
                        beforeColumn-=1
            elif g.node[(i, j)]['Direction'] == "SE":
                afterRow = i+1
                afterColumn= j+1
                while afterRow <= row and afterColumn <= column:
                    if g.node[(i, j)]['Color'] != g.node[(afterRow, afterColumn)]['Color']:
                        g.add_edge((i,j),(afterRow,afterColumn),color='b',direction= "SE")
                    afterRow+=1
                    afterColumn+=1
            elif g.node[(i, j)]['Direction'] == "SW":
                beforeRow = i+1
                beforeColumn = j-1
                while beforeRow <= row and beforeColumn >= 1:
                        if g.node[(i, j)]['Color'] != g.node[(beforeRow,beforeColumn)]['Color']:
                            g.add_edge((i, j), (beforeRow, beforeColumn), color='b', direction="SW")
                        beforeRow+=1
                        beforeColumn-=1
            elif g.node[(i, j)]['Direction'] == "NE":
                afterRow = i-1
                afterColumn = j+1
                while afterRow >= 1 and afterColumn <= column:
                        if g.node[(i, j)]['Color'] != g.node[(afterRow, afterColumn)]['Color']:
                            g.add_edge((i, j), (afterRow, afterColumn), color='b', direction="NE")
                        afterRow-=1
                        afterColumn+=1

            if i == 6 and j == 1:
                print("HI")
            if i !=7 or j != 7:
                if g.node[(i,j,"R")]['Direction'] == "N":
                    for before in range(1,i):
                        if g.node[(i,j,"R")]['Color'] != g.node[(before,j,"R")]['Color']:
                            g.add_edge((i,j,"R"),(before,j,"R"),color='b',direction="N")
                elif g.node[(i, j,"R")]['Direction'] == "S":
                    for after in range(i+1,row+1):
                        if after <= row:
                            if g.node[(i,j,"R")]['Color'] != g.node[(after,j,"R")]['Color']:
                                g.add_edge((i,j,"R"),(after,j,"R"),color='b',direction="S")
                elif g.node[(i, j,"R")]['Direction'] == "W":
                    for before in range(1,j):
                        if g.node[(i, j,"R")]['Color'] != g.node[(i, before,"R")]['Color']:
                            g.add_edge((i,j,"R"),(i,before,"R"),color='b',direction="W")
                elif g.node[(i, j,"R")]['Direction'] == "E":
                    for after in range(j+1,column+1):
                        if after <= column:
                            if g.node[(i, j,"R")]['Color'] != g.node[(i,after,"R")]['Color']:
                                g.add_edge((i,j,"R"),(i,after,"R"),direction="E")
                elif g.node[(i, j,"R")]['Direction'] == "NW":
                    beforeRow = i-1
                    beforeColumn = j-1
                    while beforeRow >= 1 and beforeColumn >= 1:
                            if g.node[(i, j,"R")]['Color'] != g.node[(beforeRow,beforeColumn,"R")]['Color']:
                                g.add_edge((i,j,"R"),(beforeRow,beforeColumn,"R"),color='b',direction="NW")
                            beforeRow-=1
                            beforeColumn-=1
                elif g.node[(i, j,"R")]['Direction'] == "SE":
                    afterRow = i+1
                    afterColumn= j+1
                    while afterRow <= row and afterColumn <= column:
                        if g.node[(i, j,"R")]['Color'] != g.node[(afterRow, afterColumn,"R")]['Color']:
                            g.add_edge((i,j,"R"),(afterRow,afterColumn,"R"),color='b',direction= "SE")
                        afterRow+=1
                        afterColumn+=1
                elif g.node[(i, j,"R")]['Direction'] == "SW":
                    beforeRow = i+1
                    beforeColumn = j-1
                    while beforeRow <= row and beforeColumn >= 1:
                            if g.node[(i, j,"R")]['Color'] != g.node[(beforeRow,beforeColumn,"R")]['Color']:
                                g.add_edge((i, j,"R"), (beforeRow, beforeColumn,"R"), color='b', direction="SW")
                            beforeRow+=1
                            beforeColumn-=1
                elif g.node[(i, j,"R")]['Direction'] == "NE":
                    afterRow = i-1
                    afterColumn = j+1
                    while afterRow >= 1 and afterColumn <= column:
                            if g.node[(i, j,"R")]['Color'] != g.node[(afterRow, afterColumn,"R")]['Color']:
                                g.add_edge((i, j,"R"), (afterRow, afterColumn,"R"), color='b', direction="NE")
                            afterRow-=1
                            afterColumn+=1

def CleanUp():
    nodeList = list(g.nodes())
    for x in nodeList:
        if len(list(nx.neighbors(g,x))) == 0 and x != (7,7):
            g.remove_node(x)







def DFS():
    reverse = False
    for point in g.nodes():
        if g.node[point]['Discovered'] == "WHITE":
            if g.node[point]['Circle'] == "C":
                g.node[point]['CircleCount'] += 1
            if point == (6, 7):
                print("HI")
            DFS_VISIT(point,ReverseCheck(point))

def DFS_VISIT(point,reverse):
    g.node[point]['Discovered'] = "GREY"
    for nodeCoord in nx.neighbors(g, point):
        if g.node[nodeCoord]['Discovered'] == "WHITE":
                if g[point][nodeCoord]['direction'] == g.node[point]['Direction']:
                    g.node[nodeCoord]['Parent'] = point
                    if g.node[nodeCoord]['Circle'] == "C":
                        g.node[nodeCoord]['CircleCount'] += 1
                    if nodeCoord == (6,7):
                        print("HI")
                    DFS_VISIT(nodeCoord,ReverseCheck(nodeCoord))
    g.node[point]['Discovered'] = "BLACK"


def BFS():
    queue = [(1,1)]
    g.node[(1,1)]['Discovered'] = "GREY"
    while queue:
        u = queue[0]
        reverse = False
        if(g.node[u]['Circle'] == "C"):
            #g.node[u]['CircleCount']+=1 #new
            reverse = True
        #reverse = ReverseCheck(u) #new
        for nodeCoord in nx.neighbors(g, u):
            if g.node[nodeCoord]['Discovered'] == "WHITE":
               if(reverse == False):
                    if g[u][nodeCoord]['direction'] == g.node[u]['Direction']:
                        g.node[nodeCoord]['Discovered'] = "GRAY"
                        g.node[nodeCoord]['Parent'] = u
                        queue.append(nodeCoord)
               else:
                    if g[u][nodeCoord]['direction'] != g.node[u]['Direction']:
                        g.node[nodeCoord]['Discovered'] = "GRAY"
                        g.node[nodeCoord]['Parent'] = u
                        #g.node[nodeCoord]['CircleCount'] += 1 #new
                        queue.append(nodeCoord)
        queue.pop(0)
        g.node[u]['Discovered'] = "BLACK"

def exBFS():
    queue = [(1,1)]
    g.node[(1,1)]['Discovered'] = "GREY"
    while queue:
        u = queue[0]
        if(g.node[u]['Circle'] == "C"):
            g.node[u]['CircleCount']+=1 #new
        reverse = ReverseCheck(u) #new
        for nodeCoord in nx.neighbors(g, u):
            if g.node[nodeCoord]['Discovered'] == "WHITE":
                    if g[u][nodeCoord]['direction'] == g.node[u]['Direction']:
                        g.node[nodeCoord]['Discovered'] = "GRAY"
                        g.node[nodeCoord]['Parent'] = u
                        if reverse == True:
                            g.node[nodeCoord]['CircleCount'] += 1 #new
                        queue.append(nodeCoord)
        queue.pop(0)
        g.node[u]['Discovered'] = "BLACK"

def ReverseCheck(nodeCoord):
    counter = g.node[nodeCoord]['CircleCount']
    reverseDict = {"N": "S", "S": "N", "W": "E", "E": "W", "NE": "SW", "SW": "NE", "NW": "SE", "SE": "NW"}
    if counter == 0:
        return False
    elif counter == 1:
        g.node[nodeCoord]['Direction'] = reverseDict[g.node[nodeCoord]['Direction']]
        return True
    elif counter%2 == 0:
        return False
    elif counter%2 != 0:
        g.node[nodeCoord]['Direction'] = reverseDict[g.node[nodeCoord]['Direction']]
        return True


def TraceBack(nodeCoord):
    if nodeCoord == (1,1):
        traceBackList.append(nodeCoord)
        return
    if nodeCoord == None:
        print("FAILED")
        return
    else:
        traceBackList.append(nodeCoord)
        TraceBack(g.node[nodeCoord]['Parent'])


def Testing():
    print("The graph is connected")
    for x in g.nodes():
        print(x, end= " ")
        print(list(nx.neighbors(g,x)))

    for x in nx.isolates(g):
        print(" isolated folks", end= " ")
        print(x)

    for x in g.nodes():
        print(x,end= " ")
        print(g.node[x]['Parent'],end=" ")
        print(g.node[x]['Discovered'])

#main
row = 0
column = 0
g = nx.DiGraph() #variable accessed globally
row,column=ReadFileAndFillNodes("input.txt")
FillEdges(row,column)
CleanUp()
print(nx.dfs_tree(g,(1,1)).edges())

#DFS()
#BFS()

#Testing()
#traceBackList = []
#TraceBack((row,column))
#traceBackList.reverse()
#print(traceBackList)

#drawing plot
nx.draw(g,with_labels=True)
plt.show()
