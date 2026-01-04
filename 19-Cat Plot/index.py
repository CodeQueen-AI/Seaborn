import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
tips = sns.load_dataset("tips")

# Categorical plot: boxplot for tip by day, split by sex
sns.catplot(x="day", y="tip", hue="sex", kind="box", data=tips)

plt.title("Tip by Day and Sex")
plt.show()
