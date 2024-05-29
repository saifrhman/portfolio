import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('data/netflix_data_cleaned.csv')

# Formulate the hypothesis
# H0: The average duration of movies has not changed over the years.
# H1: The average duration of movies has changed over the years.

# Prepare the data for hypothesis testing
movies = df[df['type'] == 'Movie']
movies_by_year = movies.groupby('release_year')['duration'].mean().reset_index()

# Perform t-test
years = movies_by_year['release_year']
durations = movies_by_year['duration']

slope, intercept, r_value, p_value, std_err = stats.linregress(years, durations)

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
print(f"P-value: {p_value}")

# Visualize the trend
plt.plot(years, durations, 'o', label='Original data')
plt.plot(years, intercept + slope*years, 'r', label='Fitted line')
plt.xlabel('Year')
plt.ylabel('Average Duration (minutes)')
plt.title('Trend of Movie Durations Over the Years')
plt.legend()
plt.show()

if p_value < 0.05:
    print("Reject the null hypothesis: The average duration of movies has changed over the years.")
else:
    print("Fail to reject the null hypothesis: No significant change in the average duration of movies over the years.")

print("Hypothesis testing is complete.")
