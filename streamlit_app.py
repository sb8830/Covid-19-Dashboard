
import pandas as pd
import streamlit as st

df = pd.read_csv("covid_data.csv")

st.title("Live COVID-19 Dashboard")
st.markdown("Source: WHO Public API")

country = st.selectbox("Select Country", df['Country'].unique())
filtered = df[df['Country'] == country]

st.metric("Total Confirmed", int(filtered['TotalConfirmed']))
st.metric("Total Deaths", int(filtered['TotalDeaths']))
st.metric("Total Recovered", int(filtered['TotalRecovered']))
