# Exploratory Data Analysis (EDA) on Dynamic Pricing

## Project Overview

Welcome to the Exploratory Data Analysis (EDA) project on dynamic pricing. This project dives into a dataset that explores various aspects of ride pricing, including rider behavior, booking details, and more. The goal is to uncover insights and patterns through data visualization and statistical analysis.

## Dataset Details

The data used for this analysis is sourced from `data/dynamic_pricing.csv`. It includes a mix of numerical and categorical features:

### Numerical Features
- `Number_of_Riders`
- `Number_of_Drivers`
- `Number_of_Past_Rides`
- `Average_Ratings`
- `Expected_Ride_Duration`
- `Historical_Cost_of_Ride`

### Categorical Features
- `Location_Category`
- `Customer_Loyalty_Status`
- `Time_of_Booking`
- `Vehicle_Type`

## Analysis Steps

Here’s a rundown of the analysis performed:

1. **Data Inspection**: Examining the first few rows and the metadata of the dataset to understand its structure and identify any missing values.
2. **Missing Values Report**: Generating a report on missing values and their types for each column.
3. **Descriptive Statistics**: Calculating summary statistics for numerical features to get a sense of their distributions.
4. **Visualizations**:
   - **Numerical Features**: Plotting histograms with Kernel Density Estimates (KDE) to explore the distributions of numerical variables.
   - **Categorical Features**: Using count plots to analyze the distribution of categorical variables.
   - **Correlation Analysis**: Creating scatter plots to investigate the relationship between numerical features and `Historical_Cost_of_Ride`.
   - **Categorical Impact**: Displaying box plots to understand how different categories affect `Historical_Cost_of_Ride`.

## Setup and Dependencies

To run the analysis, ensure you have the following Python libraries installed:

- `pandas`
- `matplotlib`
- `seaborn`

You can install them using pip:

```
pip install pandas matplotlib seaborn


