#!/bin/bash

# URL 
URL = "https://iammunibmir-weather-forecast-app-main-zzt3wh.streamlit.app"

# Send a request to the server
curl -s $URL > /dev/null
