import networkx as nx

def find_safe_path(G, start, end):
    return nx.shortest_path(G, source=start, target=end, weight='weight')
