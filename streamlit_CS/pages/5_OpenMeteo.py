# READ API ONCE:
import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

st.set_page_config(page_title="Live Denver Weather", page_icon="📡", layout="wide")
# Disable fade/transition so charts don't blink between reruns
st.markdown("""
    <style>
      [data-testid="stPlotlyChart"], .stPlotlyChart, .stElementContainer {
        transition: none !important;
        opacity: 1 !important;
      }
    </style>
""", unsafe_allow_html=True)

st.title("📡 Live Denver Weather (Open Meteo)")

# CONFIG:
def build_url(lat, lon):
    return f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"

lat, lon = 39.7392, -104.9903  # Denver
wurl = build_url(lat, lon)

# FETCH (CACHED):
@st.cache_data(ttl=600)

def get_weather():
    r = requests.get(wurl, timeout=10); r.raise_for_status()
    j = r.json()["current"]
    return pd.DataFrame([{"time": pd.to_datetime(j["time"]),
                          "temperature": j["temperature_2m"],
                          "wind": j["wind_speed_10m"]}])
# REFRESH BUTTON:
# --- Auto Refresh Controls ---
st.subheader("🔁 Auto Refresh Settings")

# Let user choose how often to refresh (in seconds)
refresh_sec = st.slider("Refresh every (sec)", 10, 120, 30)

# Toggle to turn automatic refreshing on/off
auto_refresh = st.toggle("Enable auto-refresh", value=False)

# Show current refresh time
st.caption(f"Last refreshed at: {time.strftime('%H:%M:%S')}")

# MAIN VIEW:
st.subheader("Temperature Over Time")
df = get_weather()

st.dataframe(df, use_container_width=True)

fig = px.line(df, x="time", y="temperature", title='Temperature Over Time')
st.plotly_chart(fig, use_container_width=True)

# If auto-refresh is ON, wait and rerun the app
if auto_refresh:
    time.sleep(refresh_sec)
    get_weather.clear()
    # st.rerun()
