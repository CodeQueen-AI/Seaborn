import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

plt.figure(figsize=(10,6))
sns.regplot(x="total_bill", y="tip", data=tips, color="teal", scatter_kws={'s':60})

plt.title("Annotations & Highlights Demo: Tip vs Total Bill", fontsize=18, weight='bold')
plt.xlabel("Total Bill ($)", fontsize=14)
plt.ylabel("Tip ($)", fontsize=14)

plt.axhline(y=tips['tip'].mean(), color='red', linestyle='--', label="Mean Tip")
plt.axvline(x=tips['total_bill'].mean(), color='blue', linestyle='--', label="Mean Total Bill")
plt.fill_between([0, 60], 5, 10, color='yellow', alpha=0.1)

plt.annotate("Highest tip observed", xy=(50, 10), xytext=(30, 12),
             arrowprops=dict(facecolor='red', shrink=0.05, width=2),
             fontsize=12, color="darkred")

plt.legend()

plt.show()