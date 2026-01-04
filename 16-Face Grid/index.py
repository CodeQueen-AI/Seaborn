import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

g = sns.FacetGrid(tips, col="sex", row="time", hue="smoker")  
g.map(sns.scatterplot, "total_bill", "tip")          
g.add_legend()

plt.show()
