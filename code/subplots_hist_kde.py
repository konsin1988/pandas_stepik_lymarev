import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

empl = pd.read_parquet('../tables/employees.parquet')
plt.figure(figsize=(11, 8))

plt.subplot(1, 2, 1)
(sns.histplot(data=empl, 
            x='salary',
            binwidth=5000,
            binrange=(20000, 155000),
            stat='percent'
            )
    .set(title='Hist of salary', xlabel='Salary, rub', ylabel='Percent')
)
plt.xticks([x for x in range(20000, 160001, 20000)], rotation=20)
plt.grid(alpha=0.2, color='grey')
plt.axvline(x=empl['salary'].mean(), color='red')

plt.subplot(1, 2, 2)
(sns.kdeplot(data=empl, 
            x='salary',
            common_norm=False,
            fill=True,
            bw_method=0.05)
    .set(title='KDE of salary', xlabel='Salary, rub', ylabel='Percent')
)
plt.xticks([x for x in range(20000, 160001, 20000)], rotation=20)
plt.grid(alpha=0.2, color='grey')
plt.axvline(x=empl['salary'].mean(), color='red')

plt.show()