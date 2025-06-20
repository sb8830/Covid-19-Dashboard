import pandas as pd
import streamlit as st
import requests

# Fetch live data from WHO API
st.title("Live COVID-19 Dashboard")
url = "https://api.covid19api.com/summary"
response = requests.get(url)
data = response.json()

# Parse data
countries_data = data['Countries']
df = pd.DataFrame(countries_data)

# Display
st.markdown("Source: WHO Public API")
country = st.selectbox("Select Country", df['Country'].unique())
filtered = df[df['Country'] == country]

st.metric("Total Confirmed", int(filtered['TotalConfirmed']))
st.metric("Total Deaths", int(filtered['TotalDeaths']))
st.metric("Total Recovered", int(filtered['TotalRecovered']))
