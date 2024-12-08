import pandas as pd 
import numpy as np 

empl = pd.read_parquet('../tables/employees.parquet')

# mean salary -------------------------------------
print(
    empl
    .groupby(['report_dt'], as_index = False)
    [['salary']]
    .mean()
    .round(2)
    # .reset_index()  # add index
    .head(20)
)
# dropna ------------------------------------
print(
    empl
    .groupby('employee_evaluation', dropna=False)
    [['salary']]
    .mean()
    .round(2)
)

# agg -----------------------------
print(
    empl
    .groupby('report_dt')
    [['salary']]
    .agg(['mean', 'std'])
    .head(10)
)

# list of counting columns
print(
    empl
    .groupby(['report_dt'])
    [['salary', 'birth_date']]
    .agg(['min', 'max'])
    .head(20)
)

# dict to agg
print(
    empl
    .groupby('report_dt')
    .agg({'salary': ['mean', 'std'], 'birth_date': 'min'})
    .head(20)
)

# grouping by many columns
# Средняя зп за месяц по разным должностям
print(
    empl
    .dropna()
    .groupby(['report_dt', 'pos_name'])
    [['salary', 'employee_evaluation']]
    .mean()
    .round(2)
    .head(20)
)

# Максимальная зп у каждого сотрудника
print(
    empl
    .groupby(['i_pernr','fio', 'birth_date'])
    [['salary']]
    .max()
    .head(20)
)

