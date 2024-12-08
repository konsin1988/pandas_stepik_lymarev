import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

empl = pd.read_parquet('../tables/employees.parquet')

print(empl['pos_name'].memory_usage())

empl['pos_name'] = pd.Categorical(empl['pos_name'])

print(pd.cut(empl['salary'], bins=10, labels=range(0, 100, 10)))
# print(
#     pd.cut(
#         empl['salary'],
#         bins=[0, 20000, 50000, 100000, 1000000],
#         labels=['Низкая', 'Средняя', 'Выше среднего', 'Высокая']
#     )
# )

 # barplot "Type of Salary"
# (
#     pd.cut(empl['salary'], 
#         bins=[0, 20000, 50000, 100000, 500000],
#         labels=['Low', 'Low mid', 'Mid', 'High'])
#     .value_counts(sort=False)
#     .plot(kind='bar', figsize=(10, 8))
# )
# plt.show()

# qcut - Равные по кол-ву элементов интервалы
print(pd.qcut(empl['salary'], q = 4))

print(
    empl
    .query('report_dt == "2022-12-31"')
    .assign(salary_bin = lambda df: pd.qcut(df['salary'], q =5))
    .groupby(['sex', 'education', 'salary_bin'])
    .sample(frac=0.3, random_state=10)
    [-['salary']]
)