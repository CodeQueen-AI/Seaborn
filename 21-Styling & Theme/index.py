import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(style="whitegrid")      
sns.set_context("talk")                         
palette_main = sns.cubehelix_palette(start=2, rot=0, dark=0.3, light=0.8)
palette_light = sns.light_palette("blue", reverse=True)
palette_dark = sns.dark_palette("purple", reverse=True)

plt.figure(figsize=(10,6))
sns.violinplot(x="day", y="tip", hue="smoker", data=tips, split=True, palette=palette_light)

plt.title("Styling Demo: Violin Plot of Tips by Day & Smoker", fontsize=18, weight='bold')
plt.xlabel("Day of Week", fontsize=14)
plt.ylabel("Tip ($)", fontsize=14)
plt.show()
