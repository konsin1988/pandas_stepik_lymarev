import pandas as pd 
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt 

empl = pd.read_parquet('../tables/employees.parquet').query('report_dt >= "2022-10-31"').replace({'mgmt_flag': {0: 'pure', 1: 'rich'}})

plt.figure(figsize=(10, 8))
sns.violinplot(data=empl, y='salary', x='report_dt', hue='mgmt_flag')

plt.show()