from src.preprocess import load_crime_data
from src.clustering import cluster_crimes
from src.graph_builder import generate_grid, build_graph, remove_danger_zones
from src.router import find_safe_path
from src.visualize import plot_route
import pandas as pd

# Load and cluster
coords = load_crime_data('data/crime_data.csv')
kmeans, labels = cluster_crimes(coords)

# Danger zones: top 2 dense clusters
danger_clusters = list(pd.Series(labels).value_counts().head(2).index)
danger_centers = kmeans.cluster_centers_[danger_clusters]

# Build grid and graph
grid_nodes = generate_grid(37.75, 37.79, -122.45, -122.40)
G = build_graph(grid_nodes)
remove_danger_zones(G, danger_centers)

# Define points
start = (37.755, -122.445)
end = (37.775, -122.405)

# Find and visualize path
path = find_safe_path(G, start, end)
plot_route(path, map_center=start)
