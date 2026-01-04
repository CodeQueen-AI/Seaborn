import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance', 'Marketing', 'Marketing'],
    'Salary': [40000, 42000, 50000, 52000, 45000, 47000, 30000, 35000]
}

# Violin plot
sns.violinplot(x='Department', y='Salary', data=data, palette='Pastel1')

# Titles and labels
plt.title("Salary Distribution by Department (Violin Plot)")
plt.xlabel("Department")
plt.ylabel("Salary")

plt.show()
