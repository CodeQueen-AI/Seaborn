import seaborn as sns
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85]

sns.kdeplot(marks, fill=True)
plt.title("Marks Density")
plt.show()