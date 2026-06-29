import osmnx as ox
import streamlit as st

CITY = "Vadodara, Gujarat, India"

@st.cache_resource(show_spinner="Loading road network...")
def load_graph(city=CITY):
    graph = ox.graph_from_place(
        city,
        network_type="drive",
        simplify=True
    )

    return graph