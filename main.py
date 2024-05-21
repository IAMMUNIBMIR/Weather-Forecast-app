import streamlit as st
import plotly.express as px
from backend import getData

# Designing the User Interface
st.title("Weather Forecast for the Next Days")
loc = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of days to forecast")
options = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{options} for the next {days} days in {loc}")

# Getting the weather data
if loc:
    filtered_data = getData(loc, days)
    
    if options == "Temperature":
        dates = [entry["dt_txt"] for entry in filtered_data]
        temperatures = [entry["main"]["temp"] for entry in filtered_data]
        
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
        st.plotly_chart(figure)

    elif options == "Sky":
        icons = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [entry["weather"][0]["main"] for entry in filtered_data]
        icon_paths = [icons[condition] for condition in sky_conditions]
        
        st.image(icon_paths, width=110)
