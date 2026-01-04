import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randint(50, 100, size=(5, 5)),
    columns=['Math', 'Physics', 'Chemistry', 'Biology', 'English'],
    index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5']
)

sns.clustermap(data, cmap='coolwarm', standard_scale=1, annot=True)

plt.title("Student Scores Cluster Map", pad=100) 
plt.show()
