import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")

# Regression plot with category separation
sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips, markers=["o", "s"], palette="Set1")

plt.title("Regression by Sex")
plt.show()
