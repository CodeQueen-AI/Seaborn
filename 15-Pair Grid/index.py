import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")

g = sns.PairGrid(iris, hue="species") 
g.map_upper(sns.scatterplot)        
g.map_lower(sns.kdeplot)        
g.map_diag(sns.histplot)             
g.add_legend()

plt.show()