import osmnx as ox 
import matplotlib.pyplot as plt 

#descargar y construir el grafo vial de rio iv 
#osmnx descarga los datos automaticamente desde OpenStreetMap (o Geofabrik) solo de rio iv
G = ox.graph_from_place("Río Cuarto, Córdoba, Argentina", network_type="drive")

#dibujar el grafo y guardarlo en disco 
fig, ax = ox.plot_graph(G, show=False, close=False)
fig.savefig("grafo_rio_cuarto.png", dpi=300)
plt.close(fig)
print("✅ Grafo guardado como grafo_rio_cuarto.png")

# Número de nodos y aristas
print("Nodos:", G.number_of_nodes())
print("Aristas:", G.number_of_edges())

# Ver los primeros 5 nodos
print("Primeros 5 nodos: ",list(G.nodes(data=True))[:5])

# Ver las primeros 5 aristas (calles)
print("Primeras 5 aristas: ",list(G.edges(data=True))[:5])
