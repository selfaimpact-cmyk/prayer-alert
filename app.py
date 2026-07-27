import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="Prayer Alert Dashboard", page_icon="🔔", layout="centered")

st.title("🔔 Prayer Alert Engine")
st.markdown("### *Silicon Valley Lean MVP Prototype (Cost: $0.00)*")
st.divider()

# 2. Sidebar Settings (Group Info)
st.sidebar.header("📋 Altar Configuration")
group_name = st.sidebar.text_input("Group/Altar Name", value="Selsa Global Network")
shared_focus = st.sidebar.text_area("Daily Prayer Focus", value="Economic Breakthrough and Peace")

# 3. Main Interface Elements
st.subheader("🌐 Global Time-Zone Synchronizer")
col1, col2 = st.columns(2)

with col1:
    city = st.text_input("Target City", value="Jos")
with col2:
    country = st.text_input("Target Country", value="Nigeria")

# Trigger Live API Sync
if st.button("🔄 Sync Regional Prayer Times", type="primary"):
    url = "https://api.aladhan.com/v1/timingsByCity"
    params = {"city": city, "country": country, "method": 2}
    
    try:
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            timings = data["data"]["timings"]
            
            st.success(f"✅ Real-Time Coordinates Synced for {city}!")
            
            # Display metrics beautifully
            m1, m2, m3 = st.columns(3)
            m1.metric("🌅 Fajr", timings["Fajr"])
            m2.metric("☀️ Dhuhr", timings["Dhuhr"])
            m3.metric("🌆 Maghrib", timings["Maghrib"])
        else:
            st.error("API Connection dropped. Check spelling.")
    except Exception as e:
        st.error(f"Network error: {e}")

st.divider()

# 4. Group Broadcasting simulation
st.subheader("📡 Zero-Cost Core Broadcaster")
st.write(f"**Active Altar:** {group_name}")
st.write(f"**Focus Cues:** \"{shared_focus}\"")

# Roster mockup
mock_members = ["Simi (Jos)", "Blessing (Lagos)", "Manjang (London)", "Nabiel (Mumbai)"]
st.info(f"👥 Group Members Subscribed: {', '.join(mock_members)}")

if st.button("🚀 Trigger Global Web Push"):
    st.balloons()  # Fun visual celebration animation
    st.success("✨ Success! Browser Web-Push packets routed successfully to all 4 continents at $0.00 cost.")