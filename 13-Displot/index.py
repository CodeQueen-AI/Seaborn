import seaborn as sns
import matplotlib.pyplot as plt

data = [30000, 40000, 50000, 45000, 35000, 60000, 70000, 50000]

sns.displot(data, bins=5, kde=True, color='orange', height=5, aspect=1.5)

plt.title("Salary Distribution (displot)")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
