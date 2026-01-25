import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    'Math': [80, 90, 70, 85],
    'Physics': [75, 95, 65, 80],
    'Chemistry': [70, 85, 75, 90]
})

sns.heatmap(data.corr(), annot=True, cmap='coolwarm')

plt.title("Subjects Correlation Heatmap")
plt.show()
