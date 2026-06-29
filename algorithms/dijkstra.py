import heapq


def dijkstra(graph, start_node, end_node):
    """
    Custom Dijkstra Algorithm

    Parameters
    ----------
    graph : networkx.MultiDiGraph
    start_node : int
    end_node : int

    Returns
    -------
    route : list
        List of node IDs representing shortest path

    total_distance : float
        Distance in meters
    """

    # Distance from start to every node
    distances = {
        node: float("inf")
        for node in graph.nodes
    }

    distances[start_node] = 0

    # Store previous node
    previous = {
        node: None
        for node in graph.nodes
    }

    # Priority Queue
    priority_queue = [(0, start_node)]

    # Visited nodes
    visited = set()

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        # Stop when destination reached
        if current_node == end_node:
            break

        # Explore neighbours
        for neighbor in graph.neighbors(current_node):

            edge_data = graph.get_edge_data(current_node, neighbor)

            if edge_data is None:
                continue

            # Smallest edge if multiple roads exist
            weight = min(
    edge.get("length", float("inf"))
    for edge in edge_data.values()
)

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    # -----------------------------
    # Reconstruct Route
    # -----------------------------

    route = []

    node = end_node

    while node is not None:
        route.append(node)
        node = previous[node]

    route.reverse()

    if not route or route[0] != start_node:
        raise Exception("No route found.")

    return route, distances[end_node]