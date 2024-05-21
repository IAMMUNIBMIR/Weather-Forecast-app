import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the next days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value = 1, max_value = 5,help = "Select the number of days to forecast")
options = st.selectbox("Select data to view",("Temperature","Sky"))
st.subheader(f"{options} for the next {days} in {place}")


def getData(days):

    dates = ["25-10-2025","26-10-2025","27-10-2025"]
    temperatures = [10,11,15]
    temperatures = [days * i for i in temperatures]

    return days,temperatures


dates,temperatures = getData(days)
figure = px.line(x=dates, y=temperatures,labels={"x":"Date", "y":"Temperature (C)"})
st.plotly_chart(figure)