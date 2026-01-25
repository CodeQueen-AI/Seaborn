import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance', 'Marketing', 'Marketing'],
    'Salary': [40000, 42000, 50000, 52000, 45000, 47000, 30000, 35000]
}

sns.boxplot(x='Department', y='Salary', data=data, palette='Set2')

plt.title("Salary Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()