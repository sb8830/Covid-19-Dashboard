
import requests
import pandas as pd

url = "https://api.covid19api.com/summary"
response = requests.get(url)
data = response.json()

countries_data = data['Countries']
df = pd.DataFrame(countries_data)

df = df[['Country', 'TotalConfirmed', 'TotalDeaths', 'TotalRecovered', 'Date']]
df.to_csv('covid_data.csv', index=False)
print("Data saved to covid_data.csv")
