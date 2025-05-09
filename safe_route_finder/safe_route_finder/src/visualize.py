import folium

def plot_route(path, map_center, save_path="safe_route.html"):
    m = folium.Map(location=map_center, zoom_start=14)
    for point in path:
        folium.CircleMarker(location=point, radius=3, color='blue').add_to(m)
    folium.PolyLine(locations=path, color='green').add_to(m)
    m.save(save_path)
