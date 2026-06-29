import folium
from streamlit_folium import st_folium


def display_map(graph, route, start, end):

    # Default map when no route is selected
    if start is None or end is None:

        m = folium.Map(
            location=[22.3072, 73.1812],   # Vadodara
            zoom_start=12
        )

        folium.Marker(
            location=[22.3072, 73.1812],
            popup="📍 Vadodara",
            tooltip="Default Location"
        ).add_to(m)

        st_folium(m, width=700, height=500)
        return

    # Create map
    m = folium.Map(
        location=start,
        zoom_start=14
    )

    # Start marker
    folium.Marker(
        location=start,
        popup="🚀 Start Location",
        tooltip="Start",
        icon=folium.Icon(
            color="green",
            icon="play",
            prefix="fa"
        )
    ).add_to(m)

    # Destination marker
    folium.Marker(
        location=end,
        popup="🏁 Destination",
        tooltip="Destination",
        icon=folium.Icon(
            color="red",
            icon="flag",
            prefix="fa"
        )
    ).add_to(m)

    # Route
    if route and len(route) > 1:

        route_coords = [
            (graph.nodes[node]["y"], graph.nodes[node]["x"])
            for node in route
        ]

        folium.PolyLine(
            route_coords,
            color="blue",
            weight=5,
            opacity=0.8
        ).add_to(m)

    st_folium(m, width=700, height=500)