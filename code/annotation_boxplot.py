import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

empl = pd.read_parquet('../tables/employees.parquet').query('report_dt >= "2022-10-31"')[['report_dt', 'fio', 'sex', 'birth_date', 'mgmt_flag', 'employee_evaluation', 'salary']]

plt.figure(figsize=(10, 8))
sns.boxplot(data=empl, y='salary').set(title='Boxplot of salary', ylabel='Salary, rub')
plt.yticks([i for i in range(20000, 161000, 10000)], rotation=10, fontsize=8)
# plt.ylim(15000, 80000)
plt.annotate(f'Annotation of boxplot', (0.05, empl['salary'].quantile(0.75)), xytext=(0.1, 70000), fontsize=12, arrowprops={'arrowstyle': '->', 'alpha': 0.4, 'color': 'green'})
plt.axhline(empl['salary'].median(), color='red')

plt.show()