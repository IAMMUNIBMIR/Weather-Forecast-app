import streamlit as st
import plotly.express as px
from backend import getData

# Set page config
st.set_page_config(page_title="Weather Forecast", page_icon=":partly_sunny:", layout="centered")

# Custom CSS to enhance the appearance
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .stTextInput > div > input {
        border: 2px solid #1f77b4;
        border-radius: 5px;
    }
    .stSlider > div {
        color: #1f77b4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Designing the User Interface
st.title("Weather Forecast for the Next Days :partly_sunny:")

st.write("Get the weather forecast for your desired location and number of days. Select whether you want to view the temperature trends or sky conditions.")

loc = st.text_input("Enter the Location: ")
days = st.slider("Select the number of days for the forecast:", min_value=1, max_value=5, help="Select the number of days to forecast")
options = st.selectbox("Choose the data to view:", ("Temperature", "Sky"))

st.subheader(f"{options} forecast for the next {days} days in {loc}")

# Getting the weather data
if loc:
    filtered_data = getData(loc, days)

    if options == "Temperature":
        dates = [entry["dt_txt"] for entry in filtered_data]
        temperatures = [entry["main"]["temp"] - 273.15 for entry in filtered_data]  # Convert from Kelvin to Celsius

        figure = px.line(
            x=dates, y=temperatures, 
            labels={"x": "Date", "y": "Temperature (°C)"},
            title=f"Temperature Trend for the Next {days} Days in {loc}"
        )
        st.plotly_chart(figure)

    elif options == "Sky":
        icons = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [entry["weather"][0]["main"] for entry in filtered_data]
        icon_paths = [icons[condition] for condition in sky_conditions]

        st.write("Sky Conditions Forecast:")
        st.image(icon_paths, width=110, caption=sky_conditions)

