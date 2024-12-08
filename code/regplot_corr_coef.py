import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 

empl = pd.read_parquet('../tables/employees.parquet').query('report_dt >= "2022-10-31"')

mean = [0, 0]
cov = [[1, 0.3], [0.3, 1]] 

x, y = np.random.multivariate_normal(mean, cov, 5000).T
sns.regplot(x=x, y=y)
plt.axis('equal')


plt.show()