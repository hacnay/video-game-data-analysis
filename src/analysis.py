"""
Video Game Data Analysis
Project: Visualizing Data Distributions and Analyzing Relationships

Run from the repository root:
    python src/analysis.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "video_game_reviews.csv"
OUTPUT_DIR = ROOT / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)

required_columns = ["Player ID", "Hours Played", "Review Score"]
missing_columns = [column for column in required_columns if column not in df.columns]
if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

print("=" * 65)
print("VIDEO GAME DATA ANALYSIS")
print("=" * 65)
print(f"Rows: {len(df)} | Columns: {len(df.columns)}")
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isna().sum())
print(f"\nDuplicate rows: {df.duplicated().sum()}")
print(f"Duplicate Player IDs: {df['Player ID'].duplicated().sum()}")

numeric_columns = ["Hours Played", "Review Score"]

for column in numeric_columns:
    series = df[column].dropna()
    q1 = series.quantile(0.25)
    median = series.quantile(0.50)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    potential_outliers = series[(series < lower_fence) | (series > upper_fence)].tolist()

    print(f"\n--- {column} ---")
    print(f"Mean: {series.mean():.2f}")
    print(f"Median: {series.median():.2f}")
    print(f"Mode(s): {series.mode().tolist()}")
    print(f"Minimum: {series.min():g}")
    print(f"Maximum: {series.max():g}")
    print(f"Sample standard deviation: {series.std(ddof=1):.2f}")
    print(
        "Five-number summary:",
        {
            "Minimum": series.min(),
            "Q1": q1,
            "Median": median,
            "Q3": q3,
            "Maximum": series.max(),
        },
    )
    print(f"IQR: {iqr:.2f}")
    print(f"Outlier fences: [{lower_fence:.2f}, {upper_fence:.2f}]")
    print(f"Potential outliers: {potential_outliers}")

    # Save a box plot for each numerical variable
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.boxplot(series, vert=False, showmeans=True)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_yticks([])
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    safe_name = column.lower().replace(" ", "_")
    fig.savefig(OUTPUT_DIR / f"{safe_name}_boxplot.png", dpi=220, bbox_inches="tight")
    plt.close(fig)

correlation = df["Hours Played"].corr(df["Review Score"])
print(f"\nPearson correlation (Hours Played vs Review Score): {correlation:.6f}")

# Save scatter plot with linear trendline
fig, ax = plt.subplots(figsize=(7.5, 5))
ax.scatter(df["Hours Played"], df["Review Score"], alpha=0.8)
slope, intercept = __import__("numpy").polyfit(df["Hours Played"], df["Review Score"], 1)
x_values = __import__("numpy").linspace(df["Hours Played"].min(), df["Hours Played"].max(), 100)
ax.plot(x_values, slope * x_values + intercept, linestyle="--", linewidth=1.5)
ax.set_title("Relationship Between Hours Played and Review Score")
ax.set_xlabel("Hours Played")
ax.set_ylabel("Review Score")
ax.grid(alpha=0.25)
ax.text(
    0.03, 0.96, f"Pearson r = {correlation:.3f}",
    transform=ax.transAxes, va="top",
    bbox={"boxstyle": "round,pad=0.3", "facecolor": "white", "alpha": 0.8},
)
fig.tight_layout()
fig.savefig(OUTPUT_DIR / "scatter_plot.png", dpi=220, bbox_inches="tight")
plt.close(fig)

print(f"\nCharts saved to: {OUTPUT_DIR}")
