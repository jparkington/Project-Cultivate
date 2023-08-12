<!-- omit in toc -->
# Project Derailleur
*Analyzing Bike Sharing Data to Practice Data Science Techniques*

This repository contains a detailed analysis of the UCI Bike Sharing Dataset, complete with visualizations, insights, and a series of questions that guide the exploration of data. The project utilizes Python libraries such as Pandas, Seaborn, and Matplotlib to analyze bike rental patterns, seasonal trends, and more.

<!-- omit in toc -->
## Table of Contents

- [Introduction](#introduction)
- [Questions \& Analysis](#questions--analysis)
  - [Data Preparation](#data-preparation)
    - [Importing Libraries and Configuring Plot Parameters](#importing-libraries-and-configuring-plot-parameters)
    - [Data Preprocessing and Transformation](#data-preprocessing-and-transformation)
  - [Data Exploration and Visualization Techniques](#data-exploration-and-visualization-techniques)
    - [Scatter and Bar Plots](#scatter-and-bar-plots)
    - [Advanced Visualizations](#advanced-visualizations)
  - [Predictive Analytics and Modeling](#predictive-analytics-and-modeling)
    - [Linear and Multiple Linear Regression](#linear-and-multiple-linear-regression)
  - [Specific Analysis Techniques](#specific-analysis-techniques)
    - [Seasonal, Weekday, and Hourly Analysis](#seasonal-weekday-and-hourly-analysis)
    - [Weather Impact and User Behavior](#weather-impact-and-user-behavior)
- [Classes](#classes)
- [Dataset](#dataset)
- [Setup and Usage](#setup-and-usage)
- [Authors and Acknowledgements](#authors-and-acknowledgements)

## Introduction

Project Derailleur is a comprehensive analysis of bike-sharing data, providing insights into rental patterns, customer preferences, and business strategies. By analyzing various attributes such as season, weekday, hour, and weather conditions, the project offers valuable information for pricing strategies, staff scheduling, and promotional events. Through a series of classes and an interactive Navigator, users can step through each question and visualize the data.

The project leverages technologies such as [nbformat](https://nbformat.readthedocs.io), [PIL](https://pillow.readthedocs.io), and [tkinter](https://docs.python.org/3/library/tkinter.html), creating a visually engaging experience.

## Questions & Analysis

### Data Preparation

#### Importing Libraries and Configuring Plot Parameters

- **Libraries Used**: Utilizes `numpy`, `pandas`, `seaborn`, `matplotlib`, `scipy` for data manipulation, analysis, and visualization.
- **Plot Configuration**: Defines `plot_params` for default plot attributes, enabling consistency across all plots.

#### Data Preprocessing and Transformation

- **Date Parsing**: Parses dates into datetime format to facilitate time series analysis.
- **Variable Extraction**: Extracts year, month, day, and weekday, providing a rich set of features for analysis.
- **Binning**: Bins continuous variables like temperature for interpretability.

### Data Exploration and Visualization Techniques

#### Scatter and Bar Plots

- **Scatter Plots**: Visualizes relationships between variables, such as temperature and bike rentals.
- **Bar Plots**: Analyzes categorical variables like season and weather, providing insights into rental patterns.

#### Advanced Visualizations

- **Heatmaps**: Displays correlations between features, aiding in feature selection.
- **KDE Plots**: Estimates the probability density function, revealing underlying distributions.
- **Box Plots**: Offers insights into data distribution and outliers, supporting data cleaning.
- **Time Series Plots**: Analyzes trends and seasonality over time, informing seasonal strategies.

### Predictive Analytics and Modeling

#### Linear and Multiple Linear Regression

- **Linear Regression**: Models relationships with single predictors, such as temperature vs rentals.
- **Multiple Linear Regression (MLR)**: Analyzes multiple features, enabling complex predictions.
- **Polynomial Regression**: Captures nonlinear relationships, adding flexibility to the model.
- **Optimization**: Finds optimal parameters using `scipy.optimize.minimize`, enhancing model performance.
- **Model Evaluation**: Applies MSE and R-squared metrics, ensuring model quality.

### Specific Analysis Techniques

#### Seasonal, Weekday, and Hourly Analysis

- **Seasonal Analysis**: Informs pricing strategies based on seasonal trends.
- **Weekday Analysis**: Guides staff scheduling and promotions by analyzing weekday patterns.
- **Hourly Patterns**: Offers insights into peak hours, supporting discounts and special offers.

#### Weather Impact and User Behavior

- **Weather Impact**: Examines how different weather conditions affect bike rentals.
- **User Behavior**: Analyzes casual versus registered users, informing targeted marketing strategies.

## Classes

- **Notebook**: Reads a Jupyter Notebook file and extracts questions, charts, and code snippets.
- **Navigator**: Provides an interactive slideshow for viewing a list of questions, charts, and code snippets using tkinter.

Detailed descriptions of the classes are provided in the code files with extensive comments.

## Dataset

The Bike Sharing Dataset used in this analysis is authored by Hadi Fanaee-T and affiliated with the Laboratory of Artificial Intelligence and Decision Support (LIAAD), University of Porto. The dataset provides information about bike-sharing systems, including aspects related to traffic, environment, and health.

- **Attributes**: Detailed attributes such as season, weather, temperature, and rental count.
- **Instances**: Information about instances and their significance in the analysis.
- More information can be found in the dataset README file.

## Setup and Usage

1. Clone this repository to your local machine.
2. Install [Python](https://www.python.org/downloads/).
3. Navigate to the repository's directory in the terminal.
4. Install the dependencies using the `pyproject.toml` file.
5. Run the `Application.py` file: `python Application.py`

## Authors and Acknowledgements

This project was developed by [James Parkington](https://github.com/jparkington).

It was shaped under the supervision of [Dr. Maryam Farahmand](https://www.linkedin.com/in/maryam-farahmand-asil-258a6315/) during class *5010 - Intro to Programming for Data Science* at the **Roux Institute of Northeastern University**.

I would like to express my gratitude to both Professor Jamieson for her guidance and my classmate Nelson Farrell for their valuable input and collaboration.