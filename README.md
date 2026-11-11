# Visualizing Data Distributions and Analyzing Relationships

A Python-based exploratory data analysis project using a video game player dataset.

## Project overview

This project examines the distribution of player hours and review scores, identifies potential outliers, and investigates the linear relationship between the two numerical variables.

Report Link- https://docs.google.com/document/d/1GdQcHfH7QPKfuaeFGBZQ0MmWo7XKd-aYs_4vwWlbMto

## Dataset

- **File:** `data/video_game_reviews.csv`
- **Records:** 60
- **Attributes:** 3
- **Columns:** Player ID, Hours Played, Review Score

The CSV supplied for the assignment is included in this repository. Player ID is an identifier; the quantitative analysis focuses on Hours Played and Review Score.

## Tools and libraries

- Python
- Pandas
- NumPy
- Matplotlib

## Analysis performed

1. Dataset inspection and data-type review.
2. Missing-value and duplicate checks.
3. Mean, median, mode, minimum, maximum and sample standard deviation.
4. Five-number summary and interquartile range.
5. Potential outlier detection using the 1.5 × IQR rule.
6. Box plots for Hours Played and Review Score.
7. Scatter plot and Pearson correlation analysis.

## Key results

- Average Hours Played: **16.33**
- Average Review Score: **80.62**
- Pearson correlation: **0.007**
- Potential Hours Played outliers: **40 and 45 hours**
- Potential Review Score outliers: **None** under the 1.5 × IQR rule.

The correlation is very close to zero, indicating virtually no linear association in this dataset. Correlation does not establish causation.

## Repository structure

```text
video-game-data-analysis/
├── data/
│   └── video_game_reviews.csv
├── outputs/
│   ├── dataset_preview.png
│   ├── hours_played_boxplot.png
│   ├── review_score_boxplot.png
│   └── scatter_plot.png
├── src/
│   └── analysis.py
├── .gitignore
├── README.md
└── requirements.txt
```

## How to run

1. Install Python 3.9 or newer.
2. Clone or download this repository.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. From the repository root, run:

   ```bash
   python src/analysis.py
   ```

The script prints the statistical results and saves the visualizations in the `outputs/` folder.

## Notes

- The original data is retained; the script does not delete observations.
- Outliers are flagged for investigation, not automatically removed.
- Results describe this supplied dataset and should not automatically be generalized to all video game players.

## Author

Subhang Kumar
