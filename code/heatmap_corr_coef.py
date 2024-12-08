import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 


marks = pd.read_csv('../tables/оценки 6Д.csv')

plt.figure(figsize=(9, 9))
# print(marks.corr(numeric_only=True))
sns.heatmap(marks.corr(numeric_only=True), annot=True, cmap=sns.color_palette('coolwarm', n_colors=8), vmin=-1, vmax=1)

plt.show()