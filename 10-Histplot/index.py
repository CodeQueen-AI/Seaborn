import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'Salary': [30000, 40000, 50000, 45000, 35000, 60000, 70000, 50000]
}

# Histogram
sns.histplot(data['Salary'], bins=5, kde=True, color='skyblue')

# Titles and labels
plt.title("Salary Distribution Histogram")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()
