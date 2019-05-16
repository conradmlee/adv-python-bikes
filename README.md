# Advanced Python: Bike Sharing analysis using Dask 
Analysis of Bike Sharing in Washington D.C. dataset using Dask data structures and ecosystem (instead of Pandas).

## Introduction
The goal of this assignment is to predict the total count of bike rentals during each hour. This notebook explains how we can explore and prepare the data for model building.
For this purpose, we have structured the project into the following steps:

1. Data Summary
2. Feature Engineering: Part I
3. Missing Value Analysis
4. Exploratory data analysis
5. Outlier Analysis
6. Correlation Analysis
7. Feature Engineering: Part II
8. Linear Regression Model
9. Decision Tree
10. Random Forest Regression
11. XGBoost

## Data

The data comes from the Kaggle competition: "Bike Sharing in Washington D.C. Dataset: Rental bikes in 2011 and 2012 with corresponding weather and seasonal info." The data is contained in two files: hour.csv and day.csv.

Acknowledgements: Hadi Fanaee-T Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto INESC Porto, Campus da FEUP Rua Dr. Roberto Frias, 378 4200 - 465 Porto, Portugal.

Link: https://www.kaggle.com/marklvl/bike-sharing-dataset/home

## Content
Both hour.csv and day.csv have the following fields, except hr which is not available in day.csv:

- instant: Record index
- dteday: Date
- season: Season (1:springer, 2:summer, 3:fall, 4:winter)
- yr: Year (0: 2011, 1:2012)
- mnth: Month (1 to 12)
- hr: Hour (0 to 23)
- holiday: weather day is holiday or not (extracted from Holiday Schedule)
- weekday: Day of the week
- workingday: If day is neither weekend nor holiday is 1, otherwise is 0.
- weathersit: (extracted from Freemeteo)
- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp: Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
- atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
- hum: Normalized humidity. The values are divided to 100 (max)
- windspeed: Normalized wind speed. The values are divided to 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered
