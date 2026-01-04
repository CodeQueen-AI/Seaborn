import seaborn as sns
import matplotlib.pyplot as plt
data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance', 'Marketing', 'Marketing'],
    'Salary': [40000, 42000, 50000, 52000, 45000, 47000, 30000, 35000]
}

sns.stripplot(x='Department', y='Salary', data=data, color='purple', size=8, jitter=True)

plt.title("Salary Distribution by Department (Strip Plot)")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()
