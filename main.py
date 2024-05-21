import streamlit as st
import plotly.express as px
from backend import getData

#Designing the User interface:

st.title("Weather Forecast for the next days")
loc = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value = 1, max_value = 5,help = "Select the number of days to forecast")
options = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{options} for the next {days} in {loc}")

#Getting the weather data:
if loc:
    filtered_data = getData(loc,days)

    #Creating the plot:

    if options == "Temperature":
        dates = [dict["main"]["temp"] for dict in filtered_data]
        temperatures = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperatures,labels={"x":"Date", "y":"Temperature (C)"})
        st.plotly_chart(figure)

    elif options == "Sky":
        icons = {"Clear":"images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png", "Snow":"images/snow.png"}
        skyConditions = [dict["weather"][0]["main"] for dict in filtered_data]
        print(skyConditions)
        st.image()