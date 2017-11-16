import networkx as nx
import matplotlib.pyplot as plt

g=nx.DiGraph()

#name of node then position
g.add_node("(1,1)", message="HELLO")
g.add_node("(2,1)", message= "HI")
g.add_node("(3,1)", message="WHAT")
g.add_node("(4,1)", message="HI2")

g.add_edge("(1,1)","(2,1)",color='b')
g.add_edge("(2,1)","(3,1)",color='r')
g.add_edge("(2,1)","(4,1)",color='r')

#get position of all the nodes
#pos = nx.get_node_attributes(g,'pos')
#circle = nx.get_node_attributes(g,'circle')


#print(circle)
#g.add_edge(2,5)
#g.add_edge(4,1)

#g.add_edges_from([ (2,5),(1,3)])

#print(nx.info(g))
print(list(nx.neighbors(g,"(2,1)")))
print(g.node["(1,1)"]['message'])
g.node["(1,1)"]['message'] = "CHANGED" #accessing particular node and changing value
print(g.node["(1,1)"]['message'])
print(g["(1,1)"]["(2,1)"]['color'])
g["(1,1)"]["(2,1)"]['color'] = 'g' #accessing particular edge and changing value
edges = g.edges()
colors = [g[u][v]['color'] for u,v in edges]
nx.draw(g,with_labels=True,edge_color=colors)

plt.show()


