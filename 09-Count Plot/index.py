import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Department': ['HR', 'IT', 'Finance', 'HR', 'IT', 'Finance', 'IT', 'HR']
}

sns.countplot(x='Department', data=data, palette='Set2')
plt.title("Count of Employees by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()