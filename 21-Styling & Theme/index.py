import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------
# Dataset
# -----------------------
tips = sns.load_dataset("tips")

# -----------------------
# Styling Setup
# -----------------------
sns.set_theme(style="whitegrid")                 # overall theme
sns.set_context("talk")                          # larger labels
palette_main = sns.cubehelix_palette(start=2, rot=0, dark=0.3, light=0.8)
palette_light = sns.light_palette("blue", reverse=True)
palette_dark = sns.dark_palette("purple", reverse=True)

# -----------------------
# Single Plot: Violin Plot
# -----------------------
plt.figure(figsize=(10,6))
sns.violinplot(x="day", y="tip", hue="smoker", data=tips, split=True, palette=palette_light)

# Titles & labels
plt.title("Styling Demo: Violin Plot of Tips by Day & Smoker", fontsize=18, weight='bold')
plt.xlabel("Day of Week", fontsize=14)
plt.ylabel("Tip ($)", fontsize=14)

# Show
plt.show()
