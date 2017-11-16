import networkx as nx
import matplotlib.pyplot as plt
import numpy as np 
import math 

def ReadFileAndFillNodes(fileName):
    file=open(fileName,'r')
    row,column = file.readline().split()
    grid = [[0 for i in range(int(column))] for j in range(int(row))]
   # print(row+ "and " +  column)
    counter = 1
    for i in range(int(row)):
        for j in range(int(column)):
            numRow,numColumn,color,circle,direction = file.readline().split()
            g.add_node((int(numRow),int(numColumn)),Color=color,Circle=circle,Direction=direction,parent=-1,discovered = "WHITE", distance = math.inf)
            counter+=1
    file.close()
    return int(row),int(column)

def FillEdges(row,column):
    for i in range(1, row + 1):
        for j in range(1,column+1):
            if(g.node[(i,j)]['Direction'] == "N" or g.node[(i,j)]['Direction'] == "S"):
                for before in range(1,i):
                    if g.node[(i,j)]['Color'] != g.node[(before,j)]['Color']:
                        g.add_edge((i,j),(before,j),color='b',direction="N")
                for after in range(i+1,row+1):
                    if after <= row:
                        if g.node[(i,j)]['Color'] != g.node[(after,j)]['Color']:
                            g.add_edge((i,j),(after,j),color='b',direction="S")
            elif (g.node[(i, j)]['Direction'] == "W" or g.node[(i, j)]['Direction'] == "E"):
                for before in range(1,j):
                    if g.node[(i, j)]['Color'] != g.node[(i, before)]['Color']:
                        g.add_edge((i,j),(i,before),color='b',direction="W")
                for after in range(j+1,column+1):
                    if after <= column:
                        if g.node[(i, j)]['Color'] != g.node[(i,after)]['Color']:
                            g.add_edge((i,j),(i,after),direction="E")
            elif (g.node[(i, j)]['Direction'] == "NW" or g.node[(i, j)]['Direction'] == "SE"):
                beforeRow = i-1
                beforeColumn = j-1
                while beforeRow >= 1 and beforeColumn >= 1:
                        if g.node[(i, j)]['Color'] != g.node[(beforeRow,beforeColumn)]['Color']:
                            g.add_edge((i,j),(beforeRow,beforeColumn),color='b',direction="NW")
                        beforeRow-=1
                        beforeColumn-=1

                afterRow = i+1
                afterColumn= j+1
                while afterRow <= row and afterColumn <= column:
                    if g.node[(i, j)]['Color'] != g.node[(afterRow, afterColumn)]['Color']:
                        g.add_edge((i,j),(afterRow,afterColumn),color='b',direction= "SE")
                    afterRow+=1
                    afterColumn+=1
            elif (g.node[(i, j)]['Direction'] == "NE" or g.node[(i, j)]['Direction'] == "SW"):
                beforeRow = i+1
                beforeColumn = j-1
                while beforeRow <= row and beforeColumn >= 1:
                        if g.node[(i, j)]['Color'] != g.node[(beforeRow,beforeColumn)]['Color']:
                            g.add_edge((i, j), (beforeRow, beforeColumn), color='b', direction="SW")
                        beforeRow+=1
                        beforeColumn-=1

                afterRow = i-1
                afterColumn = j+1
                while afterRow >= 1 and afterColumn <= column:
                        if g.node[(i, j)]['Color'] != g.node[(afterRow, afterColumn)]['Color']:
                            g.add_edge((i, j), (afterRow, afterColumn), color='b', direction="NE")
                        afterRow-=1
                        afterColumn+=1




#main
row = 0
column = 0
g = nx.DiGraph() #variable accessed globally
row,column=ReadFileAndFillNodes("input.txt")
FillEdges(row,column)

#testing for N and S CHECKED!!!!!!!!!!!!!!
print(list(nx.neighbors(g,(5,5)))) #blue down arrow, should be 4 items
#testing for W and E CHECKED!!!!!!!!!!!
print(list(nx.neighbors(g,(4,3)))) #blue right arrow with circle, should be 4 itmes
# testing edges for SW and NE CHECKED!!!!!!!!!!!
print(list(nx.neighbors(g,(5,4)))) #red arrow pointing SW, should be 2 items
#testing NW and SE CHECKED!!!!!!!!
print(g.node[(6,3)]['Direction'])
print(g.node[(6,3)]['Color'])
print(list(nx.neighbors(g,(6,3)))) #blue arrow pointing NW, should be 3 items
#drawing plot
nx.draw(g,with_labels=True)
plt.show()
