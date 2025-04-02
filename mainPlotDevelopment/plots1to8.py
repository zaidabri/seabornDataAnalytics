import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.set(style="whitegrid")

plt.figure(figsize=(20, 15))

plt.subplot(4, 2, 1)
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

plt.subplot(4, 2, 2)
sns.boxplot(data=tips, x="day", y="tip", palette="Set2")

plt.subplot(4, 2, 3)
sns.histplot(data=tips, x="total_bill", kde=True, color="skyblue")

plt.subplot(4, 2, 4)
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", split=True)

plt.subplot(4, 2, 5)
sns.barplot(data=tips, x="day", y="tip", hue="smoker")

plt.subplot(4, 2, 6)
sns.stripplot(data=tips, x="day", y="tip", jitter=True, hue="sex", dodge=True)

plt.subplot(4, 2, 7)
sns.countplot(data=tips, x="day", hue="sex")

plt.subplot(4, 2, 8)
sns.lineplot(data=tips.sort_values("size"), x="size", y="total_bill", marker="o")

plt.tight_layout()
plt.show()
