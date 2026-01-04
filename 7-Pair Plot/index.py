import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'SepalLength': [5.1, 4.9, 6.7, 5.6, 5.9],
    'SepalWidth': [3.5, 3.0, 3.1, 2.9, 3.0],
    'PetalLength': [1.4, 1.4, 5.6, 4.2, 5.1],
    'PetalWidth': [0.2, 0.2, 2.4, 1.5, 1.8],
    'Species': ['Setosa', 'Setosa', 'Virginica', 'Versicolor', 'Virginica']
})

# Pair plot
sns.pairplot(data, hue='Species', palette='bright')

plt.show()
