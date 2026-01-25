import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Month': [1, 2, 3, 4, 5, 6],
    'Sales': [200, 250, 300, 350, 400, 450]
}

sns.lineplot(x='Month', y='Sales', data=data, marker='o')

plt.title("Monthly Sales Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()