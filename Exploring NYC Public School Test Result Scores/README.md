# NYC Public Schools SAT Performance Analysis

## Overview

This project presents an in-depth analysis of SAT performance across New York City (NYC) public schools. The Scholastic Assessment Test (SAT) is a standardized test widely used for college admissions in the United States. It assesses students' readiness for college, covering literacy, numeracy, and writing skills. This analysis focuses on identifying the top-performing schools in math, overall SAT scores, and exploring trends across different boroughs in NYC. Additionally, the impact of SAT scores on college admissions is discussed.

## Objectives

1. Identify NYC schools with the best math results.
2. Determine the top 10 performing schools based on combined SAT scores.
3. Identify the NYC borough with the largest standard deviation in combined SAT scores.
4. Analyze borough trends and provide additional insights into SAT performance.
5. Discuss the impact of SAT scores on college admissions.

## Data

The dataset, `schools.csv`, contains information on various NYC public schools, including the average scores for math, reading, and writing sections of the SAT. Each section has a maximum score of 800, making the total maximum possible SAT score 2400.

## Methodology

### Data Processing

The data was processed to:

1. Identify schools with the best math results.
2. Calculate the total SAT scores for each school.
3. Determine the top 10 performing schools based on combined SAT scores.
4. Analyze borough trends by calculating the average and standard deviation of total SAT scores for each borough.
5. Provide additional insights by identifying schools with the highest reading and writing scores, and those with the lowest total SAT scores.

### Visualizations

The following visualizations were created to support the analysis:

1. **Best Math Schools**: Bar chart of schools with the highest average math scores.![image](https://github.com/Saif-Ur-Rehmn/portfolio/assets/62953610/ec00f29c-c412-4905-9788-10341c93f834)

2. **Top 10 Performing Schools**: Bar chart of the top 10 schools based on total SAT scores.![image](https://github.com/Saif-Ur-Rehmn/portfolio/assets/62953610/ce2ee041-bc56-4793-b789-b015417f9a3e)

3. **Distribution of SAT Scores**: Histogram showing the distribution of total SAT scores across all schools.![image](https://github.com/Saif-Ur-Rehmn/portfolio/assets/62953610/eedfd0ef-961c-4173-ac45-6a77fd57faf7)

4. **Average Total SAT Scores by Borough**: Bar chart showing the average total SAT scores by borough.![image](https://github.com/Saif-Ur-Rehmn/portfolio/assets/62953610/0b2067f6-a93b-4cfb-a251-1227afc248ad)

5. **Number of Schools by Borough**: Bar chart showing the number of schools in each borough.![image](https://github.com/Saif-Ur-Rehmn/portfolio/assets/62953610/ef1f1570-ce00-4d51-aabe-6fd9f5bb3716)


## Results

### Best Math Schools

The schools with the highest average math scores are:
1. Stuyvesant High School: 754
2. Bronx High School of Science: 714
3. Staten Island Technical High School: 711

### Top 10 Performing Schools

The top 10 schools based on total SAT scores are:
1. Stuyvesant High School: 2144
2. Bronx High School of Science: 2041
3. Staten Island Technical High School: 2041

### Borough with Largest Standard Deviation

Manhattan has the largest standard deviation in total SAT scores, indicating the highest variability in school performance within this borough.

### Additional Insights

- **Best Reading and Writing Schools**: Stuyvesant High School, High School of American Studies at Lehman College, and Bronx High School of Science excel in both reading and writing.
- **Lowest SAT Schools**: Pan American International High School at Monroe and Multicultural High School have the lowest total SAT scores.

### Borough Trends Analysis

The analysis of SAT performance across different NYC boroughs reveals distinct trends and insights. Each borough exhibits unique characteristics in terms of average SAT scores, the number of schools, and variability in performance.

## Impact of SAT Scores on College Admissions

SAT scores significantly influence college admissions by serving as a standardized measure for comparing students across different educational backgrounds. High SAT scores can enhance admission chances, qualify students for scholarships, and allow placement in advanced courses. Conversely, low SAT scores may necessitate remedial courses. Additionally, some colleges adopt test-optional policies to promote diversity and inclusion.

## Repository Contents

- `data/schools.csv`: Dataset containing SAT scores of NYC public schools.
- `notebook/notebook.ipynb`: Jupyter notebook containing the data processing and analysis code.
- `reports/Report-SATAnalysis.pdf.docx`: Detailed project report in DOCX format.
- `README.md`: This file.

## How to Use

1. Clone this repository.
2. Open `notebook.ipynb` to explore the data processing and analysis steps.
3. Review the `Report-SATAnalysis.pdf` for detailed insights and visualizations.
4. Use the provided visualizations to understand the SAT performance trends across NYC public schools.

## Conclusion

This analysis provides valuable insights into SAT performance across NYC public schools, highlighting top-performing schools and borough trends. Understanding these patterns can aid policymakers, educators, and parents in making informed decisions to improve educational outcomes and support student success in college admissions.

