import pandas as pd

# Load the dataset
df = pd.read_csv('data/netflix_data.csv')

# Inspect the dataset
print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Handle missing values (optional)
# For this project, handling missing values is out of scope. If needed, uncomment the following line:
# df = df.dropna()

# Convert data types where necessary
df['date_added'] = pd.to_datetime(df['date_added'])

# Save the cleaned data (optional)
df.to_csv('data/netflix_data_cleaned.csv', index=False)

print("Data preparation is complete.")
