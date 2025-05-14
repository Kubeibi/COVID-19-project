# covid_data_analysis.ipynb (converted to .py script)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Optional imports for advanced visualization
try:
    import plotly.express as px
except ImportError:
    px = None

# Step 1: Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Step 2: Basic exploration
print("Columns in dataset:", df.columns.tolist())
print(df.head())
print(df.isnull().sum())

# Step 3: Data Cleaning
countries = ['Kenya', 'United States', 'India']
df = df[df['location'].isin(countries)]
df['date'] = pd.to_datetime(df['date'])
df.fillna(0, inplace=True)

# Step 4: Exploratory Data Analysis
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 5: Vaccination Progress
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title("Cumulative Vaccinations Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 6: Choropleth Map (optional)
if px:
    latest = df[df['date'] == df['date'].max()]
    fig = px.choropleth(latest,
                        locations='iso_code',
                        color='total_cases',
                        hover_name='location',
                        color_continuous_scale='Reds',
                        title="Global COVID-19 Total Cases")
    fig.show()

# Step 7: Sample Insights
print("\nSample Insights:")
print("1. India experienced a large spike in cases around May 2021.")
print("2. Kenya had a slower but steady vaccination progress.")
print("3. The US had the earliest and most aggressive vaccination rollout among the three.")
