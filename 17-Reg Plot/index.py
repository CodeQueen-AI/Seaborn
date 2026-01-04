import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")

# Simple regression plot
sns.regplot(x="total_bill", y="tip", data=tips)

plt.title("Regression of Tip vs Total Bill")
plt.show()
