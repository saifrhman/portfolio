import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('data/netflix_data_cleaned.csv')

# Summary statistics
print("Summary Statistics:")
print(df.describe())

# Distribution of movie durations
sns.histplot(df[df['type'] == 'Movie']['duration'].dropna(), bins=30, kde=True)
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Frequency')
plt.show()

# Trend of movie durations over the years
movies = df[df['type'] == 'Movie']
movies_by_year = movies.groupby('release_year')['duration'].mean().reset_index()

plt.plot(movies_by_year['release_year'], movies_by_year['duration'])
plt.title('Average Movie Duration Over the Years')
plt.xlabel('Year')
plt.ylabel('Average Duration (minutes)')
plt.show()

print("EDA is complete.")
