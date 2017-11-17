import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math
from collections import OrderedDict

def ReadFileAndFillNodes(fileName):
    file=open(fileName,'r')
    row,column = file.readline().split()
    grid = [[0 for i in range(int(column))] for j in range(int(row))]
   # print(row+ "and " +  column)
    reverseDict = {"N": "S", "S": "N", "W": "E", "E": "W", "NE": "SW", "SW": "NE", "NW": "SE", "SE": "NW", "X": "X"}
    for i in range(int(row)):
        for j in range(int(column)):
            numRow,numColumn,color,circle,direction = file.readline().split()
            g.add_node((int(numRow),int(numColumn)),Color=color,Circle=circle,Direction=direction,Parent=None) #adding normal node
            g.add_node((int(numRow),int(numColumn),"R"),Color=color,Circle=circle,Direction=reverseDict[direction],Parent=None) #adding reverse node
    file.close()
    return int(row),int(column)

def FillEdges(row,column):
    counter = 0
    for i in range(1, row + 1):
        for j in range(1,column+1):
            if g.node[(i,j)]['Circle'] == "C" or (i == 1 and j == 1) or (i ==7 and j == 7): # connecting the circle nodes to its reverse copy
                g.add_edge((i,j), (i,j,"R"), color='r', direction="R")
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

def DisplayResult():
    dict = {}
    print("size of traversal: ", end=" ")
    print(len(list(nx.dfs_tree(g,(1,1)).nodes())))
    print(len(list(nx.dfs_tree(g, (1, 1)).edges())))
    print(len(list(nx.bfs_tree(g,(1,1)).nodes())))
    print(len(list(nx.bfs_tree(g, (1, 1)).edges())))
    print("size of nodes: ",end = " ")
    print(len(list(g.nodes())))
    for parent,child in nx.dfs_tree(g, (1, 1)).edges():
        dict.update({child:parent})
    DisplayRoute((7,7),dict)

def DisplayRoute(child,dict):
    if (child == (1,1)):
        traceBackList.append(str(child))
        return
    else:
        traceBackList.append(str(child))
        DisplayRoute(dict[child],dict)

#main
row = 0
column = 0
g = nx.DiGraph() #variable accessed globally
row,column=ReadFileAndFillNodes("input.txt")
FillEdges(row,column)
#CleanUp()


traceBackList = []
DisplayResult()
traceBackList.reverse()
print(traceBackList)
for x in range(len(traceBackList)):
    if "R" in traceBackList[x]:
        traceBackList[x] = traceBackList[x][0:5]+")"

print(OrderedDict((x,True) for x in traceBackList).keys())

#drawing plot
#nx.draw(g,with_labels=True)
#plt.show()



#sanity checks
t = nx.DiGraph()
t.add_node(1)
t.add_node(2)
t.add_edge(1,2)
print(list(t.neighbors(1)))
print(list(t.neighbors(2)))
nx.draw(t,with_labels=True)
plt.show()
