# Netflix Data Analysis

# Investigation of Netflix Movies

## Project Overview

This project aims to explore the Netflix dataset to investigate the hypothesis that the average duration of movies on Netflix has been declining over the years. The analysis involves examining the dataset, visualizing trends, and identifying any contributing factors to changes in movie lengths. This project leverages Python and its data analysis libraries to conduct exploratory data analysis (EDA).

## Dataset

The dataset used for this project is `netflix_data.csv`. Below is a table detailing the column names and descriptions:

| Column Name         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `show_id`           | Unique identifier for each show (movie or series)                           |
| `type`              | Type of the show (Movie or TV Show)                                         |
| `title`             | Title of the show                                                           |
| `director`          | Director of the show                                                        |
| `cast`              | Main cast of the show                                                       |
| `country`           | Country where the show was produced                                         |
| `date_added`        | Date when the show was added to Netflix                                     |
| `release_year`      | Year when the show was released                                             |
| `rating`            | Rating of the show (e.g., PG, R, etc.)                                      |
| `duration`          | Duration of the show (in minutes for movies, in seasons for TV shows)       |
| `listed_in`         | Genres the show is listed under                                             |
| `description`       | Brief description of the show                                               |

## Objectives

1. **Data Cleaning and Preparation:**
   - Load the dataset and inspect its structure.
   - Handle any missing values and outliers, if necessary (though this is out of scope for the project).
   - Convert data types where needed for accurate analysis.

2. **Exploratory Data Analysis (EDA):**
   - Analyze the distribution of movie durations.
   - Visualize the trend of movie durations over the years.
   - Identify any patterns or anomalies in the data.
   - Investigate contributing factors to changes in movie durations, such as genre or country of production.

3. **Hypothesis Testing:**
   - Test the hypothesis that the average duration of movies has been declining over the years.
   - Use appropriate statistical methods to support or refute the hypothesis.

## Tools and Libraries

The following tools and libraries are used in this project:

- **Python**: The primary programming language for the analysis.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib**: For data visualization.

## Project Structure

The project is structured as follows:

```
investigation-of-netflix-movies/
│
├── data/
│   └── netflix_data.csv
│
├── notebooks/
│   └── netflix_data_analysis.ipynb
│
├── src/
│   ├── data_preparation.py
│   ├── eda.py
│   └── hypothesis_testing.py
│
├── README.md
└── requirements.txt
```

- **data/**: Contains the dataset.
- **notebooks/**: Jupyter notebooks for interactive analysis.
- **src/**: Python scripts for data preparation, EDA, and hypothesis testing.
- **README.md**: Project documentation.
- **requirements.txt**: List of dependencies required for the project.


## Analysis of Netflix Data
# Distribution of movies in the 1990s
The histogram in the notebook shows the distribution of movie durations for Netflix movies released in the 1990s. The distribution gives us an idea of how long movies typically were during this decade.
# Counting Short Action Movies
Short action movies are defined as those with a duration of less than 90 minutes. We used two methods to count the number of short action movies released in the 1990s.

Using a for loop and a counter:

Number of short action movies: 8
Using the .sum() method for quicker counting:

Number of short action movies: 8
Both methods yielded the same result, confirming the consistency and accuracy of our data handling and analysis.

# Conclusion
Based on the analysis of the Netflix dataset for movies released in the 1990s, we can conclude the following:

Most Frequent Movie Duration:

The most frequent movie duration in the 1990s was approximately 100 minutes.
Short Action Movies:

A movie is considered short if it is less than 90 minutes. There were 8 short action movies released in the 1990s.
The histogram provides a clear visualization of the distribution of movie durations during this period, with the most common duration being around 100 minutes. This analysis helps in understanding the trends and patterns in movie durations over a specific decade and can be extended to other genres and time periods for a more comprehensive study.

This analysis helps in understanding the trends and patterns in movie durations over a specific decade and can be extended to other genres and time periods for a more comprehensive study.

# Acknowledgments
Special thanks to DataCamp who provided the initial research and dataset, and to the developers of the Python libraries used in this project.
