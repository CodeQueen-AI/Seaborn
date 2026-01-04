import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lmplot(x="total_bill", y="tip", hue="sex", data=tips, markers=["o", "s"], palette="Set1")

plt.title("Regression by Sex")
plt.show()
