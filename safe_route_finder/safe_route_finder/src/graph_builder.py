import numpy as np
import networkx as nx
from geopy.distance import geodesic

def generate_grid(min_lat, max_lat, min_lon, max_lon, step=0.005):
    nodes = []
    for lat in np.arange(min_lat, max_lat, step):
        for lon in np.arange(min_lon, max_lon, step):
            nodes.append((lat, lon))
    return nodes

def build_graph(nodes):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node)
        for dx in [-0.005, 0.005]:
            for dy in [-0.005, 0.005]:
                neighbor = (round(node[0] + dx, 6), round(node[1] + dy, 6))
                if neighbor in nodes:
                    G.add_edge(node, neighbor, weight=geodesic(node, neighbor).meters)
    return G

def remove_danger_zones(G, danger_centers, radius=0.5):
    for node in list(G.nodes):
        for center in danger_centers:
            if geodesic(node, center).km < radius:
                G.remove_node(node)
                break
