import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")

# Joint plot: scatter with histograms
sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")

plt.show()
