import networkx as nx
import matplotlib.pyplot as plt

def ReadFileAndFillNodes(fileName,G):
    file=open(fileName,'r')
    row,column = file.readline().split()
    reverseDict = {"N": "S", "S": "N", "W": "E", "E": "W", "NE": "SW", "SW": "NE", "NW": "SE", "SE": "NW", "X": "X"}
    counter = 0
    for i in range(int(row)):
        for j in range(int(column)):
            numRow,numColumn,color,circle,direction = file.readline().split()
            G.add_node((int(numRow),int(numColumn)),Color=color,Circle=circle,Direction=direction,Parent=None) #adding normal node
            G.add_node((-int(numRow),-int(numColumn)),Color=color,Circle=circle,Direction=reverseDict[direction],Parent=None) #adding reverse node
            counter+=1
    file.close()
    return int(row),int(column)

def FillLinkingEdges(row,column,G):
    for i in range(1, row + 1):
        for j in range(1,column+1):
            if G.node[(i, j)]['Circle'] == "C" or (i == 1 and j == 1) or (i == 7 and j == 7):  # connecting the circle nodes to its reverse copy
                G.add_edge((i, j), (-i,-j))
                G.add_edge((-i,-j),(i,j))

def FillNormalEdges(row,column,G):
    for i in range(1, row + 1):
        for j in range(1,column+1):
            if G.node[(i,j)]['Direction'] == "N": # decrease in row value until hit 1
                counter = i-1
                while counter > 0:
                    if G.node[(i,j)]['Color'] != G.node[(counter,j)]['Color']:
                        if G.node[(counter,j)]['Circle'] == "C":   #<<<<<<<<<<<< THIS IS GONNA BE VERY IMPORTANT!!!!!!!!!!!
                            G.add_edge((i,j),(-counter,-j))
                        else:
                            G.add_edge((i,j),(counter,j))
                    counter-=1

            elif G.node[(i, j)]['Direction'] == "S": # increase in row value until hit max
                counter = i+1
                while counter < row+1:
                    if G.node[(i,j)]['Color'] != G.node[(counter,j)]['Color']:
                        G.add_edge((i,j),(counter,j))
                    counter+=1

            elif G.node[(i, j)]['Direction'] == "W": # decrease in column value until hit 1
                counter = j - 1
                while counter > 0:
                    if G.node[(i, j)]['Color'] != G.node[(i, counter)]['Color']:
                        G.add_edge((i,j),(i,counter))
                    counter-=1

            elif G.node[(i, j)]['Direction'] == "E": # increase in column value until hit max
                counter = j+1
                while counter < column+1:
                    if G.node[(i, j)]['Color'] != G.node[(i,counter)]['Color']:
                        G.add_edge((i,j),(i,counter))
                    counter+=1

            elif G.node[(i, j)]['Direction'] == "NW": #decrease in row value, decrease in column value
                rowCounter = i-1
                colCounter = j-1
                while rowCounter > 0 and colCounter > 0:
                        if G.node[(i, j)]['Color'] != G.node[(rowCounter,colCounter)]['Color']:
                            G.add_edge((i,j),(rowCounter,colCounter))
                        rowCounter-=1
                        colCounter-=1
            elif G.node[(i, j)]['Direction'] == "SE": # increase in row value, increase in col value
                rowCounter = i+1
                colCounter = j+1
                while rowCounter < row+1 and colCounter < column+1:
                        if G.node[(i, j)]['Color'] != G.node[(rowCounter,colCounter)]['Color']:
                            G.add_edge((i,j),(rowCounter,colCounter))
                        rowCounter+=1
                        colCounter+=1

            elif G.node[(i, j)]['Direction'] == "SW": #increase in row val, decrease in col value
                rowCounter = i+1
                colCounter = j-1
                while rowCounter < row+1 and colCounter > 0:
                        if G.node[(i, j)]['Color'] != G.node[(rowCounter,colCounter)]['Color']:
                            G.add_edge((i,j),(rowCounter,colCounter))
                        rowCounter+=1
                        colCounter-=1

            elif G.node[(i, j)]['Direction'] == "NE": # decrease in row val, increase in col value
                rowCounter = i-1
                colCounter = j+1
                while rowCounter > 0 and colCounter < column+1:
                        if G.node[(i, j)]['Color'] != G.node[(rowCounter,colCounter)]['Color']:
                            G.add_edge((i,j),(rowCounter,colCounter))
                        rowCounter-=1
                        colCounter+=1

def FillInverseEdges(row, column,G):
    for i in range(-row,0):
        for j in range(-column,0):
            if G.node[(i, j)]['Direction'] == "S":  # decrease in row value until hit 1
                counter = i - 1
                while counter > -(row+1):
                    if G.node[(i, j)]['Color'] != G.node[(counter, j)]['Color']:
                        G.add_edge((i, j), (counter, j))
                    counter -= 1

            elif G.node[(i, j)]['Direction'] == "N":  # increase in row value until hit max
                counter = i + 1
                while counter < 0:
                    if G.node[(i, j)]['Color'] != G.node[(counter, j)]['Color']:
                        G.add_edge((i, j), (counter, j))
                    counter += 1

            elif G.node[(i, j)]['Direction'] == "E":  # decrease in column value until hit 1
                counter = j - 1
                while counter > -(column+1):
                    if G.node[(i, j)]['Color'] != G.node[(i, counter)]['Color']:
                        G.add_edge((i, j), (i, counter))
                    counter -= 1

            elif G.node[(i, j)]['Direction'] == "W":  # increase in column value until hit max
                counter = j + 1
                while counter < 0:
                    if G.node[(i, j)]['Color'] != G.node[(i, counter)]['Color']:
                        G.add_edge((i, j), (i, counter))
                    counter += 1

            elif G.node[(i, j)]['Direction'] == "SE":  # decrease in row value, decrease in column value
                rowCounter = i - 1
                colCounter = j - 1
                while rowCounter > -(row+1) and colCounter > -(column+1):
                    if G.node[(i, j)]['Color'] != G.node[(rowCounter, colCounter)]['Color']:
                        G.add_edge((i, j), (rowCounter, colCounter))
                    rowCounter -= 1
                    colCounter -= 1
            elif G.node[(i, j)]['Direction'] == "NW":  # increase in row value, increase in col value
                rowCounter = i + 1
                colCounter = j + 1
                while rowCounter < 0 and colCounter < 0:
                    if G.node[(i, j)]['Color'] != G.node[(rowCounter, colCounter)]['Color']:
                        G.add_edge((i, j), (rowCounter, colCounter))
                    rowCounter += 1
                    colCounter += 1

            elif G.node[(i, j)]['Direction'] == "NE":  # increase in row val, decrease in col value
                rowCounter = i + 1
                colCounter = j - 1
                while rowCounter < 0 and colCounter > -(column+1):
                    if G.node[(i, j)]['Color'] != G.node[(rowCounter, colCounter)]['Color']:
                        G.add_edge((i, j), (rowCounter, colCounter))
                    rowCounter += 1
                    colCounter -= 1

            elif G.node[(i, j)]['Direction'] == "SW":  # decrease in row val, increase in col value
                rowCounter = i - 1
                colCounter = j + 1
                while rowCounter > -(row+1) and colCounter < 0:
                    if G.node[(i, j)]['Color'] != G.node[(rowCounter, colCounter)]['Color']:
                        G.add_edge((i, j), (rowCounter, colCounter))
                    rowCounter -= 1
                    colCounter += 1

def Testing():
    #testing East and West CHECKED
    print(list(G.neighbors((4, 6)))) # 0 items
    print(list(G.neighbors((-4, -6)))) #4 items
    #testing North and South
    print(list(G.neighbors((4, 5)))) #1 item
    print(list(G.neighbors((-4, -5)))) #2 item
    #testing NorthWest and SouthEast
    print(list(G.neighbors((6, 3)))) #2 items
    print(list(G.neighbors((-6, -3)))) #1 items
    #testing NorthEast and SouthWest
    print(list(G.neighbors((5, 4)))) #1 item
    print(list(G.neighbors((-5, -4)))) #1 item
    #testing special case: 3,3
    print(list(G.neighbors((3, 3))))  # 1 item
    print(list(G.neighbors((-3, -3))))  # 1 item

    # testing special case: 1,1
    print(list(G.neighbors((1, 1))))  # 1 item
    print(list(G.neighbors((-1, -1))))  # 1 item


def Result(G):
    dict={}
    #print(list(nx.dfs_tree(G, (1, 1)).edges()))
    for parent,child in nx.dfs_tree(G,(1,1)).edges():
        dict.update({child:parent})
    #print(dict)
    return dict


# finds shortest path between 2 nodes of a graph using BFS
def Route(node,G,dict):
    templist = []
    if(node == (1,1)):
        templist.append(node)
        return templist
    else:
        templist.append(node)
        Route(dict[node],G,dict)

#main
G = nx.DiGraph()
traceBackList = []
row,column = ReadFileAndFillNodes("input.txt",G)
FillNormalEdges(row,column,G)
FillInverseEdges(row,column,G)
#FillLinkingEdges(row,column,G)
#traceBackList = Route((7,7),G,Result(G))
#print(traceBackList)


Testing()
nx.draw(G,with_labels=True)
plt.show()
