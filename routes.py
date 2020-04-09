import networkx as nx

map = nx.Graph()
map.add_nodes_from(range(1,21))
map.add_edges_from([(1,2),(2,3),(2,4),(3,6),(3,12),(6,11),(6,9),(9,14),(9,13),(14,20),(13,10),(20,19),(18,19),(17,18),(4,5),(5,7),(7,8),(8,10),(10,16),(10,15),(15,16),(15,17)])

print(map.nodes)
print(map.edges)
