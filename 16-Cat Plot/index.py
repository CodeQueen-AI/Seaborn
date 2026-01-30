import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.catplot(x="day", y="tip", hue="sex", kind="box", data=tips)

plt.title("Tip by Day and Sex")
plt.show()