# COVID-19-project

#  COVID-19 Global Data Analysis

A data-driven project analyzing COVID-19 trends across countries using Python. The goal is to explore the progression of cases, deaths, and vaccinations globally with visual insights using real-world data.


# Project Objectives

- Import and clean COVID-19 data from reliable sources.
- Analyze trends in total cases, deaths, and vaccinations.
- Compare key metrics across countries (Kenya, United States, India).
- Visualize patterns using clear and informative charts.
- Generate insights and present them in a Jupyter Notebook or PDF report.


# Tools & Libraries Used

- Python
- [pandas](https://pandas.pydata.org/) – for data manipulation
- [matplotlib](https://matplotlib.org/) – for basic plotting
- [seaborn](https://seaborn.pydata.org/) – for statistical visualizations
- [plotly](https://plotly.com/python/) *(optional)* – for interactive maps
- [Jupyter Notebook](https://jupyter.org/) – to write and present the analysis

---

# How to Run the Project

1. **Download Dataset:**
   - Get `owid-covid-data.csv` from [Our World in Data](https://ourworldindata.org/coronavirus-source-data).
   - Save it in your working directory.

2. **Open and Run:**
   - Open `covid_data_analysis.ipynb` in Jupyter Notebook or
   - Run the Python script `covid_data_analysis.py` in any IDE or notebook environment.

3. **View Output:**
   - Charts will display trends for total cases, deaths, and vaccinations.
   - Insights are printed at the end or annotated in Markdown cells (if using the notebook).


# Sample Insights

- **India** experienced a major spike in cases during May 2021.
- **Kenya** showed a steady increase in vaccination from mid-2021.
- **USA** had a rapid vaccine rollout, especially early in 2021.
- There is a clear correlation between vaccination uptake and declining death rates.


# Files Included

- `covid_data_analysis.py` – Python script containing all steps.
- *(optional)* `covid_data_analysis.ipynb` – if using a Jupyter Notebook format.
- `README.md` – this documentation.

---

# Notes

- You can export the final Jupyter Notebook as a PDF for presentation.
- Interactive world maps require the Plotly library.


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

# Step 6: Choropleth Map 
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

