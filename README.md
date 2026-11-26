
# SDG 7: Global Clean Energy Analytics

An exploratory data analysis and econometric study examining the economic, infrastructural, and environmental factors associated with renewable energy consumption across countries.

## Project Overview

This project investigates the factors associated with renewable energy consumption as a share of total final energy consumption across countries and years. It focuses on the relationship between renewable energy adoption and selected indicators, including GDP per capita, urbanization, electricity access, and CO₂ emissions per capita.

The project combines data analysis, statistical modeling, and an interactive Streamlit dashboard to present global clean energy trends and explore relationships between key development indicators.

## Research Objectives

- Examine global trends in renewable energy consumption across countries.
- Analyze the relationship between renewable energy consumption and GDP per capita.
- Investigate the association between renewable energy consumption, electricity access, and urbanization.
- Explore the relationship between CO₂ emissions per capita and renewable energy consumption.
- Present key findings through statistical analysis and interactive visualizations.

## Research Questions

1. How is GDP per capita associated with renewable energy consumption?
2. What is the relationship between CO₂ emissions per capita and renewable energy adoption?
3. Does greater access to electricity correspond to higher renewable energy consumption?
4. How is urbanization associated with the transition toward renewable energy?

## Dataset and Data Sources

The study uses a country-level panel dataset containing more than 4,300 observations.

### World Bank Open Data

The following indicators were obtained from the World Bank:

- Renewable Energy Consumption (% of total final energy consumption)
- GDP per Capita (current US$)
- Urban Population (% of total population)
- Access to Electricity (% of population)

Source: [World Bank Open Data](https://data.worldbank.org/)

### Our World in Data

- CO₂ Emissions per Capita

Source: [Our World in Data](https://ourworldindata.org/)

## Methodology

The project followed these analytical procedures:

1. **Data Collection** – Gathered country-level indicators from the World Bank and Our World in Data.
2. **Data Preprocessing** – Cleaned, merged, and prepared the datasets for analysis.
3. **Exploratory Data Analysis** – Examined distributions, trends, and relationships among the selected variables.
4. **Statistical Analysis** – Used descriptive statistics, correlation analysis, and visualizations to explore the dataset.
5. **Econometric Modeling** – Applied Ordinary Least Squares (OLS) regression and Robust Linear Model (RLM) using Huber's M-estimation.
6. **Visualization** – Developed an interactive dashboard to explore renewable energy patterns and related indicators.

## Econometric Analysis

Two regression approaches were applied:

- **Ordinary Least Squares (OLS):** Used as the baseline regression model to examine the relationships between the selected explanatory variables and renewable energy consumption.
- **Robust Linear Model (RLM):** Applied using Huber's M-estimation to reduce the influence of outliers on the regression estimates.

### Regression Results

| Variable | OLS Coefficient | RLM Coefficient |
|---|---:|---:|
| Electricity Access | -0.6860 | -0.7110 |
| Urbanization | -0.0715 | -0.1249 |
| CO₂ Emissions per Capita | -1.01 | -0.88 |
| GDP per Capita | Approximately 0.0002 | Approximately 0.0002 |

### Key Findings

- **Electricity Access:** Shows a negative association with renewable energy consumption in the estimated models.
- **Urbanization:** Also exhibits a negative association, suggesting that higher urban population shares do not automatically correspond to greater renewable energy consumption.
- **CO₂ Emissions:** Shows a negative association with renewable energy consumption in the estimated models.
- **GDP per Capita:** Has a coefficient close to zero, indicating a relatively small estimated relationship in the model's measurement scale.

The OLS and RLM estimates show generally consistent directions across the explanatory variables. These results describe statistical associations within the dataset and should not be interpreted as evidence of causation.

## Interactive Dashboard

The project includes a Streamlit dashboard titled **SDG 7: Global Clean Energy Analytics Hub**, designed to explore renewable energy indicators through interactive visualizations.

### Dashboard Features

- **Key Performance Indicators** – Displays summary metrics for renewable energy consumption, GDP per capita, electricity access, and CO₂ emissions.
- **Country Rankings** – Compares countries based on renewable energy consumption.
- **Renewable Energy Distribution** – Examines renewable energy consumption across GDP-based wealth categories.
- **Electricity Access Analysis** – Explores the relationship between electricity access and renewable energy consumption.
- **GDP and CO₂ Analysis** – Visualizes the relationship between economic output and carbon emissions.
- **Global Renewable Energy Map** – Displays renewable energy consumption across countries.
- **Correlation Heatmap** – Presents correlations among the selected analytical variables.
- **Country-Level Data Table** – Allows users to inspect filtered observations.
- **Interactive Filters** – Supports filtering by year, country, GDP per capita, and electricity access.

## Technologies Used

- **Python** – Data analysis and application development
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations
- **Plotly** – Interactive data visualizations
- **Streamlit** – Interactive dashboard development
- **Jupyter Notebook** – Exploratory data analysis and econometric modeling

## Repository Contents

| File | Description |
|---|---|
| `ILARDE_SDG7_FINAL_PROJECT.ipynb` | Jupyter Notebook containing the data analysis and econometric study |
| `app.py` | Streamlit dashboard application |
| `cleaned_sdg7_data.csv` | Cleaned dataset used by the dashboard |
| `requirements.txt` | Python project dependencies |
| `README.md` | Project documentation |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/RalphIlarde/SDG7-Clean-Energy-Analytics.git
```

### 2. Navigate to the Project Directory

```bash
cd SDG7-Clean-Energy-Analytics
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## Sustainable Development Goal Alignment

This project supports **[United Nations Sustainable Development Goal 7 (SDG 7)](https://sdgs.un.org/goals/goal7): Affordable and Clean Energy**, which aims to ensure access to affordable, reliable, sustainable, and modern energy for all.

By analyzing renewable energy consumption and its associated economic, infrastructural, and environmental indicators, the project provides a data-driven perspective on global clean energy patterns.

## Author

**Ralph Victor Ilarde**  
BS Information Systems – Business Analytics  
West Visayas State University

GitHub: [RalphIlarde](https://github.com/RalphIlarde)
