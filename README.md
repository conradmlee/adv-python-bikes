# Advanced Python: Bike Sharing analysis using Dask 
Analysis of Bike Sharing in Washington D.C. dataset using Dask data structures and ecosystem (instead of Pandas).

## Introduction

The objective is to perform an analysis of the Bike Sharing in DC dataset using Dask data structures and ecosystem. The purpose of using Dask is to implement a parallel computing system in Python. The primary components of Dask that we will be using include: Dask DataFrames, distributed.Client (working with Future objects), and Dask-ML (to run distributed ML algorithms and hyperparameter tuning). We will also be making use of the Kaggle API to perform an automatically download of the dataset (instead of hosting the data directly on Github which is typically considered bad practice).

The goal of the original Bike Sharing analysis is to predict the total count of bike rentals during each hour. This notebook explains how we can explore and prepare the data for model building.

For this purpose, we have structured the project into the following steps:

1. Load Libraries
2. Load Dataset
3.	Data Summary
4.	Feature Engineering: Part I
5.	Missing Value Analysis
6.	Exploratory data analysis 
7.	Outlier Analysis
8.	Correlation Analysis
9. Feature Engineering: Part II
10. Train Test Split
11.	Linear Regression Model
12.	Decision Tree
13.	Random Forest Regression
14.	XGBoost

## Instructions

1. Run the bash file "load.sh" in command line (should work for both Windows and Mac/Linux) which will automatically download and extract the dataset from Kaggle.
2. Run the bikesharing.ipynb Jupyter notebook, which contains the Dask analysis.

## Data

The data comes from the Kaggle competition: "Bike Sharing in Washington D.C. Dataset: Rental bikes in 2011 and 2012 with corresponding weather and seasonal info." The data is contained in two files: hour.csv and day.csv.

Acknowledgements: Hadi Fanaee-T Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto INESC Porto, Campus da FEUP Rua Dr. Roberto Frias, 378 4200 - 465 Porto, Portugal.

Kaggle API: https://github.com/Kaggle/kaggle-api

Bike Sharing Dataset: https://www.kaggle.com/marklvl/bike-sharing-dataset/home

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
