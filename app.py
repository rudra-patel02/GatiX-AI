from visualization.map_view import display_map
import streamlit as st
from utils.graph_loader import load_graph
from utils.geocoder import geocode_location
from utils.route_engine import find_route
from datetime import datetime, timedelta

st.set_page_config(
    page_title="GatiX AI Pro",
    page_icon="🚀",
    layout="wide"
)
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.markdown("""
<style>

/* Main App */
.stApp{
    background: linear-gradient(135deg,#071B34,#0B2A4A,#123E6B);
    color:white;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#081A33;
    border-right:1px solid #1f4e79;
}

/* Headings */
h1,h2,h3{
    color:white;
}

</style>
""", unsafe_allow_html=True)
# ---------------- Sidebar ----------------
with st.sidebar:
    st.markdown("""
<h1 style='color:white;font-size:42px;font-weight:bold;'>
🚀 GatiX AI Pro
</h1>
""", unsafe_allow_html=True)
    st.markdown("---")

    st.subheader("About")
    st.info("""
    🚀 AI-Powered Route Optimization

    📍 Real Road Network

    🗺️ Interactive Map

    📏 Distance & ETA
""")
    st.subheader("Algorithms")
    st.write("✅ Dijkstra")
    st.write("🚧 A* Search (Coming Soon)")
    st.write("🚧 Genetic Algorithm (Coming Soon)")
    st.subheader("Algorithm")

algorithm = st.selectbox(
    "Choose Algorithm",
    ["Dijkstra"]
)
st.markdown("---")

st.info("Version 1.0")

st.title("🚀 GatiX AI Pro")

st.markdown("---")

st.caption("Version 1.0")
st.caption("Developed by Rudra")
# Load Graph
G = load_graph()


st.divider()

# Initialize session state
if "route" not in st.session_state:
    st.session_state.route = None
    st.session_state.distance = None
    st.session_state.start = None
    st.session_state.end = None

# Input boxes
source = st.text_input(
    "📍 Source",
    placeholder="Vadodara Railway Station"
)

destination = st.text_input(
    "📍 Destination",
    placeholder="Laxmi Vilas Palace"
)

if st.button("🚀 Find Best Route"):

    if source == "" or destination == "":
     st.warning("⚠️ Please enter both locations.")
     st.stop()

    else:

        start = geocode_location(source)
        end = geocode_location(destination)

        if start is None or end is None:
            st.error("Location not found.")

        else:

         with st.spinner("🤖 AI is calculating the best route..."):

              route, distance = find_route(
                  G,
                  start,
                  end
              )   

    distance_km = distance / 1000
    speed = 30

    eta = round((distance_km / speed) * 60)

    arrival_time = (
        datetime.now() + timedelta(minutes=eta)
    ).strftime("%I:%M %p")

    st.session_state.route = route
    st.session_state.distance = distance
    st.session_state.start = start
    st.session_state.end = end
    st.session_state.eta = eta
    st.session_state.arrival_time = arrival_time

    st.success("✅ Route Found!")
# Display result after rerun
if st.session_state.route is not None:

    st.success("Route Found Successfully!")
    st.balloons()

    col1, col2, col3 = st.columns(3)

    with col1:
        pass

    with col2:
        pass

    with col3:
        pass
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg,#2563eb,#1d4ed8);
        padding:20px;
        border-radius:18px;
        text-align:center;
        color:white;
        box-shadow:0 8px 20px rgba(37,99,235,.35);">
        <h4>📏 Distance</h4>
        <h2>{st.session_state.distance/1000:.2f} km</h2>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
    <div style="
        background: linear-gradient(135deg,#06b6d4,#0891b2);
        padding:20px;
        border-radius:18px;
        text-align:center;
        color:white;
        box-shadow:0 8px 20px rgba(6,182,212,.35);">
        <h4>⏱ ETA</h4>
        <h2>{st.session_state.eta} min</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
     st.markdown(f"""
    <div style="
        background: linear-gradient(135deg,#7c3aed,#6d28d9);
        padding:20px;
        border-radius:18px;
        text-align:center;
        color:white;
        box-shadow:0 8px 20px rgba(124,58,237,.35);">
        <h4>🛣 Route Nodes</h4>
        <h2>{len(st.session_state.route)}</h2>
    </div>
    """, unsafe_allow_html=True)
    st.info(
        "🤖 AI Recommendation\n\n"
        "Recommended Route\n\n"
        "✔ Shortest Route\n"
        "✔ Good Connectivity\n"
        "✔ Fuel Efficient"
    )
    st.subheader("🤖 GatiX AI Assistant")

    st.info(
    f"""
    🚗 **Best route selected successfully!**

    🕒 If you leave **now**, you'll arrive by **{st.session_state.arrival_time}**.
    📏 Total distance: **{st.session_state.distance/1000:.2f} km**

    ⏱ Estimated travel time: **{st.session_state.eta} minutes**

    🌱 This route is currently the **shortest and most fuel-efficient** path available.

     Have a safe journey! 🚀
     """
     )

if st.session_state.route is not None:
    display_map(
        G,
        st.session_state.route,
        st.session_state.start,
        st.session_state.end
    )
