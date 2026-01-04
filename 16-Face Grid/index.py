import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")

# Create a FacetGrid
g = sns.FacetGrid(tips, col="sex", row="time", hue="smoker")  # split by sex (columns) and time (rows)
g.map(sns.scatterplot, "total_bill", "tip")                  # plot scatterplot on each facet
g.add_legend()

plt.show()
