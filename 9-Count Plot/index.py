import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'HR']
}

# Count plot
sns.countplot(x='Department', data=data, palette='Set2')

# Titles and labels
plt.title("Count of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")

plt.show()
