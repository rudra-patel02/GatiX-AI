import osmnx as ox


def geocode_location(place):
    """
    Convert place name into latitude and longitude.
    """

    try:
        location = ox.geocode(place)
        return location

    except Exception:
        return None