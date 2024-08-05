import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("data/dynamic_pricing.csv")

# It will give data of top 5 rows
print(data.head())

# It will give the metadata of the dataset
print(data.info())

# It will count the number of null values in each column with their datatypes
missing_values = data.isnull().sum()
data_types = data.dtypes
missing_values_report = pd.DataFrame({'Missing Values': missing_values, 'Data Type': data_types})
print(missing_values_report)

# dividing dataset in numerical and categorical columns
numerical_cols = ['Number_of_Riders', 'Number_of_Drivers', 'Number_of_Past_Rides',
                  'Average_Ratings', 'Expected_Ride_Duration', 'Historical_Cost_of_Ride']
categorical_cols = ['Location_Category', 'Customer_Loyalty_Status', 'Time_of_Booking', 'Vehicle_Type']

# It will give all the numerical column's data like min , max , mean , count , etc
print(data.describe())

# set the aesthetics for the plots
sns.set_style("whitegrid")

# descriptive statistics for numerical features
descriptive_stats = data[numerical_cols].describe()

# plotting distributions for numerical features
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 12))
# we can say that axes is an array of 3*2(6) elements where each element is an object to a subplot and fig is the whole fig which contains all the 6 subplots
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i, col in enumerate(numerical_cols):
    sns.histplot(data[col], kde=True, ax=axes[i // 2, i % 2])
    axes[i // 2, i % 2].set_title(f'Distribution of {col}', fontsize=10)
    axes[i // 2, i % 2].set_xlabel('')
    axes[i // 2, i % 2].set_ylabel('')

plt.show()

# plotting distributions for categorical features
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.subplots_adjust(hspace=0.4, wspace=0.6)

for i, col in enumerate(categorical_cols):
    sns.countplot(data=data, x=col, ax=axes[i // 2, i % 2])
    axes[i // 2, i % 2].set_title(f'Distribution of {col}', fontsize=10)
    axes[i // 2, i % 2].set_xlabel('')
    axes[i // 2, i % 2].set_ylabel('')
    axes[i // 2, i % 2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()

num_plots = len(numerical_cols[:-1])
n_cols = 2
n_rows = (num_plots + 1) // n_cols

fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(14, n_rows * 4))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

axes = axes.flatten()

# plot each numerical column against the historical cost.
for i, col in enumerate(numerical_cols[:-1]):
    sns.scatterplot(data=data, x=col, y='Historical_Cost_of_Ride', ax=axes[i])
    axes[i].set_title(f'{col} vs Historical_Cost_of_Ride', fontsize=10)
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Historical_Cost_of_Ride')

for j in range(i + 1, n_rows * n_cols):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# bivariate Analysis: categorical features vs historical_cost_of_ride
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 12))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i, col in enumerate(categorical_cols):
    sns.boxplot(data=data, x=col, y='Historical_Cost_of_Ride', ax=axes[i//2, i%2])
    axes[i//2, i%2].set_title(f'{col} vs Historical_Cost_of_Ride', fontsize=10)
    axes[i//2, i%2].set_xlabel('')
    axes[i//2, i%2].set_ylabel('Historical_Cost_of_Ride')
    axes[i//2, i%2].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
