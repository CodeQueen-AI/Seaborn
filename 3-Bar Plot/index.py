import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Products': ['A', 'B', 'C', 'D'],
    'Sales': [150, 200, 300, 250]
}

sns.barplot(x='Products', y='Sales', data=data, palette='viridis')

plt.title("Product-wise Sales Bar Plot")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()