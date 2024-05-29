import pandas as pd
import matplotlib.pyplot as plt

# Load the filtered dataset
movies_1990s = pd.read_csv('data/movies_1990s.csv')

# Visualize the duration column of your filtered data to see the distribution of movie durations
plt.hist(movies_1990s["duration"], bins=10)
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

# Save the most frequent movie duration in the 1990s
duration = 100
print(f"The most frequent movie duration in the 1990s is approximately {duration} minutes.")

# Filter the data again to keep only the Action movies
action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

# Use a for loop and a counter to count how many short action movies there were in the 1990s
# Start the counter
short_movie_count = 0

# Iterate over the labels and rows of the DataFrame and check if the duration is less than 90
for label, row in action_movies_1990s.iterrows():
    if row["duration"] < 90:
        short_movie_count += 1

print(f"Number of short action movies in the 1990s: {short_movie_count}")

# A quicker way of counting values in a column is to use .sum() on the desired column
quick_count = (action_movies_1990s["duration"] < 90).sum()

assert short_movie_count == quick_count, "Counts do not match!"
