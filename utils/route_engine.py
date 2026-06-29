import networkx as nx
import osmnx as ox


def find_route(graph, start, destination):

    # Find nearest nodes
    start_node = ox.distance.nearest_nodes(
        graph,
        X=start[1],
        Y=start[0]
    )
   
    end_node = ox.distance.nearest_nodes(
        graph,
        X=destination[1],
        Y=destination[0]
    )
   


    # Shortest route
    from algorithms.dijkstra import dijkstra

    route, distance = dijkstra(
    graph,
    start_node,
    end_node
)

    return route, distance