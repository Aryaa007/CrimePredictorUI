import streamlit as st
import pandas as pd
import pydeck as pdk
import matplotlib.pyplot as plt


st.set_page_config(layout="wide")
st.title("Crime Risk Visualizer - Crime Dashboard")

#Crime Risk Model Data
df = pd.read_csv("Final.csv").dropna()

df['State'] = df['State'].str.title()
df['District_x'] = df['District_x'].str.title()

Highrisk = df["RAPE"].quantile(0.75)
Lowrisk = df["RAPE"].quantile(0.25)

def get_risk_category(case_count):
    if case_count >= Highrisk:
        return "High Risk"
    elif case_count <= Lowrisk:
        return "Low Risk"
    return "Medium Risk"
 
#Adding data of how risk each district is
df["Risk Category"] = df["RAPE"].apply(get_risk_category)


color_map = {
    "Low Risk": [0, 255, 0],
    "Medium Risk": [255, 165, 0],
    "High Risk": [255, 0, 0],
}
df["color_map"] = df["Risk Category"].apply(lambda x: color_map[x])
df["elevation"] = df["RAPE"] * 25  


st.sidebar.header("🗺️ Choose Location")
states = sorted(df["State"].unique())
state = st.sidebar.selectbox("Select State", states)

districts = sorted(df[df["State"] == state]["District_x"].unique())
district = st.sidebar.selectbox("Select District", districts)

# Focusing view on selected district
focus = df[(df["State"] == state) & (df["District_x"] == district)]
focus_lat = float(focus.iloc[0]["lat"])
focus_lng = float(focus.iloc[0]["lng"])

view_state = pdk.ViewState(
    latitude=focus_lat,
    longitude=focus_lng,
    zoom=7,
    pitch=60,
)

#Risk Report
st.markdown(f"### 🏙️ Risk Report: **{district.upper()}, {state.upper()}**")

col1, col2 = st.columns(2)

risk_colors = {"High Risk": "#FF0000", "Medium Risk": "#FFA500", "Low Risk": "#00FF00"}
level = focus.iloc[0]["Risk Category"]

with col1:
    st.markdown(f"<h2 style='text-align: center; color: {risk_colors[level]}'>{level}</h2>", unsafe_allow_html=True)

with col2:
    st.metric("Historical Rape Cases", int(focus.iloc[0]["RAPE"]))

st.markdown("<hr style='border: 1px solid #444;'>", unsafe_allow_html=True)

#Map
st.subheader("🌍 Regional Risk Map View")

layer = pdk.Layer(
    "ColumnLayer",
    data=df,
    get_position='[lng, lat]',
    get_elevation="elevation",
    elevation_scale=30,
    radius=15000,
    get_fill_color="color_map",
    pickable=True,
    auto_highlight=True,
)

tooltip = {
    "html": "<b>District:</b> {District_x}<br/>"
            "<b>State:</b> {State}<br/>"
            "<b>Rape Cases:</b> {RAPE}<br/>"
            "<b>Risk Level:</b> {Risk Category}",
    "style": {
        "backgroundColor": "black",
        "color": "white"
    }
}

st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip=tooltip))

focus_row = focus.iloc[0]

#Raw data
with st.expander("📂 See Raw Data"):
    st.dataframe(df)

#Demographic Factors
st.markdown("### 📌 Demographic Risk Factors")

density = focus_row["Population Density"]
literacy = focus_row["Literacy"]
unemp = focus_row["Estimated Unemployment Rate (%)"]
male = focus_row["Male Population"]
female = focus_row["Female Population"]
gender_ratio = round((female / male) * 100, 2)

risk_flags = []

# Population Density
if density > 1000:
    risk_flags.append(f"🏙️ **High Population Density**: {density} people/sq km - Can contribute to stress, reduced space for safety.")

# Literacy Rate
if literacy < 70:
    risk_flags.append(f"📚 **Low Literacy Rate**: {literacy}% - Less awareness and poor reporting culture might prevail.")

# Unemployment
if unemp > 6:
    risk_flags.append(f"💼 **Elevated Unemployment**: {unemp}% - Economic frustration often fuels aggression or vulnerability.")

if not risk_flags:
    st.success("✨ Demographic indicators look stable. This district shows no major demographic red flags.")
else:
    for flag in risk_flags:
        st.warning(flag)

#Historical Trend
st.markdown("### 📊 Historical Trend of Rape Cases")


historical_data = df[(df["State"] == state) & (df["District_x"] == district)]

trend = historical_data.groupby("YEAR")["RAPE"].sum().reset_index()

if not trend.empty:
    fig, ax = plt.subplots()
    ax.plot(trend["YEAR"], trend["RAPE"], marker='o', color='crimson', linewidth=2)
    ax.set_title(f"Year-wise Reported Rape Cases in {district}, {state}", fontsize=14)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Reported Rape Cases", fontsize=12)
    ax.grid(True)
    st.pyplot(fig)
else:
    st.info("📉 No historical data available for this district.")
