import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
iris = sns.load_dataset("iris")

# Create a PairGrid
g = sns.PairGrid(iris, hue="species")  # hue adds color by species
g.map_upper(sns.scatterplot)           # scatter plots in upper triangle
g.map_lower(sns.kdeplot)               # kde plots in lower triangle
g.map_diag(sns.histplot)               # histogram on diagonal
g.add_legend()

plt.show()
