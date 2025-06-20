
# Live COVID-19 Dashboard with WHO API

This project fetches real-time COVID-19 data from the WHO API using Python and visualizes it through a Streamlit app and Power BI dashboard.

## Features:
- Real-time global COVID-19 statistics
- Country-wise confirmed, deaths, recovered metrics
- Streamlit-based web app for user-friendly interaction

## Tech Stack:
- Python (Requests, Pandas)
- Streamlit
- Power BI
- WHO API

## How to Run:
1. Run `covid_api_fetch.py` to fetch and save the latest data
2. Run `streamlit run streamlit_app.py` to launch the app locally
3. Or deploy via [Streamlit Cloud](https://streamlit.io/cloud)

## File Structure:
- `covid_api_fetch.py`: Script to fetch WHO COVID-19 data
- `covid_data.csv`: Output data file
- `streamlit_app.py`: Streamlit dashboard app
