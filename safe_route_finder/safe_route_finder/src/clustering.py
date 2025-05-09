import pandas as pd
from sklearn.cluster import KMeans

def cluster_crimes(coords, n_clusters=5):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(coords)
    return kmeans, labels
