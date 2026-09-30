import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
location = st.text_input("Location: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {location}")

data = get_data(location, days, option)

figure = px.line(x=dates, y=temperatures,
                 labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
