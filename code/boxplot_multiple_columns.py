import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

plt.figure(figsize=(10, 9))
empl = pd.read_parquet('../tables/employees.parquet').query('report_dt >= "2022-10-31"')[['report_dt', 'fio', 'sex', 'birth_date', 'mgmt_flag', 'employee_evaluation', 'salary']]

sns.boxplot(data=empl.replace({'mgmt_flag': {0: 'pure', 1: 'rich'}}), y='salary', x='report_dt', hue='mgmt_flag').set(title='Boxplot of salary in varios dates', ylabel='Salary, rub', xlabel='dates')
plt.legend(loc='upper right')

plt.show()