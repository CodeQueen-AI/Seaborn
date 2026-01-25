import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Age': [23, 25, 30, 35, 40, 45, 50],
    'Salary': [25000, 27000, 35000, 40000, 45000, 50000, 60000]
}

sns.scatterplot(x='Age', y='Salary', data=data, s=100)

plt.title("Age vs Salary Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()