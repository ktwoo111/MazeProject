import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math
from collections import OrderedDict

def ReadFileAndFillNodes(fileName):
    file=open(fileName,'r')
    row,column = file.readline().split()
    reverseDict = {"N": "S", "S": "N", "W": "E", "E": "W", "NE": "SW", "SW": "NE", "NW": "SE", "SE": "NW", "X": "X"}
    for i in range(int(row)):
        for j in range(int(column)):
            numRow,numColumn,color,circle,direction = file.readline().split()
            g.add_node((int(numRow),int(numColumn)),Color=color,Circle=circle,Direction=direction,Parent=None) #adding normal node
            g.add_node((int(numRow),int(numColumn),"R"),Color=color,Circle=circle,Direction=reverseDict[direction],Parent=None) #adding reverse node
    file.close()
    return int(row),int(column)

def FillEdges(row,column):
    for i in range(1, row + 1):
        for j in range(1,column+1):
            if g.node[(i,j)]['Direction'] == "N":
                for before in range(1,i):
                    if g.node[(i,j)]['Color'] != g.node[(before,j)]['Color']:
                        if g.node[(before,j)]['Circle'] == "C":
                            g.add_edge((i,j),(before,j,"R"))
                        else:
                            g.add_edge((i,j),(before,j),color='b')
            elif g.node[(i, j)]['Direction'] == "S":
                for after in range(i+1,row+1):
                    if after <= row:
                        if g.node[(i,j)]['Color'] != g.node[(after,j)]['Color']:
                            if g.node[(after,j)]['Circle'] == "C":
                                g.add_edge((i, j), (after, j,"R"))
                            else:
                                g.add_edge((i,j),(after,j))
            elif g.node[(i, j)]['Direction'] == "W":
                for before in range(1,j):
                    if g.node[(i, j)]['Color'] != g.node[(i, before)]['Color']:
                        if g.node[(i,before)]['Circle'] == "C":
                            g.add_edge((i,j),(i,before,"R"))
                        else:
                            g.add_edge((i,j),(i,before))
            elif g.node[(i, j)]['Direction'] == "E":
                for after in range(j+1,column+1):
                    if after <= column:
                        if g.node[(i, j)]['Color'] != g.node[(i,after)]['Color']:
                            if g.node[(i,after)]['Circle'] == "C":
                                g.add_edge((i,j),(i,after,"R"))
                            else:
                                g.add_edge((i,j),(i,after))
            elif g.node[(i, j)]['Direction'] == "NW":
                beforeRow = i-1
                beforeColumn = j-1
                while beforeRow >= 1 and beforeColumn >= 1:
                        if g.node[(i, j)]['Color'] != g.node[(beforeRow,beforeColumn)]['Color']:
                            if g.node[(beforeRow,beforeColumn)]['Circle'] == "C":
                                g.add_edge((i, j), (beforeRow,beforeColumn, "R"))
                            else:
                                g.add_edge((i, j), (beforeRow,beforeColumn))
                        beforeRow-=1
                        beforeColumn-=1
            elif g.node[(i, j)]['Direction'] == "SE":
                afterRow = i+1
                afterColumn= j+1
                while afterRow <= row and afterColumn <= column:
                    if g.node[(i, j)]['Color'] != g.node[(afterRow, afterColumn)]['Color']:
                        if g.node[(afterRow,afterColumn)]['Circle'] == "C":
                            g.add_edge((i, j), (afterRow, afterColumn, "R"))
                        else:
                            g.add_edge((i, j), (afterRow, afterColumn))
                    afterRow+=1
                    afterColumn+=1
            elif g.node[(i, j)]['Direction'] == "SW":
                beforeRow = i+1
                beforeColumn = j-1
                while beforeRow <= row and beforeColumn >= 1:
                        if g.node[(i, j)]['Color'] != g.node[(beforeRow,beforeColumn)]['Color']:
                            if g.node[(beforeRow, beforeColumn)]['Circle'] == "C":
                                g.add_edge((i, j), (beforeRow, beforeColumn, "R"))
                            else:
                                g.add_edge((i, j), (beforeRow, beforeColumn))
                        beforeRow+=1
                        beforeColumn-=1
            elif g.node[(i, j)]['Direction'] == "NE":
                afterRow = i-1
                afterColumn = j+1
                while afterRow >= 1 and afterColumn <= column:
                        if g.node[(i, j)]['Color'] != g.node[(afterRow, afterColumn)]['Color']:
                            if g.node[(afterRow, afterColumn)]['Circle'] == "C":
                                g.add_edge((i, j), (afterRow, afterColumn, "R"))
                            else:
                                g.add_edge((i, j), (afterRow, afterColumn))
                        afterRow-=1
                        afterColumn+=1


            if g.node[(i,j,"R")]['Direction'] == "N":
                for before in range(1,i):
                    if g.node[(i,j,"R")]['Color'] != g.node[(before,j,"R")]['Color']:
                        if g.node[(before, j,"R")]['Circle'] == "C":
                            g.add_edge((i, j,"R"), (before, j))
                        else:
                            g.add_edge((i, j,"R"), (before, j,"R"), color='b')
            elif g.node[(i, j,"R")]['Direction'] == "S":
                for after in range(i+1,row+1):
                    if after <= row:
                        if g.node[(i,j,"R")]['Color'] != g.node[(after,j,"R")]['Color']:
                            if g.node[(after, j,"R")]['Circle'] == "C":
                                g.add_edge((i, j,"R"), (after, j))
                            else:
                                g.add_edge((i, j,"R"), (after, j,"R"))

            elif g.node[(i, j,"R")]['Direction'] == "W":
                for before in range(1,j):
                    if g.node[(i, j,"R")]['Color'] != g.node[(i, before,"R")]['Color']:
                        if g.node[(i,before,"R")]['Circle'] == "C":
                            g.add_edge((i,j,"R"),(i,before))
                        else:
                            g.add_edge((i,j,"R"),(i,before,"R"))
            elif g.node[(i, j,"R")]['Direction'] == "E":
                for after in range(j+1,column+1):
                    if after <= column:
                        if g.node[(i, j,"R")]['Color'] != g.node[(i,after,"R")]['Color']:
                            if g.node[(i,after,"R")]['Circle'] == "C":
                                g.add_edge((i,j,"R"),(i,after))
                            else:
                                g.add_edge((i,j,"R"),(i,after,"R"))
            elif g.node[(i, j,"R")]['Direction'] == "NW":
                beforeRow = i-1
                beforeColumn = j-1
                while beforeRow >= 1 and beforeColumn >= 1:
                        if g.node[(i, j,"R")]['Color'] != g.node[(beforeRow,beforeColumn,"R")]['Color']:
                            if g.node[(beforeRow,beforeColumn,"R")]['Circle'] == "C":
                                g.add_edge((i, j,"R"), (beforeRow,beforeColumn))
                            else:
                                g.add_edge((i, j,"R"), (beforeRow,beforeColumn,"R"))
                        beforeRow-=1
                        beforeColumn-=1
            elif g.node[(i, j,"R")]['Direction'] == "SE":
                afterRow = i+1
                afterColumn= j+1
                while afterRow <= row and afterColumn <= column:
                    if g.node[(i, j,"R")]['Color'] != g.node[(afterRow, afterColumn,"R")]['Color']:
                        if g.node[(afterRow, afterColumn,"R")]['Circle'] == "C":
                            g.add_edge((i, j,"R"), (afterRow, afterColumn))
                        else:
                            g.add_edge((i, j,"R"), (afterRow, afterColumn,"R"))
                    afterRow+=1
                    afterColumn+=1
            elif g.node[(i, j,"R")]['Direction'] == "SW":
                beforeRow = i+1
                beforeColumn = j-1
                while beforeRow <= row and beforeColumn >= 1:
                        if g.node[(i, j,"R")]['Color'] != g.node[(beforeRow,beforeColumn,"R")]['Color']:
                            if g.node[(beforeRow, beforeColumn,"R")]['Circle'] == "C":
                                g.add_edge((i, j,"R"), (beforeRow, beforeColumn))
                            else:
                                g.add_edge((i, j,"R"), (beforeRow, beforeColumn,"R"))
                        beforeRow+=1
                        beforeColumn-=1
            elif g.node[(i, j,"R")]['Direction'] == "NE":
                afterRow = i-1
                afterColumn = j+1
                while afterRow >= 1 and afterColumn <= column:
                        if g.node[(i, j,"R")]['Color'] != g.node[(afterRow, afterColumn,"R")]['Color']:
                            if g.node[(afterRow, afterColumn,"R")]['Circle'] == "C":
                                g.add_edge((i, j,"R"), (afterRow, afterColumn))
                            else:
                                g.add_edge((i, j,"R"), (afterRow, afterColumn,"R"))
                        afterRow-=1
                        afterColumn+=1


def CleanUp():
    nodeList = list(g.nodes())
    for x in nodeList:
        if len(list(nx.neighbors(g,x))) == 0 and x != (7,7):
            g.remove_node(x)

def DisplayResult():
    dict = {}
    for parent,child in nx.dfs_tree(g, (1, 1)).edges():
        dict.update({child:parent})

    DisplayRoute((7,7),dict)

    traceBackList.reverse()
    for x in range(len(traceBackList)):
        if "R" in traceBackList[x]:
            traceBackList[x] = traceBackList[x][0:5] + ")"
    print(traceBackList)

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
traceBackList = []
g = nx.DiGraph()

row,column=ReadFileAndFillNodes("input.txt")
FillEdges(row,column)
DisplayResult()

#drawing plot
nx.draw(g,with_labels=True)
plt.show()


