import pandas as pd
from scipy import stats

# Load the filtered dataset
movies_1990s = pd.read_csv('data/movies_1990s.csv')

# Group by year and calculate the mean duration
mean_durations_by_year = movies_1990s.groupby('release_year')['duration'].mean().reset_index()

# Perform linear regression
years = mean_durations_by_year['release_year']
durations = mean_durations_by_year['duration']
slope, intercept, r_value, p_value, std_err = stats.linregress(years, durations)

# Print the regression results
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")
print(f"Standard Error: {std_err}")

# Interpretation of the results
if p_value < 0.05:
    print("The average duration of movies has changed significantly over the years.")
else:
    print("There is no significant change in the average duration of movies over the years.")
