import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

empl = pd.read_parquet('../tables/employees.parquet')

plt.figure(figsize=(10, 9))

(sns.histplot(data=empl,
            x='salary',
            binwidth = 5000,
            binrange=(20000, 155000),
            stat='percent')
    .set(title='Hist plot of Salary', xlabel='Salary, rub', ylabel='Percent'))
plt.xticks([x for x in range(20000, 161001, 10000)], rotation=20)

plt.axvline(x=empl['salary'].quantile(0.9), color='red')

plt.annotate(f'90% of people have \nthe same or less salary', (empl['salary'].quantile(0.9)+1000, 10), xytext=(empl['salary'].quantile(0.9) + 5000, 20), fontsize=12, arrowprops={'arrowstyle': '->', 'alpha': 0.4})

plt.show()